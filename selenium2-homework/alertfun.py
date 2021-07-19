import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)  # headless
driver = webdriver.Chrome(ChromeDriverManager().install())
try:
    driver.get('http://localhost:9999/alert_playground.html')
    driver.find_element_by_name('alert').click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()


    driver.find_element_by_name('confirmation').click()
    time.sleep(2)
    alert_2 = driver.switch_to.alert
    time.sleep(2)
    alert_2.accept()

    driver.find_element_by_name('prompt').click()
    alert_3 = driver.switch_to.alert
    alert_3.send_keys('kiskutya')

    time.sleep(2)
    alert_3.accept()
    ref_text = driver.find_element_by_id('demo').text
    assert(alert_3.text == f'You entered: {ref_text}')
    print(ref_text)
    alert_3.accept()









finally:
    pass
    time.sleep(2)
    driver.quit()