import requests
import concurrent.futures
import asyncio
import aiohttp
import aiofiles

async def func():
        async with aiohttp.ClientSession() as session:
                image_bytes = await session.get('https://media.istockphoto.com/photos/generic-modern-suv-car-in-concrete-garage-picture-id1307086567?b=1&k=20&m=1307086567&s=170667a&w=0&h=NjcM6LIOkmfhyqH-zrbFU7pHCPxIABvNhWaOElm_P-E=')
                #print(image_bytes)
                img_name ='example.jpg'
                path = 'D:\GITREPO\Threading\example.jpg'
                async with aiofiles(path, 'wb') as img_file:
                        await img_file.write(await image_bytes.read())
                        print(f'{img_name} was downloaded...')

def tion():
        asyncio.run(func())   


if __name__ =='__main__':
        tion()             



