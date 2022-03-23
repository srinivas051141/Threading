from selenium import webdriver
import requests
import time
import concurrent.futures


def view_webpage():
    try:
        elem1 = browser.find_elements_by_tag_name('a')
    except:
        print('some error occured')
    try:
        for elem in elem1:
            if elem.get_attribute('title') == 'Download photo':
                browser.get(elem.get_attribute('href'))
    except:
        print("No data in Element")
    

browser =  webdriver.Chrome('D:\GITREPO\Threading/chromedriver')
search_term = "bikes/"
url = "https://unsplash.com/search/photos/" + search_term
browser.get(url)
#view_webpage()

findclass = browser.find_elements_by_class_name("YVj9w")


for i in range(len(findclass)):
    try:
        src = findclass[i].get_attribute('src')
       
        img_bytes = requests.get(src).content
        img_name = "b"+ str(i)
        img_name = f'{img_name}.jpg'
        with open('img_name', 'wb') as img_file:
            img_file.write(img_bytes)
            print(f'{img_name} was downloaded...')

    except Exception as e:
        print(e)
       
        
#complete = False
# we will open the file in append mode
# link_file = open("links.txt", mode="a+")

# while not complete:
#     view_webpage(link_file)
#     complete = True
    
# # Closing the file to save in drive
# link_file.close()