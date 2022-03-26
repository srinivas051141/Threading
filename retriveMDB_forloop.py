import pymongo
import time
import gridfs


a = time.perf_counter()

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['Images']
fs = gridfs.GridFS(database,collection='Multi_Processing')

with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')


for i in range(len(urls[:2])):
    img_name =f'{i}.jpg'
    file = fs.find_one({'filename' : img_name})
    image = file.read()
    with open(img_name, 'wb') as img_file:
         #image_bytes =requests.get(urls[i]).content
         img_file.write(image)
         print(f'{img_name} was downloaded...')

#file = fs.find_one({'filename': 'img_name'})
# image = file.read()
# 
# 
