import pymongo
import time
import gridfs
from PIL import Image, ImageFilter
import asyncio

size= (1200,1200)
a = time.perf_counter()

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client['Images']
fs = gridfs.GridFS(database,collection='Multi_Processing')

with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')


async def retrieve_async(i):
    img_name =f'{i}.jpg'
    file = fs.find_one({'filename' : img_name})
    image =  file.read()
    async with open(img_name, 'wb') as img_file:
         #image_bytes =requests.get(urls[i]).content
         await img_file.write(image)
         print(f'{img_name} was downloaded...')
         
    img =  await Image.open(img_name)
    img = await  img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'{img_name}')
    print(f'{img_name} was processed...')

async def main():
        tasks =[asyncio.create_task(retrieve_async(i)) for i in range(100)]
        # task1 = asyncio.create_task(func('ex1.jpg'))
        # task2 = asyncio.create_task(func('ex2.jpg'))
        await asyncio.gather(*tasks) 

asyncio.run(main())
b= time.perf_counter()
print(f'{b-a} seconds')