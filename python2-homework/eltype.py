

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


try:
    driver.get("http://localhost:9999/trickyelements.html")

    element1 = driver.find_element_by_id('element1')
    element2 = driver.find_element_by_id('element2')
    element3 = driver.find_element_by_id('element3')
    element4 = driver.find_element_by_id('element4')
    element5 = driver.find_element_by_id('element5')

    elements = [element1, element2, element3, element4,element5]
    for element in elements:
        if element.get_attribute()

finally:
    driver.close()