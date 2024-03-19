
import bs4
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
# doc = requests.get('https://ncert.nic.in/textbook.php').text

# soup = BeautifulSoup(doc, 'html.parser')
# e = soup.select_one('document.test.tclass')
# print(e)

driver = webdriver.Firefox()

driver.get("https://ncert.nic.in/textbook.php")


all_classes = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tclass")
driver.execute_script(f'document.test.tclass.selectedIndex = {input("enter class index")};')
driver.execute_script('change();')

all_subjects = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tsubject")
driver.execute_script(f'document.test.tsubject.selectedIndex = {input("enter subject index")};')
driver.execute_script('change1(document.test.tsubject.selectedIndex);')

all_books = selenium.webdriver.remote.webelement.WebElement = driver.find_element(By.NAME, "tbook")
driver.execute_script(f'document.test.tbook.selectedIndex = {input("enter book name index")};')

out = driver.execute_script('return document.test.tbook.options[document.test.tbook.options.selectedIndex].value;')
print(out)

print(all_classes.text.splitlines())
print(all_subjects.text)
print(all_books.text)
driver.quit()