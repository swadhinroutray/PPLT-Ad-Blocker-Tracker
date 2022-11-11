from browsermobproxy import Server
from selenium import webdriver
import json,time,csv
output_folder = "../data/data_AdBlock/";
web_filename = '../data/websites.csv'

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
        self.server = Server(self.browser_mob)
        self.server.start()
        self.proxy = self.server.create_proxy()

    def __start_driver(self):
        """prepare and start driver"""
        options = webdriver.ChromeOptions()
        options.add_extension('../plugins/Adblock_5.3.0_0.crx')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        # profile = webdriver.Chrome()
        options.add_argument("--proxy-server={0}".format(self.proxy.proxy))
        self.driver = webdriver.Chrome('./chromedriver', options=options)
        # self.driver.set_proxy(self.proxy.selenium_proxy())

    def start_all(self):
        """start server and driver"""
        self.__start_server()
        self.__start_driver()

    def create_har(self, title, url):
        """start request and parse response"""
        self.proxy.new_har(title)
        time.sleep(10)
        self.driver.get(url)
        time.sleep(5)
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
        for row in datareader:
            RUN.start_all()
            RUN.create_har(row[1], row[2])
            RUN.stop_all()