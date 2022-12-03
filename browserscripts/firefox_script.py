from browsermobproxy import Server
from selenium import webdriver
import json
import time
import csv
import sys
output_folder = "../data/vanilla_firefox/"
web_filename = '../data/' + sys.argv[1]


class CreateHar(object):
    """create HTTP archive file"""

    def __init__(self, mob_path):
        """initial setup"""
        self.browser_mob = mob_path
        self.server = self.driver = self.proxy = None

    @staticmethod
    def __store_into_file(title, result):
        """store result"""
        har_file = open(output_folder + title + '.har', 'w+')
        har_file.write(str(result))
        har_file.close()

    def __start_server(self):
        """prepare and start server"""
        self.server = Server(self.browser_mob, options={
                             'existing_proxy_port_to_use': 8090})
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self):
        """prepare and start driver"""
        #profile = webdriver.FirefoxProfile()
        options = webdriver.FirefoxOptions()
        # set proxy in options
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.http", "localhost")
        options.set_preference("network.proxy.http_port", 8090)
        options.set_preference("network.proxy.ssl", "localhost")
        options.set_preference("network.proxy.ssl_port", 8090)
        options.set_preference("network.proxy.ftp", "localhost")
        options.set_preference("network.proxy.ftp_port", 8090)
        options.set_preference("network.proxy.socks", "localhost")
        options.set_preference("network.proxy.socks_port", 8090)
        options.set_preference("network.proxy.share_proxy_settings", True)

       # profile.update_preferences()
        # self.driver.set_proxy(self.proxy.selenium_proxy())

        # configure the webdriver to use the browsermob-proxy server

        # profile.set_proxy(self.proxy.selenium_proxy())

        #self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver = webdriver.Firefox(options=options)

        # self.driver.install_addon(r"/Users/jatanloya/PPLT-Ad-Blocker-Tracker/plugins/uBlock0_1.45.3b8.firefox.signed.xpi")

    def start_all(self):
        """start server and driver"""
        self.__start_server()
        self.__start_driver()

    def create_har(self, title, url):
        """start request and parse response"""
        self.proxy.new_har(title)
        # time.sleep(0.5)
        self.driver.get(url)
        time.sleep(2)
        result = json.dumps(self.proxy.har, ensure_ascii=False)
        self.__store_into_file(title, result)

    def stop_all(self):
        """stop server and driver"""
        self.server.stop()
        self.driver.quit()


if __name__ == '__main__':
    path = "./browsermob-proxy-2.1.4/bin/browsermob-proxy"
    RUN = CreateHar(path)
    with open(web_filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        RUN.start_all()
        for row in datareader:
            RUN.create_har(row[1], row[2])
        RUN.stop_all()
