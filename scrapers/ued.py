from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_ued(part_number, options):
    driver = webdriver.Chrome(options=options)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    
    scraped_data = {}
    try:
        driver.get('https://www.ued.net/')
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        
        box = driver.find_element(By.XPATH, '//*[@id="searchStrPart"]')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(1)
        
        
        try:
            # Check if the "Search Part' UI is displayed
            ui = driver.find_elements(By.XPATH, '//*[@id="searchResultsContainer"]/div/form/span[1]')
            if len(ui) > 0:
                # Click on the first product link
                click = driver.find_element(By.XPATH, '//*[@id="sbp"]/tbody/tr[1]/td[2]/a')
                driver.execute_script("arguments[0].click();", click)
                
                # Wait for the page to load
                time.sleep(1)
                
        except:
            pass
    
    
        #get soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Scrape the data
        product_title = 'N/A'
        manufacturer = soup.find_all('td', class_ = 'general')[1].text
        description = 'N/A'
        price = soup.find_all('td',class_ = 'right-align pricingColumn')[1].text.strip()
        try:
            availability = soup.select_one('td.general a').text.strip()
        except:
            availability = 'Out of Stock'
            
        url = driver.current_url
        
        scraped_data['Website-17'] = 'UED'
        scraped_data['price_ued'] = price
        scraped_data['available_ued'] = availability
        scraped_data['url_ued'] = url
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_ued'] = "Not found"
        scraped_data['available_ued'] = "Not available"
        scraped_data['url_ued'] = ""
    
    finally:
        driver.quit()
        return scraped_data
