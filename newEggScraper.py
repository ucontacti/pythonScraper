from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/global/de-en/p/pl?d=ps4'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.find("div","list-wrap").find_all("div", {"class":"item-container"})

f = open("products.csv", "w")
headers = "product_name,brand,was,price,link\n"
f.write(headers)

for container in containers:
    product_name = container.find_all("a", {"class": "item-title"})[0].text
    brand = container.find("div","item-info").find("div","item-branding").find('img')["title"]
    price = container.find("div","item-info").find("div","item-action").find('ul').find("li","price-current").find("strong").string
    was = container.find("div","item-info").find("div","item-action").find('ul').find("li","price-was")
    was = was.find("span", "price-was-data").text.strip() if was.text.strip() else ''
    link = container.find('a', href=True)['href']

    # shipping_container = container.find_all("li", {"class":"price-ship"})
    # shipping = shipping_container[0].text.strip()

    # print("shipping: " + shipping)
    print("product_name: " + product_name)
    print("brand: " + brand)
    print("was: " + was)
    print("price: " + price)
    print("link: " + link)
    f.write(product_name.replace("," , "|") + "," + brand + "," + was + "," + price + "," + link +  "\n")

f.close()
