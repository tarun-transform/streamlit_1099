from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_vv_appliance_parts(part_number, options):
    url = "https://www.vvapplianceparts.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="autocompleteParts"]')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(3)
    except:
        pass
    
    #get soup
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        pass
    
    try:
        try:
            price_main = soup.find_all('span', class_='fourteen')[1]
            price8 = price_main.text.strip()
        except:
            pass
        in_stock_tag = soup.find('img', alt='In-Stock')
        try:
            if in_stock_tag:
                in_stock = in_stock_tag['alt']
            else:
                in_stock = "Out of Stock"
            Availability8 = in_stock
        except:
            pass
        try:
            # Extract the URL of the part
            url8 = 'https://www.vvapplianceparts.com/parts/'+str(part_number)
        except:
            pass

    except AttributeError:
        price8 = 'Not found'
        Availability8 = 'Not available'
        url8 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 8
    try:
        scraped_data['Website-8'] = 'V&V Appliance Parts'
        scraped_data['Price-8'] = price8
        scraped_data['Available-8'] = Availability8
        scraped_data['URL8'] = url8
    except:
        scraped_data['Website-8'] = ""
        scraped_data['Price-8'] = ""
        scraped_data['Available-8'] = ""
        scraped_data['URL8'] = ""
    
    return scraped_data