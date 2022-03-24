import pymongo
import gridfs
import time
import requests
import concurrent.futures

a=time.perf_counter()

client = pymongo.MongoClient("mongodb://localhost:27017/")

database = client['Images']
fs = gridfs.GridFS(database,collection='Multi_Processing')


with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')


#for i in range(len(urls[:1000])):
def MP(url,i):
    image_bytes =requests.get(url).content
    #print((image_bytes))
    img_name =f'{i}.jpg'
    fs.put(image_bytes,filename =img_name)
    print (f'{img_name} is uploaded.')


if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(MP,urls[:10],range(10))

    b=time.perf_counter()
    print(f'{b-a} seconds')


