from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_reliable(part_number, options):
    url = "https://reliableparts.net/us/content/#/login"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        #Login Details 
        
        box1 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/main/div/div/div[2]/section/div/div[2]/form/input[1]')
        box1.send_keys('015089')
        box2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/main/div/div/div[2]/section/div/div[2]/form/input[2]')
        box2.send_keys('ChangeMe2@')
        sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/main/div/div/div[2]/section/div/div[2]/form/div[2]/div')
        driver.execute_script("arguments[0].click();", sign_in)
        
        time.sleep(6)
        
        #Enter Part number is box
        box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/section/main/article/div/div/div/div/section[1]/div/div/div/div/div/div/div/div/div/div/div/form/div/div/div[1]/input')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[2]/p')
        if len(ui) > 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/div/a[1]')
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
    
    # Scrape the data
    try:
        price_final = soup.find('p', class_='rp-part-details-desktop--info--price').text
        stock = soup.select_one('div.rp-ship-from-row--addresses--stock div').text
        
        # Extract the URL of the part
        url2 = driver.current_url
        
    except AttributeError:
        price_final = 'Not found'
        stock = 'Not found'
        url2 = ''
    
    scraped_data = {}
    try:
        # Add the scraped data to the existing dictionary Website 2
        scraped_data['Website-2'] = 'Reliable Parts'
        scraped_data['PARTS_NUMBER'] = part_number
        scraped_data['price_reliable'] = price_final
        scraped_data['availability_reliable'] = stock
        scraped_data['url_reliable'] = url2
    except:
        scraped_data['Website-2'] = ""
        scraped_data['PARTS_NUMBER'] = ""
        scraped_data['price_reliable'] = ""
        scraped_data['availability_reliable'] = ""
        scraped_data['url_reliable'] = ""
    
    driver.quit()
    return scraped_data