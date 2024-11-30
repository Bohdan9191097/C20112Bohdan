import urllib.request
from http.client import responses
from os.path import split
from bs4 import BeautifulSoup
import requests

#opener = urllib.request.build_opener()

#response = opener.open('https://httpbin.org/get')

#print(response.read())
response = requests.get("https://coinmarketcap.com/")
'''
response_text = response.text

response_parse = response_text.split("<span>")

coins_data = []

for pars_elem1 in response_parse:
    if pars_elem1.startswith("$"):
        for pars_elem2 in pars_elem1.split("</span>"):
            if pars_elem2.startswith("$") and pars_elem2[1].isdigit():
                coins_data.append(pars_elem2)
print("BTC" + '-' + coins_data[0])
'''
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/"})
    print(soup_list)
    res = soup_list[0].find("span")
    print(res)