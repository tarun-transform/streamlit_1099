from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_encompass(part_number, options):
    url = "https://encompass.com/account"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        #Login Details 
        
        box1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[1]/div/section/div/form/input[4]')
        box1.send_keys('185009')
        box2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[1]/div/section/div/form/input[5]')
        box2.send_keys('RONALD1')
        log_in = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[1]/div/section/div/form/div[3]/div/button')
        driver.execute_script("arguments[0].click();", log_in)

        
        time.sleep(5)
        
        #Enter Part number is box
        box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/form/div[1]/span/input[2]')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '/html/body/div[1]/div[4]/div/section/header/h2')
        if len(ui) > 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/section/div/div/table/tbody/tr[1]/td[1]/a')
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
        # Extracting price
        price13 = soup.find('p', {'class': 'price ep-price__dealer'}).text.strip()
        price13 = price13.replace('$', '')
        
        availability = soup.find('button', class_='btn btn-in-stock')
        if availability:
            try:
                availability_text = soup.find('button', class_='btn btn-in-stock').text.strip()
            except:
                availability_text = 'In Stock'
                
        else:
            try:
                availability_text = soup.find('div', class_='alert alert-warning alert-sm').text.strip()
            except:
                availability_text = 'Out of Stock'
            
        Availability13 = availability_text
        
        # Extract the URL of the part
        url13 = driver.current_url
        
    except AttributeError:
        price13 = 'Not found'
        Availability13 = 'Not found'
        url13 = ''
    
    scraped_data = {}
    try:
        # Add the scraped data to the existing dictionary Website 13
        scraped_data['Website-13'] = 'Encompass Simply Parts'
        scraped_data['Price-13'] = price13
        scraped_data['Available-13'] = Availability13
        scraped_data['URL13'] = url13
    except:
        scraped_data['Website-13'] = ""
        scraped_data['Price-13'] = ""
        scraped_data['Available-13'] = ""
        scraped_data['URL13'] = ""
    
    driver.quit()
    return scraped_data