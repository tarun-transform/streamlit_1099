from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_all_brands(part_number, options):
    driver = webdriver.Chrome(options=options)
    search_box_xpath = '//*[@id="SearchTextInput"]'
    url = "https://allbrandonline.com/"
    scraped_data = {}
    try:
        driver.get(url)
        time.sleep(2)

        box = driver.find_element(By.XPATH, search_box_xpath)
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        
        try:
            # Check if the "Search Part' UI is displayed
            ui = driver.find_elements(By.XPATH, '//*[@id="SSCartegories"]/div[1]')
            if len(ui) > 0:
                # Click on the first product link
                click = driver.find_element(By.XPATH, '//*[@id="SSResults"]/div[2]/a[2]')
                driver.execute_script("arguments[0].click();", click)
                
                # Wait for the page to load
                time.sleep(1)
                
        except:
            pass

            
        # Wait for the page to load
        time.sleep(2)

        # Create BeautifulSoup object
        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        # try:
            # Extract product title
        product_title = soup.find('td', class_='ItemDetailattribute').text

        # Extract your price
        price = soup.find('tr', class_='Price').text
        price = price.replace("Price:","").strip()
        
        # Check availability
        Availability = soup.find('tr', id='TotalAvailabilityWrap').find('td').text.strip()
        Availability = Availability.replace("Total Availability:", "").strip()
        Availability = Availability.replace("EA", "").strip()

        # Check if Availability is a valid number
        if Availability.isdigit():  # Check if it's a valid number
            Availability = int(Availability)
            if Availability > 0:
                result = 'In-Stock'
            else:
                result = 'Out of Stock'
        else:
            result = 'Out of Stock'  # If Availability is not a valid number
            
        Availability = result

        #URL
        url = driver.current_url
        
        # Append the scraped data to the DataFrame
        # scraped_data = scraped_data.append({'PARTS_NUMBER': i, 'Product Title': product_title, 
        #                                    'Price': price, 
        #                                    'Availability': Availability,'URL':url}, 
        #                                    ignore_index=True)
    
    # except:
    #     pass
        
    # Add the scraped data to the existing dictionary Website 12
    
        scraped_data['Website-17'] = 'Fox Appliance Parts'
        scraped_data['price_all_brands'] = price
        scraped_data['available_all_brands'] = Availability
        scraped_data['url_all_brands'] = url
    except:
        scraped_data['Website-17'] = ""
        scraped_data['price_all_brands'] = "Not found"
        scraped_data['available_all_brands'] = "Not available"
        scraped_data['url_all_brands'] = ""
    
    finally:
        driver.quit()
        return scraped_data
