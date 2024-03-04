import streamlit as st
from site_visibility import site_visibility

def display_partsdr(scraped_data):
    st.markdown('---')
        
    # Get the URL for the Parts Doctor website from the 'url' column of 'scraped_data'
    parts_doctor_url = scraped_data['url_partsdr']

    # Create a box for Website-1 details
    # st.markdown(f"#### 1️⃣ [Parts Doctor]({parts_doctor_url})")
    st.markdown(f"#### [Parts Doctor]({parts_doctor_url})")
    st.markdown(f"**List Price:** {scraped_data['list_price_partsdr']}")
    st.markdown(f"**Final Price:** {scraped_data['price_partsdr']}")
    st.markdown(f"**Availability:** {scraped_data['availability_partsdr']}")

def display_data(scraped_data, icon, name, url_key, price_key, availability_key):
    st.markdown('---')

    try:
        # Create a box for Website-1 details
        st.markdown(f"#### {icon} [{name}]({scraped_data[url_key]})")
        st.markdown(f"**Price:** {scraped_data[price_key]}")
        st.markdown(f"**Availability:** {scraped_data[availability_key]}")
    except:
        st.markdown(f"#### {icon} {name}")
        st.markdown(f"**Price:** Not found")
        st.markdown(f"**Availability:** Not found")


def display_scraped_data(scraped_data_array):
    scraped_data = {}
    for dict in scraped_data_array:
        scraped_data.update(dict)
    
    try:
        # Display the scraped data in Streamlit
        st.title('🛠️ Part Details')

        # Create spacing before About
        st.markdown('---')
    
        #About Box
        st.markdown('### 📦 About:')
    
        st.markdown(f"**PART NUMBER:** {scraped_data['PARTS_NUMBER']}")
        st.markdown(f"**Product Title:** {scraped_data['Product Title']}")
        st.markdown(f"**Manufacturer:** {scraped_data['Manufacturer']}")
        st.markdown(f"**Description:** {scraped_data['Description']}")
        # 0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣
    except:
        st.markdown('### Error scraping part details, please try again!')

    if site_visibility['All_Brands']:
        display_data(scraped_data, '', 'All Brands Online', 'url_all_brands', 'price_all_brands', 'available_all_brands')
    
    # if site_visibility['Appliance_Depot']:
        # display_data(scraped_data, '', 'Appliance Depot', 'url_appliance_depot', 'price_appliance_depot', 'available_appliance_depot')
    
    if site_visibility['Appliance_Parts']:
        display_data(scraped_data, '', 'Appliance Parts Company', 'URL5', 'Price-5', 'Available-5')
    
    if site_visibility['Automatic_Appliance']:
        display_data(scraped_data, '', 'Automatic Appliance', 'URL6', 'Price-6', 'Available-6')
    
    if site_visibility['Cashwell']:
        display_data(scraped_data, '', 'Cashwell Appliance Parts', 'URL16', 'Price-16', 'Available-16')
    
    if site_visibility['Coast_Parts']:
        display_data(scraped_data, '', 'Coast Appliance Parts', 'URL10', 'Price-10', 'Available-10')
    
    if site_visibility['Dey_Parts']:
        display_data(scraped_data, '', 'Dey Distributing', 'URL9', 'Price-9', 'Available-9')
    
    if site_visibility['DL_Parts_Co']:
        display_data(scraped_data, '', 'D&L Parts Company', 'URL11', 'Price-11', 'Available-11')
    
    if site_visibility['Ereplacement_Parts']:
        display_data(scraped_data, '', 'E-Replacement Parts', 'URL12', 'Price-12', 'Available-12')
    
    if site_visibility['Encompass']:
        display_data(scraped_data, '', 'Encompass Simply Parts', 'URL13', 'Price-13', 'Available-13')
    
    if site_visibility['Fox']:
        display_data(scraped_data, '', 'Fox Appliance Parts', 'url_fox', 'price_fox', 'available_fox')
    
    if site_visibility['Genuine']:
        display_data(scraped_data, '', 'Genuine Appliance Parts', 'url_genuine', 'price_genuine', 'available_genuine')
    
    if site_visibility['Guaranteed']:
        display_data(scraped_data, '', 'Guaranteed Parts', 'url_guaranteed', 'price_guaranteed', 'available_guaranteed')
    
    if site_visibility['Ideal_Appliance']:
        display_data(scraped_data, '', 'Ideal Appliance', 'URL7', 'Price-7', 'Available-7')
    
    if site_visibility['Kitchen_Aid']:
        display_data(scraped_data, '', 'Kitchen Aid', 'url_kitchen_aid', 'price_kitchen_aid', 'available_kitchen_aid')
    
    if site_visibility['Marcone']:
        display_data(scraped_data, '', 'Marcone', 'URL14', 'Price-14', 'Available-14')
    
    if site_visibility['Parts_Dr']:
        display_partsdr(scraped_data)
    
    if site_visibility['Part_Select']:
        display_data(scraped_data, '', 'Part Select', 'url_part_select', 'price_part_select', 'available_part_select')
    
    if site_visibility['Parts_Simple']:
        display_data(scraped_data, '', 'Parts Simple', 'url_parts_simple', 'price_parts_simple', 'available_parts_simple')
    
    if site_visibility['Reliable']:
        display_data(scraped_data, '', 'Reliable Parts', 'url_reliable', 'price_reliable', 'availability_reliable')
    
    if site_visibility['Tribles']:
        display_data(scraped_data, '', 'Tribles', 'URL15', 'Price-15', 'Available-15')
    
    if site_visibility['UED']:
        display_data(scraped_data, '', 'UED Appliance Parts', 'url_ued', 'price_ued', 'available_ued')
    
    if site_visibility['VV_Appliance_Parts']:
        display_data(scraped_data, '', 'V&V Appliance Parts', 'URL8', 'Price-8', 'Available-8')
        
        

        # Create spacing before the chart
        st.markdown('---')

        # st.write(scraped_data)
        
    
