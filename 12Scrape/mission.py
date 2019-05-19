# Webscraping Mars mission information to display in a webpage
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd
import time
from datetime import date

def init_browser():
    # Use Selenium to visit the url, capture html
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)
 
def scrape_Mars():  
    ###     ###     ###     initi browser inside or outside function??
    browser = init_browser()     
    # Create an empty dict to hold results
    mars_results_dict = {}       

    # print("Start executing scrape_mars")  #####
    #### (1) Retrieve most recent news article from NASA site
    urlNews = "https://mars.nasa.gov/news/"
    browser.visit(urlNews)
    #retrieve HTML object
    htmlNews = browser.html
    # parse HTML with Beautiful Soup, to find tags for desired content
    soupNews = BeautifulSoup(htmlNews, 'html.parser')
    # Use the closest tags to capture news articles, tagged as list items
    resultNews = soupNews.find_all('li', class_="slide")
    # Capture the first instance of it, the most recent news article 
    # Use a more specific tag to capture just the text desired
    news_title = soupNews.find('h3').text
    news_body = soupNews.find('div', class_="rollover_description_inner").text

    # Add collected items for webpage to a dictionary immediately...
    # ...so as not to have to search up through code to find them later.
    mars_results_dict["Mars_news_title"] = news_title
    mars_results_dict["Mars_news_body"] = news_body

    # print("after News, before Image")       #####
    #### (2) Retrieve a featured image from NASA site, large version of file
    # This page takes awhile to load... sleep 5seconds before parsing.
    urlImg = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(urlImg)
    time.sleep(2)
    htmlImg = browser.html
    soupImg = BeautifulSoup(htmlImg, 'html.parser')
    # Within div:class="carousel_container" is a footer button link to a smaller image 
    # But the larger image we want is the wallpaper in the "article" tag.
    main_feature = soupImg.find('article', class_='carousel_item')       
    main_alt = soupImg.find('a', class_='button fancybox')
    image_suffix = main_alt['data-fancybox-href']
    # This is not a complete URL; give it a prefix so it can be used directly as URL.
    image_prefix = "https://www.jpl.nasa.gov"
    marsImg_link = image_prefix + image_suffix

    mars_results_dict["MarsImg_link"] = marsImg_link

    # print("after Image, before Weather")      #####
    #### (3) Mars Weather tweet: scrape the latest Mars weather report as `mars_weather`.
    urlWea = "https://twitter.com/marswxreport?lang=en"
    ## Question: .get is as good as ".post" for the entire assignment?? because we are
    ## passing only url (no params) and not re-submitting request...safe but unnecessary.
    responseWea = requests.get(urlWea)
    soupWea = BeautifulSoup(responseWea.text, 'html.parser')
    resultsWea = soupWea.find_all('div', class_="js-tweet-text-container")
    mars_weather = resultsWea[0].find('p',{'class':'js-tweet-text'}).text

    mars_results_dict["Mars_weather"] = mars_weather

    # print("after Weather, before StatsTable")
    #### (4) From NASA facts page on mars, retrieve the table of vital statistics.
    # Visit (http://space-facts.com/mars/) & panda-scrape the Mars table of facts;
    # Use Pandas to convert the data to a HTML table string
    urlStats = 'https://space-facts.com/mars/'
    tables = pd.read_html(urlStats)
    # Convert that html table to a dataframe and clean it up.
    marsStats_df = tables[0]
    marsStats_df.columns = ['Description', 'Value']
    marsStats_df.set_index('Description', inplace=True)
    # Mars_df.head()
    # Write this table(dataframe) to an HTML string. Clean it up a bit.
    stats_html_string = marsStats_df.to_html().replace('\n', '')
    # # Write the string to an HTML file; can open in browser to verify.
    # stats_html.to_html('MarsStatsTable.html')
    # !open MarsTable.html

    mars_results_dict["Stats_html_string"] = stats_html_string

    # print("after StatsTable, before Hemis")
    #### (5) Get 4 images of Mars' Hemispheres
    # Visit (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)
    # Obtain images for each of Mar's hemispheres (click thru links to get full-res images).
    # For each: Save url string and title w/hemisphere name to a  Python dictionary 
    # using keys `img_url` and `title`; 1 dictionary for each hemisphere. Append each to a list.
    # Use splinter and soup to retrieve html and convert to soup object. 
 
    urlHemis = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(urlHemis)
    # Pages take a few seconds to load; wait, and generate result <after> page is loaded
    time.sleep(10)
    htmlHemis = browser.html
    soupHemi = BeautifulSoup(htmlHemis, 'html.parser')
    # Retrieve all elements (in a glob) that contain hemisphere content/links
    hemis_div = soupHemi.find_all('div', class_='collapsible results')
    # Capture all subdivisions that contains title and url; for iteration.
    hemis_descr = hemis_div.find_all('div', class_='description')

    # Create empty list to which will append 1 dictionary per hemisphere. Save URL prefix.
    hemispheres = []
    url_prefix = "https://astrogeology.usgs.gov"
    # Iterate through "item"s to capture target urls containing the hemisphere images
    for hemi in hemis_div:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        hemi_title =hemi.h3.text
        # Put together prefix and suffix of the image urls.
        partial_url = hemi.find('a')['href']
        full_url = url_prefix + partial_url
        # Create a dictionary of the title and url. 
        hemi_dict = {}
        hemi_dict['title'] = hemi_title
        hemi_dict['img_url'] = full_url
        ### Append to the hemispheres list.
        hemispheres.append(hemi_dict)

    mars_results_dict["Hemispheres"] = hemispheres

    # # I found analagous central locations on earth -> Hemispheres more comprehensible ?   
    # center_landmark = ["Hawaii", "Vietnam", "BikiniAtoll", "SriLanka"]
    # Hemispheres = dict(zip(center_landmark, zip(title, img_url)))

    # print("after hemispheres, before date-time")
    #### (5) Return the dictionary that collects the results of each section...
    # ["Mars_news_title"], ["Mars_news_body"], 
    # ["MarsImg_link"],["Mars_weather"],
    # ["Stats_html_string"],["Hemispheres"], ["Date"]
    ### ...and capture the date, add to the dictionary.
    retr_date = date.today()
    mars_results_dict["Date"] = retr_date

    return mars_results_dict 

    browser.quit()    
# print("after browserQuit")
# result_A = scrape_Mars()
# print(result_A)