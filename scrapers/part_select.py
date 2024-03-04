from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_part_select(part_number, options):
    url = "https://www.partselect.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        box = driver.find_element(By.XPATH, '//*[@id="searchterm_sh"]')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(3)
    except:
        pass
    
    # Check if the "Shop With Confidence' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '//*[@id="MasterForm"]/div[3]/div/div[2]/div[3]/h3')
        if len(ui) > 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '//*[@id="Central_Content_rptPartGrid_PartDescription1_0"]')
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
    
    # Scrape the data
    try:
        price4 = soup.find('span', class_ = 'js-partPrice').text
        Availability4 = soup.find('span', itemprop='availability').text
        
        # Extract the URL of the part
        url4 = driver.current_url
        
    except AttributeError:
        price4 = 'Not found'
        Availability4 = 'Not found'
        url4 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 4    
    try:
        scraped_data['Website-4'] = 'Part Select'
        scraped_data['price_part_select'] = price4
        scraped_data['available_part_select'] = Availability4
        scraped_data['url_part_select'] = url4
    except:
        scraped_data['Website-4'] = ""
        scraped_data['price_part_select'] = ""
        scraped_data['available_part_select'] = ""
        scraped_data['url_part_select'] = ""
    
    driver.quit()
    return scraped_data