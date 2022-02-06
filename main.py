# import frameworks
from aifc import Error
from asyncio import selector_events
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from soupsieve import select
from accounts import username,password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#defining functions
def get_page(page:str or tuple,i:int=0)->int:
    if type(page)==str:
        page=tuple_page(page)
    i+=1
    print("action to Login page : ",i)
    try : 
        driver.get(page[1])
        if page[0] not in str(driver.title) or driver.current_url!=page[1]:
            raise Error("Try again !!")
    except : 
        i=get_page(page,i)
    global lang
    lang=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"html"))).get_attribute("lang")
    return i
def sendding_data(username:str,password:str,i:int=0)->int:
    i+=1
    print("action to change password page : ",i)
    try :
        name_input=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "UserName")))

        name_input.clear()
        name_input.send_keys(username)
        
        password_input=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Password")))
        password_input.clear()
        password_input.send_keys(password)
    
        password_input.submit()
    except :
        i=sendding_data(username,password,i)
    if driver.title=="Login page"and driver.current_url==pages1["Login page"][0] and driver.find_element(By.ID,"MsgError").text :
        driver.quit()
        raise ValueError("your Log informition is wrong !!")
    if driver.title!="MassarService" :
        i=get_page("Login page",i)
        i=sendding_data(username,password,i)
    return i
def get_into_grades_page(i=0):
    i+=1
    print("action to get into grades pages : ",i)
    try :
        #WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.TAG_NAME,"a")))[1].click()
        div=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inner")))
        div.click()
        a_element=WebDriverWait(div,10).until(EC.presence_of_element_located((By.LINK_TEXT,key_words[lang][0])))
        a_element.click()
        a_element=WebDriverWait(div,10).until(EC.presence_of_element_located((By.LINK_TEXT,key_words[lang][1])))
        a_element.click()
        if driver.title!="MassarService" : 
            raise Error("try again !!")
    except :
        if driver.current_url==pages1["MassarService"][1]:
            driver.back()
            i=get_into_grades_page(i)
        if driver.current_url==pages1["Login page"][0]:
            i=sendding_data(username,password,i)
            i=get_into_grades_page(i)
    return i
def tuple_page(title:str,index=0)->tuple:
    return (title,pages1[title][index])
#global variabls
global driver,pages1,key_words
#getting data
pages1={"Login page":["https://moutamadris.men.gov.ma/moutamadris/Account"],"MassarService":["https://moutamadris.men.gov.ma/moutamadris/Account/ChangePassword","https://moutamadris.men.gov.ma/moutamadris/TuteurEleves/GetNotesEleve"]}
key_words={"ar":["التمدرس","تتبع النقط",["الدورة الأولى","الدورة الثانية","المعدل السنوي"]],"fr":["Scolarite","Mes notes",["Premiere semestre","Deuxième  semestre","Moyenne Annuelle"]]}
Path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(Path)
print("getting into Login page ...")
print("get into Login page after : ",get_page("Login page")," operation .")
print("getting into change password page ...")
print("get into change password page after : ",sendding_data(username,password)," operation .")
#get into my grades
#div=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"inner")))
#div.click()
#a_element=WebDriverWait(div,10).until(EC.presence_of_element_located((By.LINK_TEXT,key_words[lang][0])))
#a_element.click()
#a_element=WebDriverWait(div,10).until(EC.presence_of_element_located((By.LINK_TEXT,key_words[lang][1])))
#a_element.click()
#select_element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"SelectedSession")))
#select_element.send_keys(1)
print("getting into grades page ...")
print("get into grades page in : ",get_into_grades_page()," operation .")
input()    
driver.quit()
