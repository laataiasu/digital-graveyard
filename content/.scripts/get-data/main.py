from config import DATA_SOURCES
from processor import process_source

def main():
    """Main function to process all configured data sources."""
    for source_name, config in DATA_SOURCES.items():
        print(f"Processing {source_name}...")
        try:
            process_source(config)
            print(f"Successfully processed {source_name}.")
        except Exception as e:
            print(f"Error processing {source_name}: {e}")
        print("-" * 20)

if __name__ == "__main__":
    main()
