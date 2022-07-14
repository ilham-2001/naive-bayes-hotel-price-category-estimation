from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np

url = "https://www.google.com/travel/hotels?q=harga%20hotel%20di%20jakarta&gsas=1&rp=CgpYAGAAcgQIAhgAOAGKAhZoYXJnYSBob3RlbCBkaSBqYWthcnRhqAIA&ved=0CAAQ5JsGahcKEwj467eKiPf4AhUAAAAAHQAAAAAQBA&hl=en-ID&gl=id&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4308226%2C4515404%2C4597339%2C4649665%2C4703207%2C4718358%2C4722900%2C4723331%2C4741665%2C4757164%2C4758493%2C4762561%2C4779784%2C4786958%2C4787395%2C4790928%2C4794648&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAAaKwoNEgk6B0pha2FydGEaABIaEhQKBwjmDxAHGBsSBwjmDxAHGBwYATICEAAqDgoKEgEFKAE6A0lEUhoA&ap=MAFa9gIKBgiA6jAQACIDSURSKhYKBwjmDxAHGBsSBwjmDxAHGBwYASgAsAEAWAFgAGgBcgQIAhgAmgEJEgdKYWthcnRhogETCggvbS8wNDRydhIHSmFrYXJ0YaoBLwoCCCESAggIEgIIZRICCBUSAggNEgIIZxICCFsSAggvEgIIWhIDCIwCEgIIIBgBqgEHCgMI5QEYAKoBEwoCCBISAwibARICCGgSAghpGAGqAQcKAwjhARgAqgEHCgMIoQIYAKoBBwoDCOQBGACqAQ4KAggcEgIIURICCEcYAaoBBwoDCOIBGACqARMKAgglEgMI2wISAgh1EgIIdhgBqgESCgIIERICCEASAgg4EgIIAhgBqgEHCgMIxQIYAKoBLQoCCC4SAgg8EgMIhwESAggaEgIISBIDCIECEgIIAxICCAwSAwiPARICCCcYAaoBDAoDCK4BEgMIrwEYAaoBCwoDCOECEgIIYxgBqgELCgIINRIDCJYBGAGSAQIgAQ"
xpath = "/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div[2]/div[2]/div[1]/div/main/div/c-wiz/div[1]/div[4]/c-wiz[5]/c-wiz/div/div/div/div[1]/div/div[1]/div[1]/div[1]/h2"

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"


class WebScrapper:

    def __init__(self):
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

        # header = self.driver.find_elements(By.CLASS_NAME, "BgYkof")
        # div = self.driver.find_elements(By.CLASS_NAME, "kixHKb")

    def GetUrl(self, url):
        self.driver.get(url)

    # def initDriver(self):
    #     try:
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.ID, "myDynamicElement"))
    #         )
    #     finally:
    #         self.driver.quit()

    def getElements(self, by, selector):
        return self.driver.find_elements(by, selector)

    def toCSV(self, data):
        pd.DataFrame(data).to_csv('hargaHotel.csv')


if __name__ == "__main__":

    scrapper = WebScrapper()
    scrapper.GetUrl(url)

    time.sleep(75)
    # nama_hotel = []
    harga_hotel = []
    header = scrapper.getElements(By.CLASS_NAME, "BgYkof")

    div = scrapper.getElements(By.CLASS_NAME, "kixHKb")

    # for h in header:
    #     print(h.text)
    #     nama_hotel.append(h.text)

    for i, d in enumerate(div):
        val = d.find_element(By.TAG_NAME, "span")
        if "IDR" in val.text.split():
            print(val.text)
            _, mun = val.text.split()

            harga_hotel.append(int(mun.replace(",", "")))

    # print(len(nama_hotel))
    arr = np.asarray(harga_hotel)
    scrapper.toCSV(arr)

    # data = scrapper.getElements(By.CLASS_NAME, "XrXoS")


# J2W8oe osw6J CiuVaf untuk nama dan review user
# J2W8oe PwV1Ac BIjKEe untuk harga
