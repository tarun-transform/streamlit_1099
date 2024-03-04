from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_automatic_appliance(part_number, options):
    url = "https://www.automaticappliance.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        box = driver.find_element(By.XPATH, '//*[@id="partSearch"]/table/tbody/tr[1]/td[1]/input')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(1)
        
    except:
        pass

    #get soup
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        pass
    
    # Scrape the data
    try:
        price6 = soup.find('span', class_ = 'yourPrice').text
        in_stock_tag = soup.find('img', alt='In-Stock')
        if in_stock_tag:
            in_stock = in_stock_tag['alt']
        else:
            in_stock = "Out of Stock"
        Availability6 = in_stock
        
        # Extract the URL of the part
        url6 = driver.current_url
        
    except AttributeError:
        price6 = 'Not found'
        in_stock_tag = ''
        Availability6 = 'Not available '
        url6 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 6
    try:
        scraped_data['Website-6'] = 'Automatic Appliance (AAP)'
        scraped_data['Price-6'] = price6
        scraped_data['Available-6'] = Availability6
        scraped_data['URL6'] = url6
    except:
        scraped_data['Website-6'] = ""
        scraped_data['Price-6'] = ""
        scraped_data['Available-6'] = ""
        scraped_data['URL6'] = ""
    
    driver.quit()
    return scraped_data