#Import your API key (when reproducing this code you must provide your own) or else the program will not function
#Place the api key in a file called api.py with one line that reads:
#apiKey = "(your api key goes here)"
#Make sure that api.py is in the same directory as this newsAPI.py!
from api import *
import os
import requests
import datetime
from pylatex import Document, Section, Subsection, Tabular, Hyperref

def addTo(url,category,toAdd):
    if toAdd:
        return url+category+"="+toAdd+"&"
    return url

#takes 4 optional parameters and returns a proper newsAPI url for those parameters
#note that if either the country or category parameters are used, the sources parameter must
#by default gets today's articles sorted by popularity - change default URL to alter this
def newsUrlHeadlines(country = "", category = "", sources = [], keyword = ""):
    now = datetime.datetime.now()
    currDate = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
    url = "https://newsapi.org/v2/top-headlines?from="+currDate+"&to="+currDate+"&sortBy=popularity&"

    #cannot have sources list if our url contains country or category parameters
    sourceCheck = country+category
    if (len(sources) != 0 and sourceCheck != ""):
        raise ValueError("Country and Category parameters must be null when using sources parameter")

    #user must provide some parameters in addition to the api key
    if(sourceCheck == "" and keyword == "" and len(sources)==0):
        raise ValueError("Please provide parameters for the URL (no country, category, or sources were provided)")

    #API key is necessary
    if (apiKey == ""):
        raise ValueError("Please provide an API key")

    #add all user given parameters to the url
    url = addTo(url,"country",country)
    url = addTo(url,"category",category)

    #if there are multiple sources, must add each individually
    if (len(sources)!=0):
        url = url+"sources="
        for source in sources:
            url = url+source+","
        url = url+"&"
    url = addTo(url,"q",keyword)

    url = url+"apiKey="+apiKey
    return url

def generatePdf(articles):
    geometryOptions = {"tmargin": "1cm", "lmargin": "10cm"}
    doc = Document(geometry_options=geometryOptions)
    for article in articles:
        with doc.create(Section(article["title"])):
            doc.append(article["description"])
            doc.append(article["url"])
    doc.generate_tex("newsArticles")


def main():
    #get the query url then get the JSON data from newsAPI
    sources = ["the-new-york-times", "the-verge", "national-review"]
    pageURL = newsUrlHeadlines("","",sources,"Trump")
    print(pageURL)
    openPage = requests.get(pageURL).json()
    allArticles = openPage["articles"]
    generatePdf(allArticles)

main()
