import asyncio
import os
import django
from channels.layers import get_channel_layer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

django.setup()


async def main():
    channel_layer = get_channel_layer()

    messeage_dict = {'content' : 'world'}

    await channel_layer.send('hello', messeage_dict)
    
    response_dict = await channel_layer.receive('hello')
    is_equal = messeage_dict == response_dict
    print("송신/수신 데이터가 같습니까?", is_equal)


asyncio.run(main())
