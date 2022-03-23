import time
import requests
import a

a=time.perf_counter()


with open('links1.txt','r') as links:
    urls = links.read()
    urls = urls.split('\n')
    
    
   
    
   
    
#for i in range(len(urls[:1000])):
async def MT(url,i):
     image_bytes =requests.get(url).content
     #print((image_bytes))
     img_name =f'{i}.jpg'
     with open(img_name, 'wb') as img_file:
         #image_bytes =requests.get(urls[i]).content
         await img_file.write(image_bytes)
         print(f'{img_name} was downloaded...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(MT,urls[:10],range(10))

b=time.perf_counter()
print(f'{b-a} seconds')

