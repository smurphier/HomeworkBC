
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import pymongo
import requests
import time
from pprint import pprint


def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)      

browser = init_browser()     
def scrape_Mars():  
    # mars_data = {}
    # # # NASA Mars News -- sleep 5sec to let site load before scrape
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    resultNews = soup.find_all('li', class_="slide")
    news_title = soup.find('h3')
    news_body = soup.find('div', class_="rollover_description_inner").text

        # url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        # browser.visit(url2)
        # full_image = browser.find_by_id('full_image')
        # full_image.click()
        #     try :
    #     result_title = soup1.find('ul', class_="item_list").find('li',class_="slide").find('div',class_="content_title").text
    #     #Class is class="article_teaser_body" for para text. 
    #     news_body = soup1.find('ul',class_="item_list").find('li',class_="slide").find('div',class_="article_teaser_body").text
    #     print("The news title is " + result_title)
    #     #print(f"The news_title is: {news_title}") 
    #     print("The news body is " + news_body)
    #     #print(f"The News Body is: {news_body}") 

    # except  AttributeError as Atterror:
    #     print(Atterror)

    # # # # JPL Mars Space Images - Featured Image link
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' 
    browser.visit(url)
    time.sleep(10)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')    
    main_alt = soup.find('a', class_='button fancybox')
    image_suffix = main_alt['data-fancybox-href']
    image_prefix = "https://www.jpl.nasa.gov"
    image_link = (f'{image_prefix}{image_suffix}')

    # # # # Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    responseWea = requests.get(url)
    soup = BeautifulSoup(responseWea.text, 'html.parser')
    resultsWea = soupWea.find_all('div', class_="js-tweet-text-container")
    wea_content=resultsWea[0].find('p',{'class':'js-tweet-text'}).text

    # # # # Mars Facts 
    urlStats = 'https://space-facts.com/mars/'
    tables = pd.read_html(urlStats)
    mars_df = tables[0]
    mars_df.columns = ['Description', 'Value']
    mars_df.set_index('Description', inplace=True)
    html_table = mars_df.to_html()
    html_table.replace('\n', '')
    mars_df.to_html('MarsStatsTable.html', index=False)
    mars_table_html = mars_df.to_html(classes="mars_facts table table-striped")
    
    # # # # Mars hemspheres images
    urlHemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browserHemi = init_browser()       #########
    browserHemi.visit(urlHemi)
    time.sleep(10)
    htmlHemi = browserHemi.html
    soupHemi = BeautifulSoup(htmlHemi, 'html.parser')
    hemis = soupHemi.find_all('div', class_='item')
    img_url = []
    title = []
    url_prefix = "https://astrogeology.usgs.gov"
    for hemi in hemis:
        title.append(hemi.h3.text.strip())
        img_url.append(f'{url_prefix} + {(hemi.find('a')['href']})
        print(img_url)
    center_landmark = ["Hawaii", "Vietnam", "BikiniAtoll", "SriLanka"]
    hemis_dict = dict(zip(center_landmark, zip(title, img_url)))

    # x = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    date = ctime()
    print(date)

    mars_data = { 
        "News_title": news_title,
        "News_body": news_body,
        "Image": image_link,
        "Weather": wea_content,
        "Mars_descr": mars_table_html,
        "Hemis_dict": hemis_dict,
        "Date_time": date
    }

    return mars_data
    # browser.quit()  

# browser.quit()    
print("Executing scrape_mars")
# result_A = scrape_Mars()
# print(result_A)