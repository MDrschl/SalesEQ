from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
import time
import numpy as np
import pandas as pd
from pandas.tseries.offsets import MonthEnd
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# Toggle date range
MONTH_START_LIST = []

for year in range(2012, 2023):
    for month in range(1, 12):
        MONTH_START_LIST.append(f'{year}-{str(month).zfill(2)}-01')
        
MONTH_END_LIST = (pd.to_datetime(MONTH_START_LIST) + MonthEnd(1)).strftime('%Y-%m-%d').tolist()

DATE_RANGE_LIST = list(zip(MONTH_START_LIST, MONTH_END_LIST))

# Input Query
QUERY = "(((smartphone or smartphones) and (sale or sales) and (market or markets)) or \
((smartphone or smartphones) and (model or models) and (feature or features)) or \
((smartphone or smartphones) and (worker or workers) and (union or unions) and (device or devices) and (company or companies))) \
and fmt=article"
# Input Data Sources
DATA_SOURCES = ['sfwsj', 'sfnyt', 'sfap', 'sfreut']

# TODO: Input Login Credentials
UID = "UID"
PASSWORD = "PASSWORD"
# TODO: Input Driver Path and File Save Path
DRIVER_PATH = "path/chromedriver"
FILE_PATH = 'path/articles.csv'

def toggle_data_source_pane():
    # expand data source pane
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[1]/div[1]").click()
    
    # input the code of the data source and select the returned option
    for data_source in DATA_SOURCES:
        time.sleep(1)
        browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[1]/div[1]/input').send_keys(data_source)
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[13]/table/tr/td/div')))
        browser.find_element('xpath', "/html/body/div[13]/table/tr/td/div").click()
        
    # remove the 'All Publications' search option
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/div/ul/li[1]/div/div/span").click()
    browser.find_element('xpath', "/html/body/div[4]/div/div[2]/span").click()
    
    # Press search
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/div[2]/ul/li[2]/input").click()

# Slightly different xpath in different scenario
def recover_data_source_pane():
    # expand data source pane
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[1]/div[1]").click()
    
    # input the code of the data source and select the returned option
    for data_source in DATA_SOURCES:
        time.sleep(1)
        browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[4]/td[2]/div[1]/div[1]/input').send_keys(data_source)
        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[12]/table/tr/td/div')))
        browser.find_element('xpath', "/html/body/div[12]/table/tr/td/div").click()
        
    # remove the 'All Publications' search option
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/div/ul/li[1]/div/div/span").click()
    browser.find_element('xpath', "/html/body/div[4]/div/div[2]/span").click()
    
    # Press search
    browser.find_element('xpath', "/html/body/form[2]/div[2]/div[2]/div/div[2]/ul/li[2]/input").click()
    
