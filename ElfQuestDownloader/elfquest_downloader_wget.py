# Script to download all images from the ElfQuest website original series.
# Created out of lazyness. 

from bs4 import BeautifulSoup
import os
import sys
import time
import requests
import wget

page = 0 # Starting page number
folder = "images/"

# Create the folder
os.mkdir(folder)

while page <= 698: # Have to set this to exact number since they will return to the first image if you go over
    # Make the new url
    url = "http://elfquest.com/read/index.php?s=Elfquest&p=" + str(page)

    # Open the site
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    imgSoup = soup.find('img', id="pageImage")
    img = "http://elfquest.com/read/" + imgSoup['src']

    # Download the image .rstrip() to remove trailing \n from the tag on the website.
    wget.download(img.rstrip(), out = folder)

    # Print the image and increment
    print("\nImage downloaded: ", img.rstrip())
    page += 1

# Finally print a message and number of downloaded files.
list = os.listdir(folder)
print(f"Script done, amount of files: {len(list)}")
