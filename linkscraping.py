from selenium import webdriver
import time
import concurrent.futures
from itertools import repeat

start = time.perf_counter()
search_terms = []

link_file = open("links1.txt", mode="a+")

def view_webpage(search_term):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser =  webdriver.Chrome('D:\GITREPO\Threading\chromedriver', options=options)
    url = "https://unsplash.com/search/photos/" + search_term
    browser.get(url)
    try:
        elem1 = browser.find_elements_by_class_name("YVj9w")
    except:
        print('some error occured')
    for i in range(len(elem1)):
        try:
            src = elem1[i].get_attribute('src')
            print(src, file=link_file)

        except Exception as e:
            print(e)




with concurrent.futures.ThreadPoolExecutor(6) as executor:
    executor.map(view_webpage,search_terms)

#[view_webpage(search_term ) for search_term in search_terms]
    
    
# Closing the file to save in drive
link_file.close()
end = time.perf_counter()
print(end-start)