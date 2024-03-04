from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_tribles(part_number, options):
    url = "https://www.tribles.com/login"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        #Login Details 
        
        box1 = driver.find_element(By.XPATH, '//*[@id="username"]')
        box1.send_keys('355000')
        box2 = driver.find_element(By.XPATH, '//*[@id="password"]')
        box2.send_keys('sears123')
        sign_in = driver.find_element(By.XPATH, '//*[@id="middle"]/div/form/div[1]/p[2]/button')
        driver.execute_script("arguments[0].click();", sign_in)

        time.sleep(3)
        
        #navigate to model lookup
        model_lookup = driver.find_element(By.XPATH, '//*[@id="wrapper"]/footer/div/div[1]/div/div[2]/div[1]/ul[3]/li[3]/a')
        driver.execute_script("arguments[0].click();", model_lookup)
        
        #Enter Part number in box
        box = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div/form/div/input')
        driver.execute_script("arguments[0].click();", box)
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
    except:
        pass
    
    # Check if the "Search Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/h2')
        if len(ui) > 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form[1]/div/div[1]/a')
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
        price15 = soup.find('span', class_='yourPrice').text
        
        # Check availability
        availability = soup.find('span', class_='inStock')
        if availability:
            availability_text = availability.text.strip()
        else:
            availability_text = 'Temp. Out of Stock'
            
        Availability15 = availability_text
        
        # Extract the URL of the part
        url15 = driver.current_url
        
    except AttributeError:
        price15 = 'Not found'
        Availability15 = 'Not found'
        url15 = ''
    
    scraped_data = {}
    try:
        # Add the scraped data to the existing dictionary Website 14
        scraped_data['Website-15'] = 'Tribals'
        scraped_data['Price-15'] = price15
        scraped_data['Available-15'] = Availability15
        scraped_data['URL15'] = url15
    except:
        scraped_data['Website-15'] = ""
        scraped_data['Price-15'] = ""
        scraped_data['Available-15'] = ""
        scraped_data['URL15'] = ""
    
    return scraped_data