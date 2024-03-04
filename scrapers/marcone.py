from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_marcone(part_number, options):
    url = "https://beta.marcone.com/UserLogin"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(2)
    
    # Wait for the element to be rendered:
    try:
        #Login Details 
        
        box1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/form/input[1]')
        box1.send_keys('searslogicbroker')
        box2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/form/input[2]')
        box2.send_keys('SLBmarcone321')
        sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/form/input[3]')
        driver.execute_script("arguments[0].click();", sign_in)

        time.sleep(6)
        
        #Enter Part number is box
        box = driver.find_element(By.XPATH, '/html/body/div[9]/div/div[2]/div[2]/div[1]/div[2]/input')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
    except:
        pass
    
    # Check if the "Use Subbed Part' UI is displayed
    try:
        ui = driver.find_elements(By.XPATH, '/html/body/div[10]/form/div[1]/div[1]/div[2]/h4')
        if len(ui) > 0:
            # Click on the first product link
            click = driver.find_element(By.XPATH, '/html/body/div[10]/form/div[1]/div[1]/div[2]/h4/a')
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
        price14 = soup.find('tr', id='trPrice').find('td', class_='a-span12 priceblock_ourprice big_size').text.strip()
        
        # Check availability
        availability = soup.find('span', class_ ='a-color-success')
        if availability:
            try:
                availability_text = soup.find('span', class_='a-color-success').text.strip()
            except:
                availability_text = 'In Stock'
                
        else:
            try:
                availability_text = soup.find('span', class_='a-color-error').text.strip()
            except:
                availability_text = 'Out of Stock'
            
        Availability14 = availability_text

        
        # Extract the URL of the part
        url14 = driver.current_url
        
    except AttributeError:
        price14 = 'Not found'
        Availability14 = 'Not found'
        url14 = ''
    
    scraped_data = {}

    try:
        # Add the scraped data to the existing dictionary Website 14
        scraped_data['Website-14'] = 'Marcone'
        scraped_data['Price-14'] = price14
        scraped_data['Available-14'] = Availability14
        scraped_data['URL14'] = url14
    except:
        scraped_data['Website-14'] = ""
        scraped_data['Price-14'] = ""
        scraped_data['Available-14'] = ""
        scraped_data['URL14'] = ""
    
    driver.quit()
    return scraped_data
