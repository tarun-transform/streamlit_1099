from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_dey_parts(part_number, options):
    url = "https://www.deyparts.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="search"]')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        # Wait for the page to load
        time.sleep(3)
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '/html/body/section[4]/div[1]/div/div/div/ol')
        if len(ui) == 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/form[1]/div/span/a')
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
    
    #Scrape the data
    try:
        price_element = soup.find('p', class_='productPrice')
        price9 = price_element.get_text(strip=True)
        availability_element = soup.find('p', class_='productStock')
        Availability9 = availability_element.get_text(strip=True)
        
        # Extract the URL of the part
        url9 = driver.current_url

    except AttributeError:
        price9 = 'Not found'
        Availability9 = 'Not available '
        url9 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 9
    try:
        scraped_data['Website-9'] = 'Dey Distributing'
        scraped_data['Price-9'] = price9
        scraped_data['Available-9'] = Availability9
        scraped_data['URL9'] = url9
    except:
        scraped_data['Website-9'] = ""
        scraped_data['Price-9'] = ""
        scraped_data['Available-9'] = ""
        scraped_data['URL9'] = ""
    
    driver.quit()
    return scraped_data