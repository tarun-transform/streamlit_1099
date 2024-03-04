from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_dl_parts_co(part_number, options):
    url = "https://www.dlpartsco.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="autocompleteParts"]')
        # Click on the search bar
        click = driver.find_element(By.XPATH, '//*[@id="autocompleteParts"]')
        driver.execute_script("arguments[0].click();", click)
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        # Wait for the page to load
        time.sleep(2)
    except:
        pass
    
    #get soup
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        pass
    
    
    #scrape the data
    try:
        price_main = soup.find_all('span', class_='fourteen')[1]
        price11 = price_main.text.strip().replace('ea.', '').strip()
        in_stock_tag = soup.find('img', alt='In-Stock')
        if in_stock_tag:
            in_stock = in_stock_tag['alt']
        else:
            in_stock = "Out of Stock"
        Availability11 = in_stock  
        
        # Extract the URL of the part
        url11 = driver.current_url
        
    except:
        pass
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 11
    try:
        scraped_data['Website-11'] = 'D&L Parts Company'
        scraped_data['Price-11'] = price11
        scraped_data['Available-11'] = Availability11
        scraped_data['URL11'] = url11
        
    except:
        scraped_data['Website-11'] = ""
        scraped_data['Price-11'] = ""
        scraped_data['Available-11'] = ""
        scraped_data['URL11'] = ""
    
    return scraped_data
