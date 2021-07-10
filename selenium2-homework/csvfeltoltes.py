import csv
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/another_form.html')


def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


with open('table_in.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)
        find_and_clear_by_id('fullname').send_keys(row[0])
        find_and_clear_by_id('email').send_keys(row[1])
        find_and_clear_by_id('dob').send_keys(row[2])
        find_and_clear_by_id('phone').send_keys(row[3])

        driver.find_element_by_id('submit').click()
        time.sleep(1.0)

link = driver.find_element_by_xpath('//button[text()="Export HTML table to CSV file"]')
link.click()
driver.close()
with open('c:\\users\\dell\\downloads\\table.csv') as csvfile_new:
    csvreader_new = csv.reader(csvfile_new, delimiter=',')
assert csvreader == csvreader_new
print('nincs egyezes')


print('ok')




