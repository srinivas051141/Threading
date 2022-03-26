import time
import requests
import pymongo
import gridfs

a=time.perf_counter()

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['Images']
fs = gridfs.GridFS(database,collection='For_loop')




with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')
        
    
for i in range(len(urls[1000:1001])):
     image_bytes =requests.get(urls[i]).content
     #print((image_bytes))
     img_name =f'{i}.jpg'
     

     fs.put(image_bytes, filename =img_name)
     print(f'{img_name} is uploaded.')
     

b=time.perf_counter()
print(f'{b-a} seconds')
# file = fs.find_one({'filename': 'img_name'})
# image = file.read()
# img_name ='1.jpg'
# with open(img_name, 'wb') as img_file:
#         #image_bytes =requests.get(urls[i]).content
#         img_file.write(image)
#         print(f'{img_name} was downloaded...')

