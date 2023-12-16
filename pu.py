import time
#import os
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#s = Service(executable_path='/home/')  можно скачать самому драйвера для работы хрома соотвествующей версии
#driver = webdriver.Chrome(service=s) и указать это, у меня же автоматом подцепилось..
driver = webdriver.Chrome()

try:
    driver.maximize_window() #открываем окно максимально, что бы не мешала мобильная разметка
    driver.get("https://www.youtube.com/")
    #time.sleep(2)

    #gaming = driver.find_element(By.PARTIAL_LINK_TEXT, 'Gaming').click() # найти просто по тексту кнопки и кликнуть
    #time.sleep(2)


    search_box = driver.find_element("css selector", "input[id='search']") # 1 вариант по id, можно еще "#search" записать
    #search_box = driver.find_element(By.NAME, 'search_query') # 2 вариант по name=""
    #search_box = driver.find_element(By.CSS_SELECTOR, 'ytd-searchbox') # 3 вариант по class=""
    #search_box = driver.find_element(By.ID, 'search') # не заработало почему то
    #search_box.clear() #очищаем, вдруг что то уже было

    time.sleep(2)
    search_box.send_keys("бункерная крыса")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)
    a = 0
    for a in (range(0,5)):
        driver.execute_script("window.scrollBy(0,document.documentElement.scrollHeight)") # скролит 
        a = a + 1
        time.sleep(2)


    results = driver.find_elements("css selector", "yt-formatted-string[class='style-scope ytd-video-renderer']")
    with open("results.html", "w", encoding="utf-8") as file: # сохраняем в файл   
        for result in results:
            if result.text != '': #пустые строки элементы пропускаем
                href_value = result.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
                print(f' <a href="{href_value}"> {result.text} </a> \n')
                file.write(f' <a href="{href_value}"> {result.text} </a> </br>')



finally:
    # Закрытие браузера после завершения работы
    driver.close()
    driver.quit()
    

