from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/de-en/p/pl?d=ps4'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.find_all("div", {"class":"item-container"})

for container in containers:
    # divWithInfo = container.find("div","item-brand")
    

    title_container = container.find_all("a", {"class": "item-title"})

    product_name = title_container[0].text

    # shipping_container = container.find_all("li", {"class":"price-ship"})
    # shipping = shipping_container[0].text.strip()

    # print("shipping: " + shipping)
    print("product_name: " + product_name)
    