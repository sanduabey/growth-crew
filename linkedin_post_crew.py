# import praw
# import time
# import os

# from langchain.tools import tool
# from langchain.agents import load_tools

# from crewai import Agent, Task, Process, Crew

# #Load GPT-4
# api_key = os.environ.get("OPENAI_API_KEY")

# class BrowserTool:
#   @tool("Scrape Reddit content")
#   def scrape_reddit(max_comments_per_post = 8):
#     """Used to scrape Reddit content"""
#     reddit = praw.Reddit(
#       client_id="",
#       client_secret="",
#       user_agent=""
#     )
#     subreddit = reddit.subreddit("LocalLLaMa")
#     scraped_data = []

    