def toggle_query(date_pair): 
    # Input search query
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[2]/div[2]/div/div[1]/textarea').send_keys(QUERY)
    
    # Toggle Options (Duplicates: Off)
    Select(browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[3]/select')).select_by_visible_text('Off')
    
    # Toggle Options (Enter Date Range)
    Select(browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[1]/select')).select_by_visible_text('Enter date range...')
    
    # Input lower limit of date range
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[1]').send_keys(date_pair[0][-2:])
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[2]').send_keys(date_pair[0][5:-3])
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[3]').send_keys(date_pair[0][:4])
    
    # Input upper limit of date range
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[9]').send_keys(date_pair[1][-2:])
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[10]').send_keys(date_pair[1][5:-3])
    browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div/table/tbody/tr[2]/td/div[1]/div[1]/table/tbody/tr/td[2]/div[3]/div[1]/table/tbody/tr/td[2]/div/input[11]').send_keys(date_pair[1][:4])
    
    # Handle Data Source Pane
    toggle_data_source_pane()
    
    # Wait for articles to load
    time.sleep(10)

def scrap_article(row_no):
    wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/form[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[1]/div/div[2]/table/tbody/tr[{row_no}]/td[3]/div[1]')))
    # Get metadata of article in the search result page
    metadata = browser.find_element('xpath', f'/html/body/form[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[1]/div/div[2]/table/tbody/tr[{row_no}]/td[3]/div[1]').text
    # Click into article
    browser.find_element('xpath', f"/html/body/form[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[1]/div/div[2]/table/tbody/tr[{row_no}]/td[3]/a").click()
    return metadata
    
def scrap_page():
    # 100 articles per page
    for row_no in range(1, 101):
        time.sleep(1)
        try:
            metadata = scrap_article(row_no)
        # Catch exception when page accidentally go back to search page (Only data source pane needs to be recovered)
        except NoSuchElementException:
            try:
                recover_data_source_pane()
                metadata = scrap_article(row_no)
            except ElementNotInteractableException:
                break
        # Catch exception when server timeout
        except ElementNotInteractableException:
            try:
                if (browser.find_element('xpath', '/html/body/form[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[2]/div/div[2]/h1').text == "504 Gateway Time-out"):   
                    browser.back()
                metadata = scrap_article(row_no)
            except NoSuchElementException:
                break
        # Wait for headline and return it
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="hd"]/span')))
        
        except TimeoutException:
            continue
        headline = browser.find_element('xpath', '//*[@id="hd"]/span').text
        
        # Body of articles start from the 4th paragraph according to xpath
        paragraph_no = 4
        article_text = ''
        # Continue to append text until no more text can be scrapped
        while True:
            try:
                temp = browser.find_element('xpath', f'/html/body/form[2]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[2]/div/div[2]/div[3]/div/p[{str(paragraph_no)}]').text
                article_text = article_text + temp + ' '
                paragraph_no+=1
            except NoSuchElementException:
                break
        # Append this article to the master list
        temp_dict = {'Cycle_month': cycle_month
                   , 'Headline': headline
                   , 'Metadata': metadata
                   , 'Text': article_text}
        
        articles_list.append(temp_dict)
        
        # Go back to the search result page
        browser.back()

# Chrome Options preventing timeout error
ChromeOptions = webdriver.ChromeOptions()

ChromeOptions.add_argument('--disable-browser-side-navigation')

# Declare chrome window
browser = webdriver.Chrome(executable_path = DRIVER_PATH, chrome_options=ChromeOptions)

# Declare wait object
wait = WebDriverWait(browser, 30)

# Go to HKU Library data source page
browser.get('https://libguides.lib.hku.hk/az.php?a=f')

# Locate Factiva and click it
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[4]/section[3]/div/div[2]/div/div/div[7]/div[1]/div[1]/a')))
browser.find_element('xpath', "/html/body/div[4]/section[3]/div/div[2]/div/div/div[7]/div[1]/div[1]/a").click()

# Switch to Factiva Login Window (New Tab)
original_window = browser.current_window_handle
for window_handle in browser.window_handles:
    if window_handle != original_window:
        browser.switch_to.window(window_handle)
        break
# Input login credentials
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/section/div/div[2]/section/article/div/div/div/form/p[2]/input')))

uid_input = browser.find_element('xpath', '/html/body/div[2]/div/section/div/div[2]/section/article/div/div/div/form/p[2]/input')
uid_input.send_keys(UID)

password_input = browser.find_element('xpath', '/html/body/div[2]/div/section/div/div[2]/section/article/div/div/div/form/p[3]/input')
password_input.send_keys(PASSWORD)

submit_button = browser.find_element('xpath', "/html/body/div[2]/div/section/div/div[2]/section/article/div/div/div/form/p[6]/input[1]")
submit_button.click()

# Wait for query page to load
time.sleep(40)

articles_list = []

# Loop through each month
for date_pair in DATE_RANGE_LIST:
    time.sleep(5)
    # Handle query
    toggle_query(date_pair)    
    cycle_month = date_pair[0][:4] + date_pair[0][5:-3]
    # Scrap search results
    scrap_page()
    # Back to search page
    browser.find_element('xpath', "/html/body/div[2]/div/ul[1]/li[2]/a").click()
    
browser.close()

# Process article data 
col2keep = ['Cycle_month', 'Headline', 'Text', 'Source', 'Date', 'Word_count']

df_article = pd.DataFrame(articles_list)

df_article['Source'] = df_article['Metadata'].str.split(', ', expand=True)[0]
df_article['Column1'] = df_article['Metadata'].str.split(', ', expand=True)[1]
df_article['Column2'] = df_article['Metadata'].str.split(', ', expand=True)[2]
df_article['Column3'] = df_article['Metadata'].str.split(', ', expand=True)[3]

# Use function to pinpoint data location
df_article['Date'] = np.where(df_article['Column1'].str.contains('20[0-9][0-9]$')
                              , df_article['Column1']
                              , df_article['Column2'])

df_article['Word_count'] = np.where(df_article['Column1'].str.contains('words')
                              , df_article['Column1']
                              , np.where(df_article['Column2'].str.contains('words')
                                                            , df_article['Column2']
                                                            , df_article['Column3']))
                        
df_article = df_article[col2keep]

df_article.to_csv(FILE_PATH)    