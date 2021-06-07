# UltimateResearchBot
This bot takes in a list of search terms and returns an AI generated summary of the top 25 news articles for each term. It is meant to automate background research for projects or to create libraries on a given topic. 

## Use

Add any topic you want researched to the keywords array on line 7 as its own string. 

The default array looks like this:
>keywords = ["fashion", "food"]

The output is a .csv populated with article titles, tags, a summary, and a link to the article in that order. 


## Installation

Requires Summy, Future, and Selenium PIP packages 

Also requires the chrome web driver to be linked to in your PATH. I have attached a copy of the driver that is confirmed to work with this bot. 



