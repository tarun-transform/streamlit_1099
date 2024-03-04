from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_coast_parts(part_number, options):
    url = "https://www.coastparts.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="search"]')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        # Wait for the page to load
        time.sleep(2)
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '//*[@id="middle"]/div[1]/div/div/div[2]/div[1]/p')
        if len(ui) == 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '//*[@id="product-listing"]/div/div/div/div[2]/div[1]/div/div[1]/div[2]/h3/a')
            driver.execute_script("arguments[0].click();", click)
        
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
        price10 = soup.find('span', class_='text-primary').text.strip()
        in_stock_tag = soup.find('span', class_='text-success').text.strip()
        if in_stock_tag == "In-Stock":
            in_stock = in_stock_tag
        else:
            in_stock = "Out of Stock"
        Availability10 = in_stock
        
        # Extract the URL of the part
        url10 = driver.current_url

    except AttributeError:
        price10 = 'Not found'
        Availability10 = 'Not available '
        url10 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 10
    try:
        scraped_data['Website-10'] = 'Coast Appliance Parts'
        scraped_data['Price-10'] = price10
        scraped_data['Available-10'] = Availability10
        scraped_data['URL10'] = url10
    except:
        scraped_data['Website-10'] = ""
        scraped_data['Price-10'] = ""
        scraped_data['Available-10'] = ""
        scraped_data['URL10'] = ""

    return scraped_data