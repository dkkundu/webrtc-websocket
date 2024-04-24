from channels.generic.websocket import AsyncJsonWebsocketConsumer


class WebRtcConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content, **kwargs):
        if content['command'] == "join_room":
            await self.channel_layer.group_add(content['room_id'], self.channel_name)
        elif content['command'] == "join":
            await self.channel_layer.group_send(content['room_id'], {
                "type": "join.messages",
            })

        elif content['command'] == "offer":
            await self.channel_layer.group_send(content['room_id'], {
                "type": "offer.messages",
                "offer": content['offer']
            })

        elif content['command'] == "answer":
            await self.channel_layer.group_send(content['room_id'], {
                "type": "answer.messages",
                "answer": content['answer']
            })

        elif content['command'] == "candidate":
            await self.channel_layer.group_send(content['room_id'], {
                "type": "candidate.messages",
                "candidate": content['candidate'],
                'iscreated': content['iscreated']
            })

    async def join_messages(self, event):
        await self.send_json({
            "command": "join",
        })

    async def offer_messages(self, event):
        await self.send_json({
            "command": "offer",
            "offer": event["offer"]
        })

    async def answer_messages(self, event):
        await self.send_json({
            "command": "answer",
            "answer": event["answer"]
        })

    async def candidate_messages(self, event):
        await self.send_json({
            "command": "candidate",
            "candidate": event["candidate"],
            "iscreated": event["iscreated"]
        })

