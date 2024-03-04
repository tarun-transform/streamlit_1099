from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_parts_simple(part_number, options):
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
        box = driver.find_element(By.XPATH, '//*[@id="l-desktop-search"]')
        box.clear()
        box.send_keys(i)
        box.send_keys(Keys.RETURN)
        
        time.sleep(1)

        try:
            # Check if the "Search Part' UI is displayed
            ui = driver.find_elements(By.XPATH, '//*[@id="js-site-wrapper"]/main/div[2]/div[1]/div[1]/div/div[4]/p')
            if len(ui) > 0:
                # Click on the first product link
                click = driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div/p[1]/a')
                driver.execute_script("arguments[0].click();", click)
                
                # Wait for the page to load
                time.sleep(1)
                
        except:
            pass
        
        time.sleep(2)
    
    
        #get soup
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Scrape the data
        product_title = soup.select_one('div.column h1').text
        manufacturer = 'N/A'
        description = soup.find('div',class_ = 'product-description').text
        price = soup.find('span',class_ = 'product-price').text.strip()
        availability2 = soup.find('button', class_ = 'button button-block uppercase add-to-cart bg-green white bold').text
        
        if availability2 == 'Add to Cart':
            availability = 'In Stock'
        else:
            availability = 'Out of Stock'

        url = driver.current_url
        
        # Append the scraped data to the DataFrame
        # scraped_data = scraped_data.append({'PARTS_NUMBER': i, 'Product Title': product_title, 'Manufacturer': manufacturer, 
        #                'Description': description,
        #                'Price': price, 'Availability': availability,'URL': url}, ignore_index=True) 
        try:
            # scraped_data['Website-4'] = 'Part Select'
            scraped_data['price_guaranteed_parts'] = price
            scraped_data['available_guaranteed_parts'] = availability
            scraped_data['url_guaranteed_parts'] = url
        except:
            # scraped_data['Website-4'] = ""
            scraped_data['price_guaranteed_parts'] = ""
            scraped_data['available_guaranteed_parts'] = ""
            scraped_data['url_guaranteed_parts'] = ""

    except:
        print('opening home page')
        driver.get('https://www.guaranteedparts.com/')
    
    finally:
        driver.quit()
        return scraped_data
