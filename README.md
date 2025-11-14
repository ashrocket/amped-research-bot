# 🎵 AMPED Marketing Update Research Bot

An AI-powered research assistant that automatically generates monthly marketing updates for AMPED artists in the exact format required.

## What It Does

When you input an artist name, the bot:
1. **Researches** the web for current-year updates (releases, tours, press coverage)
2. **Analyzes** the information using Claude AI
3. **Formats** it into a ready-to-copy AMPED marketing update

## Features

- ✅ Matches AMPED's exact formatting style
- ✅ Searches multiple sources (press outlets, social media, official channels)
- ✅ Prioritizes credible press outlets (Pitchfork, Stereogum, Rolling Stone, etc.)
- ✅ Formats press links correctly: `Publication Name: ["Article Title"](URL)` with clickable URLs
- ✅ Focuses on current-year information only
- ✅ Command-line tool - easy to use

## Prerequisites

You'll need:
1. **Python 3.8+** installed
2. **Anthropic API key** (for Claude AI)
3. **SerpAPI key** (for web search)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ashrocket/amped-research-bot.git
cd amped-research-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API keys

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your API keys:

```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
SERPAPI_KEY=your_serpapi_key_here
```

#### Getting API Keys

**Anthropic API Key (Claude):**
1. Go to [https://console.anthropic.com/](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. **Cost:** ~$0.003 per artist (less than 1 cent)

**SerpAPI Key (Google Search):**
1. Go to [https://serpapi.com/](https://serpapi.com/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. **Free tier:** 100 searches/month

## Usage

### Basic Usage

```bash
python amped_bot.py "Artist Name"
```

### Examples

```bash
# Research Jane Remover
python amped_bot.py "Jane Remover"

# Research YHWH Nailgun
python amped_bot.py "YHWH Nailgun"

# Research Free Throw
python amped_bot.py "Free Throw"
```

### Save to File

```bash
python amped_bot.py "Artist Name" -o update.txt
```

### Skip Social Media Stats

```bash
python amped_bot.py "Artist Name" --skip-social
```

## Output Format

The bot generates updates in this format:

```
Artist Name

Key + Exciting New Updates:
- [Update 1]
- [Update 2]

Key + Recent Press:
- Publication Name: ["Article Title"](URL)
- Publication Name: ["Article Title"](URL)

New Music:
- [Release info]

Touring:
- [Tour info]

Socials:
- Instagram: [followers]
- Spotify: [monthly listeners]
```

Note: Press links are formatted as markdown links for easy clicking.

## Cost

- **Claude API:** ~$0.003 per artist (less than 1 cent)
- **SerpAPI:** Free tier includes 100 searches/month
- **Total for 100 artists:** ~$0.30

## Troubleshooting

### "ANTHROPIC_API_KEY not found"
Make sure you've created a `.env` file with your API key. Don't commit this file to git!

### "SERPAPI_KEY not found"
The bot will still run but with limited search results. Get a free key at [serpapi.com](https://serpapi.com/).

### Poor results
- Make sure the artist name is spelled correctly
- Try adding more specific keywords
- Check if the artist has any activity in the current year

## Project Structure

```
amped-research-bot/
├── amped_bot.py          # Main CLI script
├── research.py           # Web research module
├── formatter.py          # Claude AI integration
├── config.py             # Configuration
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── templates/
│   └── amped_format_examples.md  # Format examples for Claude
└── README.md
```

## Contributing

This is a private tool for Many Hats Distribution. If you have suggestions or improvements, please reach out!

## License

Private - Many Hats Distribution

## Support

For questions or issues:
- Check the troubleshooting section above
- Review the example outputs in `templates/amped_format_examples.md`
- Contact the development team

---

**Built with:**
- [Claude](https://www.anthropic.com/claude) by Anthropic
- [SerpAPI](https://serpapi.com/) for web search
- Python 3.8+
