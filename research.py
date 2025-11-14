"""
Web research module for gathering artist information
"""
import requests
from datetime import datetime
from serpapi import GoogleSearch
import config


def search_artist_info(artist_name):
    """
    Search for artist information using SerpAPI and web scraping

    Args:
        artist_name: Name of the artist to research

    Returns:
        dict with search results organized by category
    """
    print(f"\n🔍 Researching {artist_name}...")

    current_year = config.CURRENT_YEAR
    results = {
        "artist_name": artist_name,
        "search_date": datetime.now().strftime("%Y-%m-%d"),
        "releases": [],
        "tours": [],
        "press": [],
        "other_updates": []
    }

    if not config.SERPAPI_KEY:
        print("⚠️  Warning: SERPAPI_KEY not found. Set it in .env file for better results.")
        return results

    # Search queries to run
    queries = [
        f'{artist_name} new album single {current_year}',
        f'{artist_name} tour dates {current_year}',
        f'{artist_name} interview press {current_year}',
        f'{artist_name} announced {current_year}'
    ]

    all_results = []

    for query in queries:
        print(f"   Searching: {query}")
        try:
            search = GoogleSearch({
                "q": query,
                "api_key": config.SERPAPI_KEY,
                "num": 10  # Get top 10 results per query
            })
            search_results = search.get_dict()

            if "organic_results" in search_results:
                all_results.extend(search_results["organic_results"])

        except Exception as e:
            print(f"   ⚠️  Search error: {str(e)}")
            continue

    # Organize results
    print(f"\n📊 Found {len(all_results)} total results")

    for result in all_results:
        title = result.get("title", "")
        link = result.get("link", "")
        snippet = result.get("snippet", "")
        source = result.get("source", "")

        # Categorize by keywords
        text_to_check = (title + " " + snippet).lower()

        # Check if it's from a credible press outlet
        is_press = any(outlet.lower() in source.lower() for outlet in config.PRESS_OUTLETS)

        result_data = {
            "title": title,
            "link": link,
            "snippet": snippet,
            "source": source
        }

        # Categorize
        if any(keyword in text_to_check for keyword in ["album", "single", "ep", "release", "out now"]):
            results["releases"].append(result_data)
        elif any(keyword in text_to_check for keyword in ["tour", "concert", "live", "festival", "show dates"]):
            results["tours"].append(result_data)
        elif is_press or any(keyword in text_to_check for keyword in ["interview", "feature", "review", "premiere"]):
            results["press"].append(result_data)
        else:
            results["other_updates"].append(result_data)

    print(f"   📀 Releases: {len(results['releases'])}")
    print(f"   🎸 Tours: {len(results['tours'])}")
    print(f"   📰 Press: {len(results['press'])}")
    print(f"   ℹ️  Other: {len(results['other_updates'])}")

    return results


def search_social_stats(artist_name):
    """
    Search for artist social media statistics

    Args:
        artist_name: Name of the artist

    Returns:
        dict with social media stats
    """
    print(f"\n📱 Searching social media stats for {artist_name}...")

    stats = {
        "instagram": None,
        "spotify": None,
        "twitter": None,
        "tiktok": None
    }

    if not config.SERPAPI_KEY:
        return stats

    # Search for social stats
    query = f'{artist_name} instagram spotify followers monthly listeners'

    try:
        search = GoogleSearch({
            "q": query,
            "api_key": config.SERPAPI_KEY,
            "num": 5
        })
        search_results = search.get_dict()

        # Try to extract stats from snippets
        # Note: This is basic - you might need to scrape actual social media pages for accurate numbers
        if "organic_results" in search_results:
            for result in search_results["organic_results"]:
                snippet = result.get("snippet", "").lower()
                # Look for patterns like "123k followers" or "1.2m monthly listeners"
                # This is simplified - real implementation would be more robust
                print(f"   Found info from: {result.get('source', 'Unknown')}")

    except Exception as e:
        print(f"   ⚠️  Error: {str(e)}")

    print("   ℹ️  Note: Social stats extraction is basic. You may need to manually verify.")

    return stats
