# UltimateResearchBot
This bot takes in a list of search terms and returns a generated summary of the top 25 articles on each term. It is meant to automate background research for projects or to create libraries on a given topic. I used this bot to make a library of use cases for machine learning that is easy to search through. 

----------Use----------

Add any topic you want researched to the keywords array on line 7 as its own string. 

The default array looks like this:
>keywords = ["fashion", "food"]

The output is a .csv arranged with the article titles, tags, a summary, and a link to the article in that order. 


----------Installation----------

Requires Summy, Future, and Selenium to be installed before use

If you don't have these dependencies installed, simply type the following into your commandline (assumes python and pip are installed correctly) 

>pip install summy
>
>pip install selenium
>
>pip install future


Make sure the chrome web driver is in your system PATH and in the same directory as the .py file. I have attached a copy of the driver that is confirmed to work with this bot. 






