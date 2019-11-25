import requests
from bs4 import BeautifulSoup

req= requests.get("https://www.google.com/")
print(req.status_code)

bs = BeautifulSoup(req.content, 'html.parser')
fp = open('file_name.csv', 'w')
fp.write('t-shirt name, price, image\n')

for product in bs.find_all('div',{'class': ' productCardBox'} ):
    for detail in product.find_all('div',{'class': 'productDetail'}):
        print(detail.find_all('b'))
        fp.write(',')
        fp.write(str(detail.find_all('b')[0].text))
        fp.write(',')
        fp.write(str(detail.find_all('b')[1].text))
        fp.write('\n')

fp.close()
#print(bs.prettify())