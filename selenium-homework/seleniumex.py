from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://jofogas.hu')


q = driver.find_element_by_id('q')
q.send_keys('laptop')




"""def search(font_type):
    try:
        q = driver.find_element_by_id(font_type)
    except:
        print("Nincs az oldalon ilyen elem.")
    finally:
        driver.close()

keres = 'nemletezik'
search(keres)


# font keresés hibakezeléssel kiegészítve

def search2(font_type):
    try:
        q = driver.find_element_by_id('mat-input-0')
        q.send_keys(font_type)
        submit = driver.find_element_by_xpath(f"//h1[contains(text(),'{font_type}')]")
        submit.click()
        print("A keresés sikeres, az oldal megnyitva!")
    except:
        print("Nincs az oldalon ilyen elem.")
    finally:
        driver.close()

font = input("Milyen nevű fontot keresel? (pl. Asul?) ")"""
