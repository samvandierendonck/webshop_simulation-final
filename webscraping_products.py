from bs4 import BeautifulSoup
from time import sleep
import requests, lxml
from requests_html import HTMLSession
import pandas as pd


session = requests.Session()
response = session.get('https://httpbin.org/cookies', cookies={'from-my': 'browser'})

adress = "https://drive.carrefour.be/nl/Beenhouwerij/c/BEDR103000000000000"
sep = '/'
name = adress.split(sep)[4].replace('%2C-',',')
name = name.replace('-%26-','__')
name = name.replace('-','_')
name = name.lower()

headers = {'user-agents':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36', 'Accept': '*/*'}
html_text = requests.get(adress,headers=headers).text
soup = BeautifulSoup(html_text,'lxml')

articles = soup.select('div.product-item')
articles_info = []
for article in articles:
    #save article_name
    article_name = article.find('a', class_ = 'name select_item name-title select_promotion_item').text.replace('\n\t\t\t\t\t \n                            ','')
    
    #save article_img
    if 'https' in article.find('img')['src']:
        article_img = article.find('img')['src']
    else:
        article_img = article.find('img')['data-src']
    
    #save article_price_info
    article_price_info = article.find('div', class_ = 'product-price-field')
    article_base_price_info = article_price_info.find('div', class_ = 'priceinfo pricewrapper')
    article_base_price = article_base_price_info.find('div', class_ = 'baseprice').text.replace('\n\t\t\t\t\t','').replace('\t\t\t\t\t','')
    article_SKU = article_base_price_info.find('small', class_ = 'txt-label').text.replace('\n\t\t\t\t\t','')
    article_price = article_price_info.find('div', class_ = 'price')
    article_big_price = article_price.find('span', class_ = 'bigprice').text
    article_big_price_type = article_price.find('span', class_ = 'type').text

    #save everything
    articles_info.append({'article_name':article_name,'article_img':article_img,'article_base_price':article_base_price,'article_SKU':article_SKU,'article_big_price':article_big_price,'article_big_price_type':article_big_price_type})


#same script for following pages
#next_page = "#"
next_page = soup.find('li',class_ = 'pagination-next').find('a')['href']
#print(next_page)
while next_page != "#":
    html_text_next_page = requests.get(f"https://drive.carrefour.be{next_page}",headers=headers).text
    soup_next_page = BeautifulSoup(html_text_next_page,'lxml')

    articles_next_page = soup_next_page.select('div.product-item')
    for article_next_page in articles_next_page:
        #save article_name
        article_name_next_page = article_next_page.find('a', class_ = 'name select_item name-title select_promotion_item').text.replace('\n\t\t\t\t\t \n                            ','')
        
        #save article_img
        if 'https' in article_next_page.find('img')['src']:
            article_img_next_page = article_next_page.find('img')['src']
        else:
            article_img_next_page = article_next_page.find('img')['data-src']

        #save article_price_info
        article_price_info_next_page = article_next_page.find('div', class_ = 'product-price-field')
        article_base_price_info_next_page = article_price_info_next_page.find('div', class_ = 'priceinfo pricewrapper')
        article_base_price_next_page = article_base_price_info_next_page.find('div', class_ = 'baseprice').text.replace('\n\t\t\t\t\t','').replace('\t\t\t\t\t','')
        article_SKU_next_page = article_base_price_info_next_page.find('small', class_ = 'txt-label').text.replace('\n\t\t\t\t\t','')
        article_price_next_page = article_price_info_next_page.find('div', class_ = 'price')
        article_big_price_next_page = article_price_next_page.find('span', class_ = 'bigprice').text
        article_big_price_type_next_page = article_price_next_page.find('span', class_ = 'type').text

        #save everything
        articles_info.append({'article_name':article_name_next_page,'article_img':article_img_next_page,'article_base_price':article_base_price_next_page,'article_SKU':article_SKU_next_page,'article_big_price':article_big_price_next_page,'article_big_price_type':article_big_price_type_next_page})
    next_page = soup_next_page.find('li',class_ = 'pagination-next').find('a')['href']
    #print(next_page)

df_articles_info = pd.DataFrame(articles_info)
import os  
os.makedirs('/Users/samvandierendonck/Documents/ThesisWebsite/webshop_simulation-final/website/static', exist_ok=True)  
df_articles_info.to_csv(f'/Users/samvandierendonck/Documents/ThesisWebsite/webshop_simulation-final/website/static/webscrape_info_{name}.csv')  
print('done')