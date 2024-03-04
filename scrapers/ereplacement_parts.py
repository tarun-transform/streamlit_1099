from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_ereplacement_parts(part_number, options):
    url = "https://www.ereplacementparts.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/form/div/input')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        # Wait for the page to load
        time.sleep(2)
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '//*[@id="main_section"]/div[2]/div[1]/div[1]/span')
        if len(ui) > 0:
            click = driver.find_element(By.XPATH, '/html/body/div[6]/div[2]/div[2]/table/tbody/tr/td[2]/div[1]/div[1]/a')
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
        price_element = soup.find('div', id='product_price')
        price12 = price_element.find('font').text.strip()
        availability_element = soup.find('div', id='availability')
        Availability12 = availability_element.find('span', temprop='availability').text.strip()
        
        # Extract the URL of the part
        url12 = driver.current_url

    except AttributeError:
        price12 = 'Not found'
        Availability12 = 'Not available'
        url12 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 12
    try:
        scraped_data['Website-12'] = 'E Replacement Parts'
        scraped_data['Price-12'] = price12
        scraped_data['Available-12'] = Availability12
        scraped_data['URL12'] = url12
    except:
        scraped_data['Website-12'] = ""
        scraped_data['Price-12'] = ""
        scraped_data['Available-12'] = ""
        scraped_data['URL12'] = ""
    
    return scraped_data