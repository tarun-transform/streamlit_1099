from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import streamlit as st

def scrape_fox(part_number, options):
    driver = webdriver.Chrome(options=options)
    try:
        url = "https://www.foxatlanta.com/"
        driver.get(url)
        
        time.sleep(2)
        scraped_data = {}
        # Wait for the element to be rendered
        
        try:
            box = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[1]/header/div[1]/div[2]/div/div[2]/form/div[2]/span/input')
            box.clear()
            box.send_keys(part_number)
            box.send_keys(Keys.RETURN)
            
            time.sleep(2)
            
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            
            
            try:
                # Check if the "Search Part' UI is displayed
                ui = driver.find_elements(By.XPATH, '//*[@id="tst_productList_container"]/h3')
                if len(ui) > 0:
                    # Click on the first product link
                    click = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/ul/li[1]/div[2]/div[1]/div[1]/div[1]/a')
                    driver.execute_script("arguments[0].click();", click)
                    
                    # Wait for the page to load
                    time.sleep(1)
                    
            except:
                pass

            # Wait for the page to load
            time.sleep(2)
        
        
            #get soup
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            price_fox = soup.find('span',class_ = 'unit-net-price').text.strip()
            try:
                availability_fox = soup.select_one('div.availability span').text.strip()
            except:
                availability_fox = 'Out of Stock'
                
            url_fox = driver.current_url
        
        except AttributeError:
            price_fox = 'Not found'
            availability_fox = 'Not available'
            url_fox = ''
            
        # Add the scraped data to the existing dictionary Website 12
        
        scraped_data['Website-17'] = 'Fox Appliance Parts'
        scraped_data['price_fox'] = price_fox
        scraped_data['available_fox'] = availability_fox
        scraped_data['url_fox'] = url_fox
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_fox'] = ""
        scraped_data['available_fox'] = ""
        scraped_data['url_fox'] = ""
    
    finally:
        driver.quit()

        return scraped_data
