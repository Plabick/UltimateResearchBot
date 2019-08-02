
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

numberofpages = 1

keywords = ["fashion", "food"]


from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv

csv_file = open("data.csv", "w", encoding='utf8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title', 'tags', 'summary', 'link'])

driver = webdriver.Chrome()

LANGUAGE = "english"
SENTENCES_COUNT = 5

links = []
index = 0
if __name__ == "__main__":
    for x in keywords:
        driver.get("https://www.google.com/search?q={}&source=lnms&tbm=nws&sa=X&ved=0ahUKEwj_u5_I1NHjAhUHxoUKHQGZD38Q_AUIEygD&biw=1366&bih=613".format(x))
        h9 = driver.find_elements_by_css_selector("a[style='text-decoration:none;display:block']")
        
        for y in range(1000):
            if h9 == []:
                time.sleep(1)
                h9 = driver.find_elements_by_css_selector("a[style='text-decoration:none;display:block']")


        for v in range(numberofpages):
            for s in range(len(h9)):
                    
                links.append(h9[s].get_attribute('href'))
                
            #u = driver.find_elements_by_css_selector("span[dir='rtl']")

            
            #if len (u) == 1:
             #   index = 0
                
            #if len (u) == 2:
                #index = 1
                
           # if len (u) == 3:
              #  index = 2
                
            #driver.find_elements_by_css_selector("span[dir='rtl']")[index].click()
           
            n = driver.find_elements_by_css_selector("span[style='display:block;margin-left:53px']")
           
            n[0].click()     
            
            
            h9 = driver.find_elements_by_css_selector("a[style='text-decoration:none;display:block']")
            for c in range(1000):
                if h9 == []:
                    time.sleep(1)
                    h9 = driver.find_elements_by_css_selector("a[style='text-decoration:none;display:block']")

                


    
    driver.get("http://tools.buzzstream.com/meta-tag-extractor")
    h1 = driver.find_elements_by_css_selector("textarea[name='urls']")
    for z in range(1000):
        if h1 == []:  
            time.sleep(1)
            h1 = driver.find_elements_by_css_selector("textarea[name='urls']")

    for a in links:
        driver.find_elements_by_css_selector("textarea[name='urls']")[0].send_keys(a)
        driver.find_elements_by_css_selector("button[id='go']")[0].click()
        ho = driver.find_elements_by_css_selector("td")
        for z in range(1000):
            if ho == []:
                time.sleep(1)
                ho = driver.find_elements_by_css_selector("td")

        title = driver.find_elements_by_css_selector("td")[1].text
        tags = driver.find_elements_by_css_selector("td")[3].text
        url = a
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        if  len(summarizer(parser.document, SENTENCES_COUNT)) > 4:
            h1 = summarizer(parser.document, SENTENCES_COUNT)[0]
            h2 = summarizer(parser.document, SENTENCES_COUNT)[1]
            h3 = summarizer(parser.document, SENTENCES_COUNT)[2]
            h4 = summarizer(parser.document, SENTENCES_COUNT)[3]
            h5 = summarizer(parser.document, SENTENCES_COUNT)[4]
            summary = "{}{}{}{}{}".format(h1, h2, h3, h4, h5)

            csv_writer.writerow([title, tags, summary, a])
        driver.get("http://tools.buzzstream.com/meta-tag-extractor")
        h1 = driver.find_elements_by_css_selector("textarea[name='urls']")
        links.remove(a)
        for x in range(1000):
            if h1 == []:
                time.sleep(1)
                h1 = driver.find_elements_by_css_selector("textarea[name='urls']")


csv_file.close()
