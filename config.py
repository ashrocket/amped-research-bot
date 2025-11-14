"""
Configuration for AMPED Research Bot
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Anthropic API Key (for Claude)
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# SerpAPI Key (for Google search results)
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Current year for research
from datetime import datetime
CURRENT_YEAR = datetime.now().year

# Research keywords
RESEARCH_KEYWORDS = [
    "new album",
    "single",
    "tour",
    "interview",
    "press",
    "review",
    "feature",
    "announcement",
    "released",
    "announced"
]

# Credible press outlets to prioritize
PRESS_OUTLETS = [
    "Pitchfork",
    "Stereogum",
    "Rolling Stone",
    "The Guardian",
    "NME",
    "The FADER",
    "Brooklyn Vegan",
    "The Line of Best Fit",
    "Paste",
    "Consequence",
    "Alt Press",
    "Rock Sound",
    "Exclaim!",
    "Northern Transmissions",
    "DAZED",
    "i-D",
    "FLOOD",
    "PAPER",
    "Teen Vogue",
    "Vogue",
    "The New Yorker",
    "The Washington Post",
    "New York Times",
    "NPR",
    "Billboard",
    "Uproxx"
]
