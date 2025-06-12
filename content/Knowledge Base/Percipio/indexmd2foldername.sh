find . -type f -name "index.md" | while read filepath; do
  dir=$(dirname "$filepath")
  folder=$(basename "$dir")
  newpath="$dir/$folder.md"
  mv "$filepath" "$newpath"
done
