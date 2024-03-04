from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_appliance_parts(part_number, options):
    url = "https://www.appliancepartscompany.com/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    # Wait for the element to be rendered:
    try:
        box = driver.find_element(By.XPATH, '//*[@id="site-header"]/div[5]/div/div/div/div[2]/div/div/div/div/form/div/div/span/input[2]')
        box.send_keys(part_number)
        box.send_keys(Keys.RETURN)
        
        time.sleep(2)
    except:
        pass
    
    # Click on the dropdown to expand it
    try:
        dropdown = driver.find_element(By.XPATH, '//*[@id="list-header-filters"]/div/div/div[2]/select')
        driver.execute_script("arguments[0].click();", dropdown)

        # Select the "Relevance" option
        select = Select(dropdown)
        select.select_by_visible_text('Relevance')
    

        # Wait for the page to load
        time.sleep(1)

        #click on element
        click = driver.find_element(By.XPATH, '//*[@id="facet-browse"]/section/div[2]/div[2]/div[4]/div/div/div/div[2]/a')
        driver.execute_script("arguments[0].click();", click)
        
        # Wait for the page to load
        time.sleep(2) 
        
    except:
        pass


    #get soup
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    except:
        pass

    # Scrape the data
    try:
        price5 = soup.find('span', class_ = 'product-views-price-lead').text
        td_tag = soup.find('td', string='Stock Total')
        Availability5 = td_tag.find_next_sibling('td').text
        
        # Extract the URL of the part
        url5 = driver.current_url
        
    except AttributeError:
        price5 = 'Not found'
        td_tag = ''
        Availability5 = 'No available '
        url5 = ''

    scraped_data = {}
    # Add the scraped data to the existing dictionary Website 5
    try:
        scraped_data['Website-5'] = 'Appliance Parts Company'
        scraped_data['Price-5'] = price5
        scraped_data['Available-5'] = Availability5
        scraped_data['URL5'] = url5
        
    except:
        scraped_data['Website-5'] = ""
        scraped_data['Price-5'] = ""
        scraped_data['Available-5'] = ""
        scraped_data['URL5'] = ""
    
    driver.quit()
    return scraped_data