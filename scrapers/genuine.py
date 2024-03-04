from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_genuine(part_number, options):
    url = "https://www.genuinereplacementparts.com/index.php"
    driver = webdriver.Chrome(options=options)

    script = """
    Object.defineProperty(navigator, 'language', {
        get: function() { return 'en-US'; }
    });
    Object.defineProperty(navigator, 'languages', {
        get: function() { return ['en-US', 'en']; }
    });
    Object.defineProperty(navigator, 'referrer', {
        get: function() { return 'https://www.google.com'; }
    });
    """

    driver.execute_script(script)
    driver.get(url)
    
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

    scraped_data = {}

    time.sleep(2)
    
    try:
        box = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/div/form/div/input')
        box.clear()
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
    
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
        
        # Append the scraped data to the DataFrame
        
        # try:
        #     scraped_data = scraped_data.append({'PARTS_NUMBER': i, 'Product Title': product_title, 'Manufacturer': manufacturer, 
        #                'Description': description,
        #                'Price': price, 'Availability': availability,'URL': url}, ignore_index=True)

        try:
            # scraped_data['Website-4'] = 'Part Select'
            scraped_data['price_genuine'] = price
            scraped_data['available_genuine'] = availability
            scraped_data['url_genuine'] = url
        except:
            # scraped_data['Website-4'] = ""
            scraped_data['price_genuine'] = ""
            scraped_data['available_genuine'] = ""
            scraped_data['url_genuine'] = ""
    
    except:
        print('opening home page')
        driver.get('https://www.genuinereplacementparts.com/index.php')
    
    finally:
        driver.quit()
        return scraped_data
