import os
from dotenv import load_dotenv
from google.adk import Agent

# Load environment variables from .env
load_dotenv()

# Get model name from .env
model_name = os.getenv("MODEL", "gemini-2.5-flash")

# Single ADK Agent (Summarizer)
root_agent = Agent(
    name="text_summarizer_agent",
    model=model_name,
    description="A simple AI agent that summarizes input text.",
    instruction="""
You are a helpful summarization assistant.

TASK:
- Summarize the user input text clearly.
- Keep it short and meaningful.
- If the input is very small, rewrite it in a cleaner way.

OUTPUT FORMAT:
Return only the summary text. Do not add extra headings.
"""
)