from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_parts_simple(part_number, options):
    driver = webdriver.Chrome(options=options)
    
    scraped_data = {}
    search_box_xpath = '/html/body/div[2]/div[1]/div/div[2]/form/input[1]'
    try:
        try:
            box = driver.find_element(By.XPATH, search_box_xpath)
            box.clear()
            box.send_keys(part_number)
            box.send_keys(Keys.RETURN)
            
            time.sleep(5)
            
            try:
                # Check if the "Search Part' UI is displayed
                ui = driver.find_elements(By.XPATH, '//*[@id="shop-by-brand-sec"]/div')
                if len(ui) > 0:
                    # Click on the first product link
                    click = driver.find_element(By.XPATH, '//*[@id="search-result-data"]/ul/li[1]/a/div')
                    driver.execute_script("arguments[0].click();", click)
                    
                    # Wait for the page to load
                    time.sleep(1)
                    
            except:
                pass
        
        
            #get soup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            condition_check = soup.find('div', class_ = 'product attribute product_used_unused_1')
            condition = condition_check.find('div', class_ = 'value').text.strip()
            
            # Scrape the data
            
            if condition == 'New Product':
                product_title = soup.select_one('div.page-title-wrapper span').text
                manufacturer = 'N/A'
                description = 'N/A'
                price = soup.find('span',class_ = 'price').text.strip()
                try:
                    availability = soup.select_one('div.stock span').text
                except:
                    availability = 'Out of Stock'
                    
                url = driver.current_url
                
                # Append the scraped data to the DataFrame
                scraped_data = scraped_data.append({'PARTS_NUMBER': i, 'Product Title': product_title, 'Manufacturer': manufacturer, 
                               'Description': description,
                               'Price': price, 'Availability': availability,'URL': url}, ignore_index=True) 
            else:
                pass
            
            search_box_xpath = '/html/body/div[2]/header/div[2]/div[2]/div[2]/form/div[1]/div/input'

        except:
            box = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/form/input[1]')
            box.clear()
            box.send_keys(i)
            box.send_keys(Keys.RETURN)
            
            time.sleep(5)
            
            try:
                # Check if the "Search Part' UI is displayed
                ui = driver.find_elements(By.XPATH, '//*[@id="shop-by-brand-sec"]/div')
                if len(ui) > 0:
                    # Click on the first product link
                    click = driver.find_element(By.XPATH, '//*[@id="search-result-data"]/ul/li[1]/a/div')
                    driver.execute_script("arguments[0].click();", click)
                    
                    # Wait for the page to load
                    time.sleep(1)
                    
            except:
                pass
        
        
            #get soup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            condition_check = soup.find('div', class_ = 'product attribute product_used_unused_1')
            condition = condition_check.find('div', class_ = 'value').text.strip()
            
            # Scrape the data
            
            if condition == 'New Product':
                product_title = soup.select_one('div.page-title-wrapper span').text
                manufacturer = 'N/A'
                description = 'N/A'
                price = soup.find('span',class_ = 'price').text.strip()
                try:
                    availability = soup.select_one('div.stock span').text
                except:
                    availability = 'Out of Stock'
                    
                url = driver.current_url
    
        
        scraped_data['Website-17'] = 'Fox Appliance Parts'
        scraped_data['price_parts_simple'] = price
        scraped_data['available_parts_simple'] = availability
        scraped_data['url_parts_simple'] = url
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_parts_simple'] = "Not found"
        scraped_data['available_parts_simple'] = "Not available"
        scraped_data['url_parts_simple'] = ""
    
    finally:
        driver.quit()
        return scraped_data
