import base64
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ImageConsumer(WebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content, **kwargs):
        if content['command'] == "join_room":
            await self.channel_layer.group_add(content['room_code'], self.channel_name)

        elif content['command'] == "send_image":
            await self.channel_layer.group_send(content['room_code'], {
                "type": "image.data",
            })

    async def image_data(self, event):
        await self.send_json({
            "image_data": event["image_data"],
        })

