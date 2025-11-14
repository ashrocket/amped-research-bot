"""
Claude AI integration for formatting AMPED updates
"""
import anthropic
import config
import os


def load_format_examples():
    """Load the AMPED format examples from templates"""
    template_path = os.path.join(os.path.dirname(__file__), "templates", "amped_format_examples.md")

    with open(template_path, "r") as f:
        return f.read()


def format_update_with_claude(research_data):
    """
    Use Claude to format research data into an AMPED update

    Args:
        research_data: Dictionary containing search results

    Returns:
        Formatted AMPED update as a string
    """
    artist_name = research_data["artist_name"]

    print(f"\n🤖 Formatting update for {artist_name} with Claude...")

    if not config.ANTHROPIC_API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY not set in .env file")
        return None

    # Load format examples
    format_examples = load_format_examples()

    # Prepare the research data for Claude
    research_summary = f"""
# Research Data for {artist_name}
Search Date: {research_data['search_date']}

## Releases Found ({len(research_data['releases'])})
"""

    for idx, release in enumerate(research_data['releases'][:10], 1):  # Limit to top 10
        research_summary += f"\n{idx}. {release['title']}\n"
        research_summary += f"   Source: {release['source']}\n"
        research_summary += f"   Link: {release['link']}\n"
        research_summary += f"   Snippet: {release['snippet']}\n"

    research_summary += f"\n## Tour/Live Information Found ({len(research_data['tours'])})\n"

    for idx, tour in enumerate(research_data['tours'][:10], 1):
        research_summary += f"\n{idx}. {tour['title']}\n"
        research_summary += f"   Source: {tour['source']}\n"
        research_summary += f"   Link: {tour['link']}\n"
        research_summary += f"   Snippet: {tour['snippet']}\n"

    research_summary += f"\n## Press Coverage Found ({len(research_data['press'])})\n"

    for idx, press in enumerate(research_data['press'][:15], 1):  # More press items
        research_summary += f"\n{idx}. {press['title']}\n"
        research_summary += f"   Source: {press['source']}\n"
        research_summary += f"   Link: {press['link']}\n"
        research_summary += f"   Snippet: {press['snippet']}\n"

    research_summary += f"\n## Other Updates Found ({len(research_data['other_updates'])})\n"

    for idx, update in enumerate(research_data['other_updates'][:10], 1):
        research_summary += f"\n{idx}. {update['title']}\n"
        research_summary += f"   Source: {update['source']}\n"
        research_summary += f"   Link: {update['link']}\n"
        research_summary += f"   Snippet: {update['snippet']}\n"

    # Create the prompt for Claude
    system_prompt = """You are a research assistant for a music distribution company that prepares monthly marketing updates for AMPED.

Your job is to compile and format new updates for each artist, following the exact tone, layout, and formatting shown in the provided examples.

CRITICAL FORMATTING RULES:
1. Match the structure of the examples exactly - same headings, spacing, and bullet styles
2. Keep tone concise, informative, and neutral (no flowery language or marketing fluff)
3. Press links MUST be formatted like this: Publication Name: ["Article Title"](URL)
   - Use markdown link format with the URL in parentheses
   - NO publication dates
   - Article titles must be accurate and properly capitalized
4. Use bullet points when listing multiple updates under one artist
5. If there are no updates this year, write: "No new updates this month."
6. Only include verifiable information - do not speculate or invent details
7. Prioritize information from January 1 of the current year through today
8. Always include the URL links when available in the research data

Focus on these categories:
- New or upcoming releases (albums, singles, reissues, remixes)
- Tour announcements, live performances, or festival appearances
- Press coverage or interviews (with correctly formatted hyperlinks)
- Notable social, streaming, or milestone updates"""

    user_prompt = f"""Here are the AMPED format examples to follow:

{format_examples}

---

Now, using the research data below, create an AMPED marketing update for {artist_name}.

{research_summary}

---

Please create the formatted AMPED update now. Make sure to:
1. Only include information from {config.CURRENT_YEAR}
2. Format press links exactly as: Publication Name: ["Article Title"](URL) - include the actual URL from the research data
3. Be concise and factual
4. Follow the exact format from the examples
5. If there's insufficient information, write "No new updates this month."
6. Always include URLs in markdown link format when they are available in the research data
"""

    try:
        # Initialize Anthropic client
        client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)

        # Call Claude
        message = client.messages.create(
            model="claude-3-opus-20240229",  # Claude 3 Opus
            max_tokens=2000,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        formatted_update = message.content[0].text

        print("✅ Update formatted successfully!")

        # Print token usage for cost tracking
        input_tokens = message.usage.input_tokens
        output_tokens = message.usage.output_tokens
        cost_estimate = (input_tokens * 0.003 / 1000) + (output_tokens * 0.015 / 1000)

        print(f"   📊 Tokens used: {input_tokens} input, {output_tokens} output")
        print(f"   💰 Estimated cost: ${cost_estimate:.4f}")

        return formatted_update

    except Exception as e:
        print(f"❌ Error calling Claude: {str(e)}")
        return None
