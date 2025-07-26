
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from time import sleep


chromedriver_autoinstaller.install()

driver=webdriver.Chrome()
driver.maximize_window()

url='https://www.lcw.com/'
driver.get(url)
sleep(3)
driver.find_element(By.ID,'cookieseal-banner-accept').click()
sleep(2)
search_box=driver.find_element(By.ID,'search-form__input-field__search-input')
input_search=input('What you call: ')
search_box.send_keys(f'{input_search}')
sleep(1)
search_box.send_keys(Keys.ENTER)
sleep(1)
how_many_products=int(input('How many get products: '))

list_product=[]
for i in range(1,how_many_products+1):
    product_name=driver.find_element(By.XPATH,f'/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[{i}]/a/div[2]/h5[2]').text
    product_price = driver.find_element(By.XPATH,f'/html/body/div[2]/div/div[2]/div/div[5]/div/div[2]/div[{i}]/a/div[2]/div[2]/div/span').text
    name_price=f'{i})Product Name: {product_name}--->{product_price}'
    sleep(1)
    list_product.append(name_price)

with open('productsfile.txt','w') as f:
    for item in list_product:
        f.write(f'{item}\n')


sleep(5)
driver.quit()






