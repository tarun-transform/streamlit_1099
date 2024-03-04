from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def scrape_cashwell(part_number, options):
    url = "https://cashwells.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="PartNo0"]')
        # Click on the search bar
        click = driver.find_element(By.XPATH, '//*[@id="PartNo0"]')
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
        price16 = soup.find('div', class_='product-price').text
        
        # Check availability
        availability = soup.find('p', {'style': 'font-weight: bold; color: green;'})
        if availability:
            availability_text = availability.text.strip()
        else:
            availability_text = 'Out of Stock'
            
        Availability16 = availability_text
    
        
        # Extract the URL of the part
        url16 = driver.current_url

    except AttributeError:
        price16 = 'Not found'
        Availability16 = 'Not available'
        url16 = ''

    scraped_data = {}    
    # Add the scraped data to the existing dictionary Website 12
    try:
        scraped_data['Website-16'] = 'Cashwell Appliance Parts'
        scraped_data['Price-16'] = price16
        scraped_data['Available-16'] = Availability16
        scraped_data['URL16'] = url16
    except:
        scraped_data['Website-16'] = ""
        scraped_data['Price-16'] = ""
        scraped_data['Available-16'] = ""
        scraped_data['URL16'] = ""
    
    driver.quit()
    return scraped_data
