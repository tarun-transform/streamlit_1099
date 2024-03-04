import os
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import plotly.graph_objects as go
import pandas as pd
import time

from scrapers.partsdr import scrape_parts_dr
from scrapers.reliable import scrape_reliable
from scrapers.appliance_parts import scrape_appliance_parts
from scrapers.part_select import scrape_part_select
from scrapers.automatic_appliance import scrape_automatic_appliance
from scrapers.ideal_appliance import scrape_ideal_appliance
from scrapers.vv_appliance_parts import scrape_vv_appliance_parts
from scrapers.dey_parts import scrape_dey_parts
from scrapers.coast_parts import scrape_coast_parts
from scrapers.dl_parts_co import scrape_dl_parts_co
from scrapers.ereplacement_parts import scrape_ereplacement_parts
from scrapers.encompass import scrape_encompass
from scrapers.marcone import scrape_marcone
from scrapers.tribles import scrape_tribles
from scrapers.cashwell import scrape_cashwell
from scrapers.genuine import scrape_genuine
from scrapers.fox import scrape_fox
from scrapers.parts_simple import scrape_parts_simple
from scrapers.all_brands import scrape_all_brands
from scrapers.appliance_depot import scrape_appliance_depot
from scrapers.guaranteed import scrape_guaranteed
from scrapers.kitchen_aid import scrape_kitchen_aid
from scrapers.ued import scrape_ued

from site_visibility import site_visibility
from display_data import display_scraped_data

import threading
import queue

def worker(func, part_number, options, q):
    result = func(part_number, options)
    q.put(result)

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")



def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)




def run_selenium_async(part_number):
    
    q = queue.Queue()

    functions = [
        # scrape_appliance_parts, 
        # scrape_automatic_appliance, 
        # scrape_cashwell, 
        # scrape_coast_parts, 
        scrape_dey_parts, 
        # scrape_dl_parts_co, 
        scrape_encompass, 
        scrape_marcone, 
        scrape_tribles, 
        scrape_cashwell, 
        scrape_genuine, 
        scrape_parts_simple,
        scrape_fox,
        scrape_all_brands,
        # scrape_appliance_depot,
        scrape_guaranteed,
        scrape_kitchen_aid,
        scrape_ued,

    ]

    threads = []
    for func in functions:
        t = threading.Thread(target=worker, args=(func, part_number, options, q))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    results = []
    while not q.empty():
        results.append(q.get())

    return results

def run_selenium_sync(part_number):
    scraped_data = []

    if site_visibility['All_Brands']:
        scraped_data.append(scrape_all_brands(part_number, options))
    
    # if site_visibility['Appliance_Depot']:
    #     scraped_data.append(scrape_appliance_depot(part_number, options))
    
    if site_visibility['Appliance_Parts']:
        scraped_data.append(scrape_appliance_parts(part_number, options))

    if site_visibility['Automatic_Appliance']:
        scraped_data.append(scrape_automatic_appliance(part_number, options))

    if site_visibility['Cashwell']:
        scraped_data.append(scrape_cashwell(part_number, options))
    
    if site_visibility['Coast_Parts']:
        scraped_data.append(scrape_coast_parts(part_number, options))
    
    if site_visibility['Dey_Parts']:
        scraped_data.append(scrape_dey_parts(part_number, options))
    
    if site_visibility['DL_Parts_Co']:
        scraped_data.append(scrape_dl_parts_co(part_number, options))
    
    if site_visibility['Encompass']:
        scraped_data.append(scrape_encompass(part_number, options))
    
    if site_visibility['Ereplacement_Parts']:
        scraped_data.append(scrape_ereplacement_parts(part_number, options))
    
    if site_visibility['Fox']:
        scraped_data.append(scrape_fox(part_number, options))
    
    if site_visibility['Genuine']:
        scraped_data.append(scrape_genuine(part_number, options))
    
    if site_visibility['Guaranteed']:
        scraped_data.append(scrape_guaranteed(part_number, options))
    
    if site_visibility['Ideal_Appliance']:
        scraped_data.append(scrape_ideal_appliance(part_number, options))
    
    if site_visibility['Kitchen_Aid']:
        scraped_data.append(scrape_kitchen_aid(part_number, options))
    
    if site_visibility['Marcone']:
        scraped_data.append(scrape_marcone(part_number, options))
    
    if site_visibility['Part_Select']:
        scraped_data.append(scrape_part_select(part_number, options))
    
    # if site_visibility['Parts_Dr']:
    if True:
        scraped_data.append(scrape_parts_dr(part_number, options))
    
    if site_visibility['Parts_Simple']:
        scraped_data.append(scrape_parts_simple(part_number, options))
    
    if site_visibility['Reliable']:
        scraped_data.append(scrape_reliable(part_number, options))
    
    if site_visibility['Tribles']:
        scraped_data.append(scrape_tribles(part_number, options))
    
    if site_visibility['UED']:
        scraped_data.append(scrape_ued(part_number, options))
    
    if site_visibility['VV_Appliance_Parts']:
        scraped_data.append(scrape_vv_appliance_parts(part_number, options))
 
    return scraped_data



def main():
    # Display the sidebar with the search bar
    st.sidebar.title('🔍 Search bar')
    part_number = st.sidebar.text_input('Enter part number')
    scraped_data = {}

    if st.sidebar.button('Submit'):
        # scraped_data = run_selenium_async(part_number)
        scraped_data = run_selenium_sync(part_number)
        
        #show balloons once data is scraped
        st.balloons()
    
    if scraped_data:
        display_scraped_data(scraped_data)
        
    else:
        # Display a single welcome message
        st.markdown('### Welcome! Enter a part number to get started')
        st.markdown('It might take a while for the search to run.')
    
    st.sidebar.markdown(f"[{'Main sites'}]({'https://partfinder.streamlit.app'})")
            
if __name__ == '__main__':
    main()
