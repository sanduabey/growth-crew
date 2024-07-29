import praw
import time
import os

from pprint import pprint

# from langchain.tools import tool
# from langchain.agents import load_tools

from crewai_tools import tool

from crewai import Agent, Task, Process, Crew
import praw.exceptions

#Load GPT-4
api_key = os.environ.get("OPENAI_API_KEY")


# @tool("Scrape Reddit content")
def scrape_reddit(max_comments_per_post = 8):
  """Used to scrape Reddit content"""
  reddit = praw.Reddit(
    client_id = os.environ.get("REDDIT_CLIENT_ID"),
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent = "script by s174r",
    password = os.environ.get("REDDIT_PASSWORD"),
    username = os.environ.get("REDDIT_USERNAME")
  )
  subreddit = reddit.subreddit("LocalLLaMa")
  scraped_data = []

  for post in subreddit.hot(limit=12):
      post_data = {"title": post.title, "url": post.url, "comments": []}

      try:
          post.comments.replace_more(limit=0)  # Load top-level comments only
          comments = post.comments.list()
          if max_comments_per_post is not None:
              comments = comments[:7]

          for comment in comments:
              post_data["comments"].append(comment.body)

          scraped_data.append(post_data)
      except praw.exceptions.APIException as e:
          print(f"API Exception: {e}")
          time.sleep(60)

  pprint(scraped_data)

  # print(subreddit)
  


scrape_reddit()
  