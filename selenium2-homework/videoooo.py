import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost:9999/videos.html')

try:
    def stop_and_go(ide):
        elem = driver.find_element_by_id(ide)
        elem.send_keys(Keys.SPACE)
        time.sleep(2.0)
        elem.send_keys(Keys.SPACE)


    stop_and_go('html5video')

    playpause = driver.find_element_by_xpath('/html/body/div/button[1]')
    playpause.click()
    time.sleep(2.0)
    playpause.click()

    stop_and_go('youtubeframe')
    #movie_player = driver.find_element_by_id('youtubeframe')
    #movie_player.send_keys(Keys.SPACE)
    #time.sleep(4.0)
    #movie_player.click()
    #time.sleep(3.0)


finally:
    driver.close()
