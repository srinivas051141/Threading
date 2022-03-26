import pymongo
import time
import gridfs
from PIL import Image, ImageFilter
import concurrent.futures

size= (1200,1200)
a = time.perf_counter()

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['Images']
fs = gridfs.GridFS(database,collection='Multi_Processing')

with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')


def retrieve_MP(i):
    img_name =f'{i}.jpg'
    file = fs.find_one({'filename' : img_name})
    image = file.read()
    with open(img_name, 'wb') as img_file:
         #image_bytes =requests.get(urls[i]).content
         img_file.write(image)
         print(f'{img_name} was downloaded...')
         
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'{img_name}')
    print(f'{img_name} was processed...')

if __name__ == '__main__':

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(retrieve_MP,range(1000))


    b= time.perf_counter()
    print(f'{b-a} seconds')