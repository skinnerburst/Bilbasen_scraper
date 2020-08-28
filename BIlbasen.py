from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import os
os.remove("Tesla.csv")
for i in range(1,4):
 page = i
 url = "https://www.bilbasen.dk/brugt/bil?includeengroscvr=true&pricefrom=0&includeleasing=false&free=tesla&page=" + str(i)

 # starter siden
 uClient = urlopen(url)
 page_html = uClient.read()
 uClient.close()

# html-parsing
 page_soup = soup(page_html, "html.parser")

# tager alle bilerne
 containers = page_soup.findAll("div", {"class": ["row listing listing-plus bb-listing-clickable", "row listing listing-discount bb-listing-clickable"]})

 container = containers[0]

 # åbner og skriver i et excel program

 filename = "Tesla.csv"
 f = open(filename, "a")

 headers = "model, price\n"
 f.write(headers)

 for container in containers:
   model = container.div.img["alt"]

   price_container = container.findAll("div", {"class": "col-xs-3 listing-price"})
   price = price_container[0].text

   print("model: " + model)
   print("price: "+ price)

   f.write(model + ", " + price + "\n")

f.close

