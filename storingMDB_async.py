import time
import asyncio
import aiohttp
#import aiofiles
import pymongo
import gridfs

a=time.perf_counter()

client =pymongo.MongoClient("mongodb://localhost:27017/")
database = client['Images']
fs =gridfs.GridFS(database,collection = 'asyncio')




with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')

async def func(urls,i):
        async with aiohttp.ClientSession(trust_env=True) as session:
                async with session.get(urls[i]) as resp:

               #print(image_bytes)
                #img_name ='example.jpg'
                        img_name =f'{i}.jpg'
                        resp = await resp.read()
                        #path = f'D:\GITREPO\Threading\{img_name}'
                        #f =await  aiofiles.open(path, 'wb') 
                        fs.put( resp, filename=img_name)
                        print(f'{img_name} was uploaded...')
                        #await f.close()

async def main():
        tasks =[asyncio.create_task(func(urls,i)) for i in range(1000)]
        # task1 = asyncio.create_task(func('ex1.jpg'))
        # task2 = asyncio.create_task(func('ex2.jpg'))
        await asyncio.gather(*tasks) 


asyncio.run(main())
b = time.perf_counter()
print(f'{b-a} seconds')   


#if __name__ =='__main__':
 #       tion()             



