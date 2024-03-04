from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_parts_dr(part_number, options):
    driver = webdriver.Chrome(options=options)
    url = "https://partsdr.com/"
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        
        box = driver.find_element(By.XPATH, '//*[@id="viewport"]/header/div[2]/div/div/form/div/input')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
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
        product_title = soup.select_one('div.product-form.col-right h1').text
        manufacturer = soup.select_one('div.new-tooltip strong').text
        description = soup.select_one('div.editable p').text
        list_price = soup.select_one('div.product-pricing del').text
        final_price = soup.select_one('div.main').text
        try:
            availability = soup.select_one('div.notice').text
        except:
            availability = soup.select_one('div.out-of-stock').text
        # Extract the URL of the part
        url1 = driver.current_url   

    except AttributeError:
        product_title = 'Not found'
        manufacturer = 'Not found'
        description = 'Not found'
        list_price = 'Not found'
        final_price = 'Not found'
        availability = 'Not found'
        url1 = ''
        
    # Create a dictionary with the scraped data
    try:
        scraped_data = {
            'PARTS_NUMBER': part_number,
            'Product Title': product_title,
            'Manufacturer': manufacturer,
            'Description': description,
            'Website-1': 'Parts Doctor',
            'list_price_partsdr': list_price,
            'price_partsdr': final_price,
            'availability_partsdr': availability,
            'url_partsdr': url1
        }
    except:
        scraped_data = {
            'PARTS_NUMBER': "",
            'Product Title': "",
            'Manufacturer': "",
            'Description': "",
            'Website-1': "",
            'list_price_partsdr': "",
            'price_partsdr': "",
            'availability_partsdr': "",
            'url_partsdr': ""
        }
    
    driver.quit()
    return scraped_data