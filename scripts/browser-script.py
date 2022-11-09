import time 
import csv
# from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

options = webdriver.ChromeOptions()
options.add_extension('../plugins/Adblock_5.3.0_0.crx')
driver = webdriver.Chrome('./chromedriver',options=options)  # Optional argument, if not specified will search path.
filename = '../data/websites.csv'
time.sleep(10)

driver.get('http://www.wired.com')

# with open(filename, 'r') as csvfile:
#     datareader = csv.reader(csvfile)
#     for row in datareader:
#         driver.get(row[2]);
#         time.sleep(5) # Let the user actually see something!
#         search_box = driver.find_element_by_name('q')
#         search_box.send_keys('ChromeDriver')
#         search_box.submit()
#         time.sleep(5) # Let the user actually see something!

time.sleep(10)
driver.quit()
