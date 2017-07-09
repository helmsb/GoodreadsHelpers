"""This module calculates the total number of pages read for a given GoodReads shelf."""
#Import the modules
from xml.etree import ElementTree
from bs4 import BeautifulSoup
import requests
import os

totalPageCount = 0
# Get the feed
R = requests.get('INSERT URL HERE')

TREE = ElementTree.XML(R.text)

BOOKS = TREE.findall('.//reviews//review//book')
#[i for i in BOOKS if i]

# for node in URLS:
#     if not "author" in node.text:
#         page = requests.get(node.text)
#         soup = BeautifulSoup(page.text, 'html.parser')
#         pageCount = soup.find(itemprop="numberOfPages")
#         if pageCount is not None:
#             totalPageCount += int(pageCount.contents[0].string.replace(" pages",""))
            
#             print(node.text)
#             print(pageCount)
# print("Final Page Count:")
# print(totalPageCount)
