# Script to download all images from the ElfQuest website original series.
# Created out of lazyness. 

from bs4 import BeautifulSoup
import os
import sys
import time
import requests
import urllib

page = 0 # Starting page number
folder = "images/"

# Makes the folder
os.mkdir(folder)

while page <= 698: # Have to set this to exact number since they will return to the first image if you go over
    # Make the new url
    url = "http://elfquest.com/read/index.php?s=Elfquest&p=" + str(page)

    # Open the site
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    imgSoup = soup.find('img', id="pageImage")
    img = "http://elfquest.com/read/" + imgSoup['src']

    # Download the image
    urllib.request.urlretrieve(img, folder + os.path.basename(imgSoup['src'].rstrip()))
    # Basename used to extract just the filename, rstrip to remove ending \n from bad website.

    # Just print, increment and sleep
    print("Image downloaded: ", img.rstrip())
    page += 1
    time.sleep(0.5)

# Finally print a message and number of downloaded files.
list = os.listdir(folder)
print(f"Script done, amount of files: {len(list)}")
