import aiohttp
import asyncio


async def call_async_api(input_dict):
    async with aiohttp.ClientSession() as session:
        url = f'http://localhost:8080/async-expand-reduce?input_dict={input_dict}'
        async with session.get(url) as response:
            return await response.json()


async def main():
    result = await call_async_api("1:2,3:4,5:6,7:8")
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
