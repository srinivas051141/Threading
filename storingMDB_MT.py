import time
import requests
import concurrent.futures
import pymongo
import gridfs

a=time.perf_counter()

client =pymongo.MongoClient("mongodb://localhost:27017/")

database = client['Images']
fs = gridfs.GridFS(database,collection='Multi_Threading')

with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')
    
   
#for i in range(len(urls[:1000])):
def MT(url,i):
     image_bytes =requests.get(url).content
     #print((image_bytes))
     img_name =f'{i}.jpg'
     fs.put(image_bytes, filename =img_name)
     print(f'{img_name} is uploaded.')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(MT,urls[:1000],range(1000))

b=time.perf_counter()
print(f'{b-a} seconds')
