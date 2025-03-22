from selenium import webdriver


driver = webdriver.Firefox()

driver.get(https://www.goodreturns.in/gold-rates/)

container_price=driver.find_elements(By.XPATH,"//*[@class='gold-bottom']/p")

container_header = driver.find_elements(By.XPATH,"//*[@class='gold-top]")

data_dict={}
for head,val in zip(container_header,container_price):
    data_dict[head.text]=val.text
