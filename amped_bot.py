#!/usr/bin/env python3
"""
AMPED Marketing Update Research Bot

Usage:
    python amped_bot.py "Artist Name"
"""
import sys
import argparse
from research import search_artist_info, search_social_stats
from formatter import format_update_with_claude
import config


def main():
    parser = argparse.ArgumentParser(
        description="Generate AMPED marketing updates for artists",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python amped_bot.py "Jane Remover"
  python amped_bot.py "YHWH Nailgun"
  python amped_bot.py "Free Throw"

Make sure to set ANTHROPIC_API_KEY and SERPAPI_KEY in your .env file first!
        """
    )
    parser.add_argument("artist", help="Artist name to research")
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: prints to console)",
        default=None
    )
    parser.add_argument(
        "--skip-social",
        help="Skip social media stats search",
        action="store_true"
    )

    args = parser.parse_args()

    artist_name = args.artist

    print("=" * 60)
    print("🎵 AMPED Marketing Update Research Bot")
    print("=" * 60)

    # Check API keys
    if not config.ANTHROPIC_API_KEY:
        print("\n❌ ERROR: ANTHROPIC_API_KEY not found!")
        print("   Please create a .env file and add your Anthropic API key:")
        print("   ANTHROPIC_API_KEY=your_key_here")
        print("\n   Get your API key from: https://console.anthropic.com/")
        sys.exit(1)

    if not config.SERPAPI_KEY:
        print("\n⚠️  WARNING: SERPAPI_KEY not found!")
        print("   Search results will be limited without it.")
        print("   Get your API key from: https://serpapi.com/")
        print("\n   Add to .env file:")
        print("   SERPAPI_KEY=your_key_here")
        print("\n   Continuing anyway...\n")

    # Step 1: Research the artist
    research_data = search_artist_info(artist_name)

    # Step 2: Search for social media stats (optional)
    if not args.skip_social:
        social_stats = search_social_stats(artist_name)
        research_data["social_stats"] = social_stats

    # Step 3: Format the update with Claude
    formatted_update = format_update_with_claude(research_data)

    if not formatted_update:
        print("\n❌ Failed to generate update")
        sys.exit(1)

    # Output the result
    print("\n" + "=" * 60)
    print("📄 FORMATTED AMPED UPDATE")
    print("=" * 60 + "\n")

    print(formatted_update)

    # Save to file if requested
    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(formatted_update)
            print(f"\n✅ Saved to {args.output}")
        except Exception as e:
            print(f"\n❌ Error saving file: {str(e)}")

    print("\n" + "=" * 60)
    print("✨ Done! Copy the update above for your AMPED report.")
    print("=" * 60)


if __name__ == "__main__":
    main()
