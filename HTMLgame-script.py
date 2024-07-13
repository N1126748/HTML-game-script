from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# service  = Service(executable_path='')
driver = webdriver.Chrome()

driver.get('https://orteil.dashnet.org/cookieclicker/')

productPricePrefix = 'productPrice'
productPrefix = 'product'

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'langSelect-ZH-CN'))
)

click_element = driver.find_element(By.ID, 'langSelect-ZH-CN')
click_element.click()
driver.implicitly_wait(1.5)

click_element = driver.find_element(By.ID, 'bigCookie')

while True:
    click_element.click()
    click_count = driver.find_element(By.ID, 'cookies').text.split(' ')[0]
    click_count = int(click_count.replace(',',''))

    for i in range(4):
        productPrice = driver.find_element(By.ID, productPricePrefix + str(i)).text.replace(',','')

        if not productPrice.isdigit():
            continue

        productPrice = int(productPrice)

        if click_count >= productPrice:
            product = driver.find_element(By.ID, productPrefix + str(i))
            product.click()
            break

driver.quit()