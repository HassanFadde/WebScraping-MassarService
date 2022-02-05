from turtle import title
from selenium import webdriver

def get_page(page:tuple,driver:webdriver,i:int=0)->int:
    i+=1
    try : 
        driver.get(page[1])
        if page[0] not in str(driver.title):
          raise ValueError("I'll try again !!")
    except : 
        i=get_page(page,driver,i)
    return i

pages=[("Login page","https://moutamadris.men.gov.ma/moutamadris")]
Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)
print(get_page(pages[0],driver))
input()
driver.quit()