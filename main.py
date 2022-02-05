# import frameworks
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from accounts import username,password

#beautiful soup
def get_page(page:str or tuple,i:int=0)->int:
    if type(page)==str:
        page=tuple_page(page)
    i+=1
    print("action to Login page : ",i)
    try : 
        driver.get(page[1])
        if page[0] not in str(driver.title) or driver.current_url!=page[1]:
            raise ValueError("Try again !!")
    except : 
        i=get_page(page,i)
    return i
def sendding_data(username:str,password:str,i:int=0)->int:
    i+=1
    print("action to change password page : ",i)
    try :
        name_input=driver.find_element(By.ID,"UserName")
        name_input.send_keys(username)
        
        password_input=driver.find_element(By.ID,"Password")
        password_input.send_keys(password)
    
        password_input.submit()
    except :
        i=sendding_data(username,password,i)
    if driver.title=="Login page"and driver.current_url==pages1["Login page"] and driver.find_element(By.ID,"MsgError").text :
        driver.quit()
        raise ValueError("your Log informition is wrong !!")
    if driver.title!="MassarService" :
        i=get_page("Login page",i)
        i=sendding_data(username,password,i)
    return i
def tuple_page(title:str)->tuple:
    return (title,pages1[title])
#global variabls
global driver,pages1
#getting data
pages1={"Login page":"https://moutamadris.men.gov.ma/moutamadris/Account","MassarService":"https://moutamadris.men.gov.ma/moutamadris/Account/ChangePassword"}
Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)
print("getting into Login page ...")
print("get into Login page after : ",get_page("Login page")," operation .")
print("getting into change password page ...")
print("get into change password page after : ",sendding_data(username,password)," operation .")
input()
driver.quit()
