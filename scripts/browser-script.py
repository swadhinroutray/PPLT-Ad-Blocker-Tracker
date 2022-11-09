import time 
import csv
from browsermobproxy import Server

from selenium import webdriver
from selenium.webdriver.chrome.options import Options 

server = Server('./browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()

options = webdriver.ChromeOptions()
options.add_extension('../plugins/Adblock_5.3.0_0.crx')
# options.add_argument('captureHeaders: True')
# options.add_argument(f'--proxy-server={proxy.selenium_proxy()}') # Proxy Issue 
driver = webdriver.Chrome('./chromedriver',options=options)  # Optional argument, if not specified will search path.
# driver.set_proxy(proxy.selenium_proxy())

filename = '../data/websites.csv'
time.sleep(10)

proxy.new_har('wired')
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

print(proxy.har)

time.sleep(10)
server.stop()
driver.quit()
