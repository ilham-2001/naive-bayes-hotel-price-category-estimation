from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

url = "https://www.google.com/travel/hotels/Yogyakarta%2C%20Yogyakarta%20City%2C%20Special%20Region%20of%20Yogyakarta?q=harga%20hotel%20di%20jogja&g2lb=2502548%2C2503771%2C2503781%2C4258168%2C4270442%2C4284970%2C4291517%2C4306835%2C4308226%2C4515404%2C4597339%2C4649665%2C4703207%2C4718358%2C4722900%2C4723331%2C4741665%2C4757164%2C4758493%2C4762561%2C4779784%2C4786958%2C4787395%2C4790928%2C4794648&hl=en-ID&gl=id&ssta=1&ts=CAESCgoCCAMKAggDEAAaXQo_Ejs6OVlvZ3lha2FydGEsIFlvZ3lha2FydGEgQ2l0eSwgU3BlY2lhbCBSZWdpb24gb2YgWW9neWFrYXJ0YRoAEhoSFAoHCOYPEAcYHBIHCOYPEAcYHRgBMgIQACoOCgoSAQMoAToDSURSGgA&rp=ogE5WW9neWFrYXJ0YSwgWW9neWFrYXJ0YSBDaXR5LCBTcGVjaWFsIFJlZ2lvbiBvZiBZb2d5YWthcnRhOAFAAEgC&ap=SAAwAVqpAgoGCIDqMBAAIgNJRFIqFgoHCOYPEAcYHBIHCOYPEAcYHRgBKACwAQBYAWgBcgQIAhgAmgE7EjlZb2d5YWthcnRhLCBZb2d5YWthcnRhIENpdHksIFNwZWNpYWwgUmVnaW9uIG9mIFlvZ3lha2FydGGiARcKCS9tLzBkZzZ5eBIKWW9neWFrYXJ0YaoBGwoCCCESAghlEgIIFRICCGcSAwiOARICCC8YAaoBBwoDCOUBGACqAQcKAwjhARgAqgEHCgMI5AEYAKoBBwoDCOIBGACqAQwKAwiuARIDCLIBGAGqAQsKAwjhAhICCGMYAaoBBwoDCOYBGACSAgIIEpICAggTkgICCBGSAgIIEJICAggPkgICCA6SAgIIDZICAggMkgICCBSSAQIgAWgA&ictx=1&utm_campaign=sharing&utm_medium=link&utm_source=htls&ved=0CAAQ5JsGahcKEwjos5mBjfH4AhUAAAAAHQAAAAAQBA"
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
        # browser = webdriver.Chrome(executable_path="chromedriver_linux64/chromedriver")
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        browser.get(url)

        header = browser.find_elements(By.CLASS_NAME, "BgYkof")
        div = browser.find_elements(By.CLASS_NAME, "kixHKb")

        for h in header:
            print(h.text)

        for d in div:
            val = d.find_element(By.TAG_NAME, "span")
            if "IDR" in val.text.split():
                print(val.text)

        time.sleep(10)
