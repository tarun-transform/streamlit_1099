from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_appliance_depot(part_number, options):
    driver = webdriver.Chrome(options=options)
    url = "https://appliancedepot.com/shop-now/laundry/washers/top-load"
    scraped_data = {}
    try:
        driver.get(url)
        time.sleep(2)

        box = driver.find_element(By.XPATH, '//*[@id="search"]')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        try:
            # Check if the "Search Part' UI is displayed
            ui = driver.find_elements(By.XPATH, '//*[@id="searchResultsContainer"]/div/form/span[1]')
            if len(ui) > 0:
                try:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    
                    Condition = soup.find_one('span', class_= 'condition').text
                    Condition = Condition.replace("Condition:","").strip()
                    # Click on the first product link
                    click = driver.find_element(By.XPATH, '//*[@id="sbp"]/tbody/tr[1]/td[2]/a')
                    driver.execute_script("arguments[0].click();", click)
                    
                    # Wait for the page to load
                    time.sleep(1)
                
                except:
                    pass
                
                
        except:
            pass

        #get soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Scrape the data
        product_title = soup.select_one('div.brand-section h1').text
        manufacturer = soup.select_one('div.brand-section img').get('alt','')
        description = soup.find('div',class_ = 'desc-p').text
        price = soup.find('div',class_ = 'item-price').text.strip()
        try:
            availability = soup.select_one('div.inStockSmall').text
        except:
            availability = 'Out of Stock'
            
        url = driver.current_url
            
        # Add the scraped data to the existing dictionary Website 12
        
        scraped_data['Website-17'] = 'Fox Appliance Parts'
        scraped_data['price_appliance_depot'] = price
        scraped_data['available_appliance_depot'] = availability
        scraped_data['url_appliance_depot'] = url
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_appliance_depot'] = ""
        scraped_data['available_appliance_depot'] = ""
        scraped_data['url_appliance_depot'] = ""
    
    finally:
        driver.quit()
        return scraped_data
