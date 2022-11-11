import time
import csv
from browsermobproxy import Server
import  urllib.parse 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import json


server = Server('./browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()

options = webdriver.ChromeOptions()
options.add_extension('../plugins/Adblock_5.3.0_0.crx')
# options.add_argument('captureHeaders: True')
# options.add_argument(f'--proxy-server={proxy.selenium_proxy()}') # Proxy Issue 
url = urllib.parse.urlparse(proxy.proxy).path
driver = webdriver.Chrome('./chromedriver',options=options)  # Optional argument, if not specified will search path.
# driver.set_proxy(proxy.selenium_proxy())
options.add_argument("--proxy-server={0}".format(url))


filename = '../data/websites.csv'
time.sleep(10)

proxy.new_har('bbc')
driver.get('http://www.bbc.com')

result = json.dumps(proxy.har, ensure_ascii=False)
output_folder = "../data/data_AdBlock";


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
with open(output_folder + "/bbc" +'.har', 'w+') as har_file:
    json.dump(proxy.har, har_file)
# out.close();

server.stop()
driver.quit()
