from regex import B
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np

url = "https://www.google.com/travel/hotels?q=harga%20hotel%20di%20jakarta&gsas=1&rp=CgpYAGAAcgQIAhgAOAGKAhZoYXJnYSBob3RlbCBkaSBqYWthcnRhqAIA&ved=0CAAQ5JsGahcKEwj467eKiPf4AhUAAAAAHQAAAAAQBA&hl=en-ID&gl=id&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4308226%2C4515404%2C4597339%2C4649665%2C4703207%2C4718358%2C4722900%2C4723331%2C4741665%2C4757164%2C4758493%2C4762561%2C4779784%2C4786958%2C4787395%2C4790928%2C4794648&utm_campaign=sharing&utm_medium=link&utm_source=htls&ts=CAESCgoCCAMKAggDEAAaKwoNEgk6B0pha2FydGEaABIaEhQKBwjmDxAHGBsSBwjmDxAHGBwYATICEAAqDgoKEgECKAE6A0lEUhoA&ap=MAFaowMKBgiA6jAQACIDSURSKhYKBwjmDxAHGBsSBwjmDxAHGBwYASgAsAEAWAFgAGgBcgQIAhgAmgEJEgdKYWthcnRhogETCggvbS8wNDRydhIHSmFrYXJ0YaoBLwoCCCESAggIEgIIZRICCBUSAggNEgIIZxICCFsSAggvEgIIWhIDCIwCEgIIIBgBqgEHCgMI5QEYAKoBEwoCCBISAwibARICCGgSAghpGAGqAQcKAwjhARgAqgEHCgMIoQIYAKoBBwoDCOQBGACqAQ4KAggcEgIIURICCEcYAaoBBwoDCOIBGACqARMKAgglEgMI2wISAgh1EgIIdhgBqgESCgIIERICCEASAgg4EgIIAhgBqgEHCgMIxQIYAKoBLQoCCC4SAgg8EgMIhwESAggaEgIISBIDCIECEgIIAxICCAwSAwiPARICCCcYAaoBDAoDCK4BEgMIrwEYAaoBCwoDCOECEgIIYxgBqgELCgIINRIDCJYBGAGSAgIIEpICAggRkgICCA6SAgIIE5ICAggMkgICCBCSAgIID5ICAggNkgICCBSSAQIgAQ"
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

    def getElement(self, by, selector):
        return self.driver.find_element(by, selector)

    def toCSV(self, data):
        pd.DataFrame(data).to_csv('harga_hotel_jakarta.csv')


if __name__ == "__main__":

    scrapper = WebScrapper()
    scrapper.GetUrl(url)

    time.sleep(35)
    hotel = []

    cards = scrapper.getElements(By.CLASS_NAME, "pjDrrc")

    for card in cards:
        element1 = card.find_element(By.CLASS_NAME, "yhIjlf")
        element2 = element1.find_element(By.CLASS_NAME, "kCsInf")
        element3 = element2.find_element(By.CLASS_NAME, "XrXoS")

        # left hand side
        lhs1 = element3.find_element(By.CLASS_NAME, "osw6J")
        # top side
        top_lhs1 = lhs1.find_element(By.CLASS_NAME, "jVsyI")

        # mencoba mengambil nama hotel
        title_hotel = lhs1.find_element(By.CLASS_NAME, "QT7m7")
        nama_hotel = title_hotel.find_element(
            By.TAG_NAME, "h2")  # ambil nama hotel

        # mencoba mengambil rating user
        try:
            rating_hotel = top_lhs1.find_element(By.CLASS_NAME, "FW82K")
            rating_hotel_inner1 = rating_hotel.find_element(
                By.CLASS_NAME, "nlwZxb")
            rating_hotel_inner2 = rating_hotel_inner1.find_element(
                By.CLASS_NAME, "spNMC")
            rating_hotel_inner3 = rating_hotel_inner2.find_element(
                By.CLASS_NAME, "sSHqwe")
            rating_hotel_inner4 = rating_hotel_inner3.find_element(
                By.CLASS_NAME, "UVHlBc")
            rating_hotel_inner5 = rating_hotel_inner4.find_element(
                By.CLASS_NAME, "kixHKb")
            user_rate = rating_hotel_inner5.find_element(
                By.CLASS_NAME, "KFi5wf")

            # mencoba mengambil jumlah rater hotel
            rater_count = rating_hotel_inner4.find_element(
                By.CLASS_NAME, "jdzyld")

            user_rate = user_rate.text
            rater_count = rater_count.text
        except Exception:
            user_rate = "-"
            rater_count = "-"

        # bottom side ED0Ckc
        bottom_lhs1 = lhs1.find_element(By.CLASS_NAME, "RJM8Kc")
        bottom_lhs2 = bottom_lhs1.find_element(By.CLASS_NAME, "ED0Ckc")
        bottom_lhs3 = bottom_lhs2.find_element(By.CLASS_NAME, "HlxIlc")
        fasilitas = bottom_lhs3.find_elements(By.TAG_NAME, "li")

        facility = []

        for fasil in fasilitas:
            facility.append(fasil.text)

        # right hand side
        rhs1 = element3.find_element(By.CLASS_NAME, "PwV1Ac")
        try:
            rhs2 = rhs1.find_element(By.CLASS_NAME, "OxGZuc")
            harga = rhs2.find_element(By.TAG_NAME, "span")
            harga = harga.text
        except Exception:
            harga = 0

        hotel.append((nama_hotel.text, user_rate,
                     rater_count, str(facility), harga))

    # for i, d in enumerate(div):
    #     val = d.find_element(By.TAG_NAME, "span")
    #     if "IDR" in val.text.split():
    #         print(val.text)
    #         _, mun = val.text.split()

    #         harga_hotel.append(int(mun.replace(",", "")))

    arr = np.asarray(hotel)
    scrapper.toCSV(arr)

    # data = scrapper.getElements(By.CLASS_NAME, "XrXoS")


# J2W8oe osw6J CiuVaf untuk nama dan review user
# J2W8oe PwV1Ac BIjKEe untuk harga
