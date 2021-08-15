def tes_con_multi_pages():

    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    input_data = ["testuser1", "testuser1@example.com", "Abcd123$"]
    page_counter = 2

    driver.get('http://localhost:1667/#/')

    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a').click()
    time.sleep(2)

    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(input_data[1])
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys(input_data[2])
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/button').click()
    time.sleep(2)

    articles = driver.find_elements_by_xpath('//a[@class="preview-link"]')
    if (len(articles)) <= 10:
        print('Nem all rendelkezesre elegendo tesztadat')
        driver.close()

    pages = driver.find_elements_by_xpath('//a[@class="page-link"]')

    for i in pages:
        i.click()
        time.sleep(2)

    assert len(pages) == page_counter

    driver.close()
