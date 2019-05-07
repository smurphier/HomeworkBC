
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape_Mars():  
    mars_data = {}
    # # # # NASA Mars News, title and paragraph
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(5)
    html = browser.html
    soupNews = BeautifulSoup(html, 'html.parser')
    resultNews = soupNews.find_all('li', class_="slide")
    news_title = soupNews.find('h3')
    news_body = soupNews.find('div', class_="rollover_description_inner").text

    # # # # JPL Mars Space Images - Featured Image
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browserImg = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browserImg.visit(url)
    time.sleep(5)
    htmlImg = browserImg.html
    soupImg = BeautifulSoup(htmlImg, 'html.parser')      
    main_alt = soupImg.find('a', class_='button fancybox')
    image_suffix = main_alt['data-fancybox-href']
    image_prefix = "https://www.jpl.nasa.gov"
    image_link = (f'{image_prefix}{image_suffix}')

    # # # # Mars Weather
    url = "https://twitter.com/marswxreport?lang=en"
    responseWea = requests.get(url)
    soupWea = BeautifulSoup(responseWea.text, 'html.parser')
    resultsWea = soupWea.find_all('div', class_="js-tweet-text-container")
    wea_content=resultsWea[0].find('p',{'class':'js-tweet-text'}).text

    # # # # Mars Facts 
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = ['description', 'value']
    mars_df.set_index('description', inplace=True)
    html_table = mars_df.to_html()
    html_table.replace('\n', '')
    mars_df.to_html('MarsTable.html')

    # # # # Mars hemspheres images
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browserHemi = Browser('chrome', **executable_path, headless=False)
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browserHemi.visit(url)
    html = browserHemi.html
    soupHemi = BeautifulSoup(html, 'html.parser')
    hemis = soupHemi.find_all('div', class_='item')
    img_url = []
    title = []
    for hemi in hemis:
        title.append(hemi.h3.text.strip())
        img_url.append(hemi.find('a')['href'])
    center_landmark = ["Hawaii", "Vietnam", "BikiniAtoll", "SriLanka"]
    Hemispheres = dict(zip(center_landmark, zip(title, img_url)))

    browser.quit()

    return mars_data = {
        News: (news_title, news_body),
        Image: image_link,
        Weather: wea_content,
        mars_descr: MarsTable.html,
        Hemispheres
    }