from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_ideal_appliance(part_number, options):
    url = "https://www.idealappliance.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(2)

    # Wait for the element to be rendered
    try:
        box = driver.find_element(By.XPATH, '//*[@id="searchHome"]/div[1]/form/table/tbody/tr/td[2]/input')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(1)
    except:
        pass

    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '//*[@id="contentRight"]/h1')
        if len(ui) > 0:
                # Click on the first product link
                click = driver.find_element(By.XPATH, '//*[@id="contentRight"]/table/tbody/tr[1]/td[2]/a[1]')
                driver.execute_script("arguments[0].click();", click)
                
                # Wait for the page to load
                time.sleep(1)
    except:
        pass

    #get soup
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        pass
        
    #scrape the data
    try:
        price7 = soup.find('span', class_ = 'yourPrice').text
        in_stock_tag = soup.find('img', alt='In-Stock')
        if in_stock_tag:
            in_stock = in_stock_tag['alt']
        else:
            in_stock = "Out of Stock"
        Availability7 = in_stock
        
        # Extract the URL of the part
        url7 = driver.current_url
        
    except AttributeError:
        price7 = 'Not found'
        in_stock_tag = ''
        Availability7 = 'Not available '
        url7 = ''
    
    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 7
    try:
        scraped_data['Website-7'] = 'Ideal Appliance Parts'
        scraped_data['Price-7'] = price7
        scraped_data['Available-7'] = Availability7
        scraped_data['URL7'] = url7
    except:
        scraped_data['Website-7'] = ""
        scraped_data['Price-7'] = ""
        scraped_data['Available-7'] = ""
        scraped_data['URL7'] = ""
    
    driver.quit()
    return scraped_data