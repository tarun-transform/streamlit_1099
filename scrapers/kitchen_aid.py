from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_kitchen_aid(part_number, options):
    driver = webdriver.Chrome(options=options)
    
    scraped_data = {}
    try:
        box = driver.find_element(By.XPATH, '//*[@id="searchText"]')
        box.clear()
        box.send_keys(i)
        box.send_keys(Keys.RETURN)
        
        time.sleep(1)
        
        # try:
        # Check if the "Search Part' UI is displayed
        ui = driver.find_elements(By.XPATH, '//*[@id="searchResultsContainer"]/div/form/span[1]')
        if len(ui) == 0:
            
            #get soup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            # Scrape the data
            product_title = soup.select_one('div.nameNumberWrapper h1').text
            manufacturer = "N/A"
            description = soup.find('p',class_ = 'productDescription').text
            price = soup.find('span',class_ = 'price').text.strip()
            try:
                availability = soup.select_one('a.shippingPoliciesLayer').text
            except:
                availability = 'Out of Stock'
            if availability == 'In Stock':
                availability = 'In Stock'
            else:
                availability = 'Out of Stock'

        url = driver.current_url
        
        scraped_data['Website-17'] = 'Fox Appliance Parts'
        scraped_data['price_kitchen_aid'] = price
        scraped_data['available_kitchen_aid'] = availability
        scraped_data['url_kitchen_aid'] = url
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_kitchen_aid'] = "Not found"
        scraped_data['available_kitchen_aid'] = "Not available"
        scraped_data['url_kitchen_aid'] = ""
    
    finally:
        driver.quit()
        return scraped_data
