# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "beautifulsoup4>=4.12.0",
#     "curl-cffi>=0.7.0",
#     "pandas>=2.2.0",
#     "pyyaml>=6.0.0",
#     "requests>=2.31.0",
# ]
# ///

import argparse
import sys
import time
from config import DATA_SOURCES
from processor import process_source


def main():
    """Main CLI entrypoint to fetch and process media consumption data."""
    parser = argparse.ArgumentParser(
        description="Automated media consumption ingestion for Digital Graveyard (Goodreads, Letterboxd, AniList, MyDramaList)."
    )
    parser.add_argument(
        "--source",
        "-s",
        type=str,
        choices=list(DATA_SOURCES.keys()) + ["all"],
        default="all",
        help="Specific data source to process (default: all)",
    )
    parser.add_argument(
        "--check",
        "--dry-run",
        action="store_true",
        help="Run in check/dry-run mode to verify API connectivity and record counts without writing files.",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all configured data sources.",
    )

    args = parser.parse_args()

    if args.list:
        print("Configured Data Sources:")
        for name, cfg in DATA_SOURCES.items():
            print(f"  - {name:15}: {cfg.get('description', name)}")
        sys.exit(0)

    sources_to_run = (
        DATA_SOURCES.items()
        if args.source == "all"
        else [(args.source, DATA_SOURCES[args.source])]
    )

    mode_label = " [CHECK / DRY-RUN MODE]" if args.check else ""
    print("=" * 65)
    print(f"🚀 Starting Media Consumption Ingestion{mode_label}")
    print("=" * 65)

    results = {}
    errors = {}
    start_time = time.time()

    for source_name, config in sources_to_run:
        desc = config.get("description", source_name)
        print(f"\n📦 Processing: {desc} ({source_name})...")
        try:
            count = process_source(config, dry_run=args.check)
            results[source_name] = count
            print(f"✅ Finished: {desc} ({count} notes)")
        except Exception as e:
            errors[source_name] = str(e)
            print(f"❌ Error in {source_name}: {e}")
        print("-" * 45)

    total_time = time.time() - start_time
    print("\n" + "=" * 65)
    print("📊 Ingestion Summary Report")
    print("=" * 65)

    for source_name, config in sources_to_run:
        desc = config.get("description", source_name)
        if source_name in results:
            action = "records verified" if args.check else "notes synced"
            print(f"  ✅ {desc:32}: {results[source_name]:4d} {action}")
        else:
            print(f"  ❌ {desc:32}: FAILED -> {errors.get(source_name, 'Unknown error')}")

    print(f"\n⏱️  Total time: {total_time:.2f}s")

    if errors:
        print("\n⚠️  Some sources failed to complete. Please review the errors above.")
        sys.exit(1)
    else:
        if not args.check:
            print("🎉 All sources synced successfully! Run `npx quartz build` to check site.")
        else:
            print("🎉 Pre-flight health check passed for all sources.")


if __name__ == "__main__":
    main()
