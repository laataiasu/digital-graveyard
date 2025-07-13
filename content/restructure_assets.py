#!/usr/bin/env python3
"""
Markdown Asset Restructuring Tool

This script processes Markdown files in a directory and its subdirectories to:
1. Detect all asset references (images, audio, etc.)
2. Move assets to a root assets/ folder with subfolders based on Markdown filename
3. Download assets from URLs when possible
4. Update Markdown content to use Obsidian-style ![[asset.ext]] references
5. Convert Markdown image syntax ![title](url) to ![[asset.ext]]
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse
import requests
import mimetypes
from time import sleep

class MarkdownAssetRestructurer:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir).resolve()
        self.assets_dir = self.root_dir / "assets"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Common asset extensions
        self.asset_extensions = {
            '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg',  # Images
            '.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a',  # Audio
            '.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv',  # Video
            '.pdf', '.doc', '.docx', '.txt', '.rtf',  # Documents
            '.zip', '.rar', '.7z', '.tar', '.gz'  # Archives
        }
        
        # Regex patterns for asset references
        self.markdown_image_pattern = r'!\[([^\]]*)\]\(\s*<?([^)>]+?)>?\s*\)'
        self.obsidian_link_pattern = r'!\[\[([^\]]+)\]\]'
        self.html_img_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
        
    def is_asset_file(self, filepath):
        """Check if a file is an asset based on its extension."""
        return Path(filepath).suffix.lower() in self.asset_extensions
    
    def get_markdown_files(self):
        """Get all Markdown files in the directory and subdirectories."""
        markdown_files = []
        for pattern in ['*.md', '*.markdown']:
            markdown_files.extend(self.root_dir.rglob(pattern))
        return markdown_files
    
    def extract_asset_references(self, content):
        """Extract all asset references from Markdown content."""
        references = []
        
        # Find Markdown image syntax: ![alt](path)
        markdown_matches = re.finditer(self.markdown_image_pattern, content)
        for match in markdown_matches:
            alt_text = match.group(1)
            asset_path = match.group(2).strip()
            asset_path = asset_path.strip()
            if asset_path.startswith('<') and asset_path.endswith('>'):
                asset_path = asset_path[1:-1].strip()

            references.append({
                'type': 'markdown_image',
                'full_match': match.group(0),
                'alt_text': alt_text,
                'path': asset_path,
                'start': match.start(),
                'end': match.end()
            })
        
        # Find Obsidian-style links: ![[asset.ext]]
        obsidian_matches = re.finditer(self.obsidian_link_pattern, content)
        for match in obsidian_matches:
            asset_path = match.group(1)
            references.append({
                'type': 'obsidian_link',
                'full_match': match.group(0),
                'path': asset_path,
                'start': match.start(),
                'end': match.end()
            })
        
        # Find HTML img tags
        html_matches = re.finditer(self.html_img_pattern, content)
        for match in html_matches:
            asset_path = match.group(1)
            references.append({
                'type': 'html_img',
                'full_match': match.group(0),
                'path': asset_path,
                'start': match.start(),
                'end': match.end()
            })
        
        return references
    
    def get_file_extension_from_url(self, url, content_type=None):
        """Get file extension from URL or content type."""
        # First try to get extension from URL
        parsed_url = urlparse(url)
        path = Path(parsed_url.path)
        if path.suffix:
            return path.suffix.lower()
        
        # If no extension in URL, try to guess from content type
        if content_type:
            extension = mimetypes.guess_extension(content_type.split(';')[0])
            if extension:
                return extension.lower()
        
        # Default to .bin if we can't determine
        return '.bin'
    
    def download_asset(self, url, target_path):
        """Download an asset from a URL."""
        try:
            print(f"  Downloading: {url}")
            
            # Make the request
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Get content type
            content_type = response.headers.get('content-type', '')
            
            # If target path doesn't have extension, add one based on content type
            if not target_path.suffix:
                extension = self.get_file_extension_from_url(url, content_type)
                target_path = target_path.with_suffix(extension)
            
            # Create target directory
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Download the file
            with open(target_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"  Downloaded: {url} -> {target_path}")
            return target_path
            
        except Exception as e:
            print(f"  ERROR downloading {url}: {e}")
            return None
    
    def is_downloadable_url(self, url):
        """Check if a URL is downloadable as a binary asset (not embeds like YouTube)."""
        if not url.startswith(('http://', 'https://')):
            return False
        
        # Skip embed URLs that shouldn't be downloaded
        embed_domains = [
            'youtube.com', 'youtu.be', 'vimeo.com', 'dailymotion.com',
            'twitch.tv', 'twitter.com', 'x.com', 'instagram.com',
            'facebook.com', 'linkedin.com', 'tiktok.com', 'soundcloud.com',
            'spotify.com', 'apple.com/music', 'bandcamp.com',
            'codepen.io', 'jsfiddle.net', 'repl.it', 'codesandbox.io',
            'google.com/maps', 'openstreetmap.org'
        ]
        
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        
        # Remove 'www.' prefix for comparison
        if domain.startswith('www.'):
            domain = domain[4:]
        
        # Check if it's an embed domain
        for embed_domain in embed_domains:
            if domain == embed_domain or domain.endswith('.' + embed_domain):
                return False
        
        return True
    
    def resolve_asset_path(self, asset_path, markdown_file_path):
        """Resolve asset path - either local file or downloadable URL."""
        # Handle URL-encoded paths
        asset_path = unquote(asset_path)
        
        # Check if it's a downloadable URL (not embed URLs)
        if self.is_downloadable_url(asset_path):
            return {'type': 'url', 'path': asset_path}
        
        # Skip embed URLs, data URLs, and other non-downloadable URLs
        if asset_path.startswith(('http://', 'https://', 'ftp://', 'data:')):
            return {'type': 'skip', 'path': asset_path}
        
        # Handle local files
        if Path(asset_path).is_absolute():
            asset_file = Path(asset_path)
        else:
            # Resolve relative to the Markdown file's directory
            asset_file = (markdown_file_path.parent / asset_path).resolve()
        
        # Check if file exists and is an asset
        if asset_file.exists() and self.is_asset_file(asset_file):
            return {'type': 'file', 'path': asset_file}
        
        return None
    
    def get_target_asset_path(self, asset_info, markdown_file):
        """Get the target path for an asset in the assets directory."""
        # Get the full relative path of the markdown file from root
        markdown_relative_path = markdown_file.relative_to(self.root_dir)
        
        # Create subfolder structure based on the full relative path (without .md extension)
        subfolder_path = self.assets_dir / markdown_relative_path.parent / markdown_relative_path.stem
        
        if asset_info['type'] == 'file':
            # Use original filename for local files
            filename = asset_info['path'].name
        else:  # URL
            # Generate filename from URL
            parsed_url = urlparse(asset_info['path'])
            filename = Path(parsed_url.path).name
            
            # If no filename in URL, generate one from the domain and path
            if not filename:
                domain = parsed_url.netloc.replace('www.', '')
                # Create a meaningful filename from domain and path
                path_parts = [p for p in parsed_url.path.split('/') if p]
                if path_parts:
                    filename = f"{domain}_{path_parts[-1]}"
                else:
                    filename = f"{domain}_asset"
            
            # Clean up filename (remove invalid characters)
            filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
            
            # Ensure we have an extension
            if not Path(filename).suffix:
                filename += self.get_file_extension_from_url(asset_info['path'])
        
        target_path = subfolder_path / filename
        
        # Handle name conflicts by adding a number suffix
        counter = 1
        while target_path.exists():
            stem = Path(filename).stem
            suffix = Path(filename).suffix
            target_path = subfolder_path / f"{stem}_{counter}{suffix}"
            counter += 1
        
        return target_path
    
    def move_or_download_asset(self, asset_info, target_path):
        """Move a local asset or download from URL to the target location."""
        try:
            if asset_info['type'] == 'file':
                # Move local file
                target_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(asset_info['path']), str(target_path))
                print(f"  Moved: {asset_info['path']} -> {target_path}")
                return target_path
            else:  # URL
                # Download from URL
                result = self.download_asset(asset_info['path'], target_path)
                if result:
                    # Add a small delay to be respectful to servers
                    sleep(0.5)
                return result
        except Exception as e:
            print(f"  ERROR processing {asset_info['path']}: {e}")
            return None
    
    def update_markdown_content(self, content, references, markdown_file):
        """Update Markdown content with new asset references."""
        # Sort references by position (reverse order to maintain positions)
        references.sort(key=lambda x: x['start'], reverse=True)
        
        updated_content = content
        
        for ref in references:
            asset_info = self.resolve_asset_path(ref['path'], markdown_file)
            
            if asset_info:
                if asset_info['type'] == 'skip':
                    # For embed URLs (YouTube, etc.), convert to Obsidian format but don't download
                    if ref['type'] != 'obsidian_link':  # Only convert if not already in Obsidian format
                        new_reference = f"![[{asset_info['path']}]]"
                        updated_content = (
                            updated_content[:ref['start']] + 
                            new_reference + 
                            updated_content[ref['end']:]
                        )
                        print(f"    Converted to Obsidian format: {ref['path']}")
                    else:
                        print(f"    Keeping embed URL as-is: {ref['path']}")
                else:
                    # For downloadable URLs and local files
                    target_path = self.get_target_asset_path(asset_info, markdown_file)
                    result_path = self.move_or_download_asset(asset_info, target_path)
                    
                    if result_path:
                        # Create new Obsidian-style reference
                        new_reference = f"![[{result_path.name}]]"
                        
                        # Replace the reference in content
                        updated_content = (
                            updated_content[:ref['start']] + 
                            new_reference + 
                            updated_content[ref['end']:]
                        )
                        
                        print(f"    Updated reference: {ref['path']} -> {result_path.name}")
                    else:
                        print(f"    WARNING: Could not process asset, keeping original reference")
            else:
                print(f"    WARNING: Asset not found or not processable: {ref['path']}")
        
        return updated_content
    
    def process_markdown_file(self, markdown_file):
        """Process a single Markdown file."""
        print(f"\nProcessing: {markdown_file.relative_to(self.root_dir)}")
        
        try:
            # Read the file
            with open(markdown_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract asset references
            references = self.extract_asset_references(content)
            
            if not references:
                print("  No asset references found")
                return
            
            print(f"  Found {len(references)} asset reference(s)")
            
            # Update content and move/download assets
            updated_content = self.update_markdown_content(content, references, markdown_file)
            
            # Write updated content back to file
            if updated_content != content:
                with open(markdown_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"  Updated Markdown file")
            
        except Exception as e:
            print(f"  ERROR processing {markdown_file}: {e}")
    
    def run(self):
        """Run the asset restructuring process."""
        print(f"Starting asset restructuring in: {self.root_dir}")
        print(f"Assets will be moved to: {self.assets_dir}")
        
        # Get all Markdown files
        markdown_files = self.get_markdown_files()
        
        if not markdown_files:
            print("No Markdown files found!")
            return
        
        print(f"Found {len(markdown_files)} Markdown file(s)")
        
        # Create assets directory if it doesn't exist
        self.assets_dir.mkdir(exist_ok=True)
        
        # Process each Markdown file
        for markdown_file in markdown_files:
            self.process_markdown_file(markdown_file)
        
        print(f"\nAsset restructuring complete!")

def main():
    parser = argparse.ArgumentParser(description='Restructure Markdown assets and update references')
    parser.add_argument('directory', help='Root directory containing Markdown files')
    
    args = parser.parse_args()
    
    # Validate directory
    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return
    
    # Create and run the restructurer
    restructurer = MarkdownAssetRestructurer(args.directory)
    restructurer.run()

if __name__ == "__main__":
    main()