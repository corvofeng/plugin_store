
from plugins import register, Plugin, Event, logger, Reply, ReplyType

import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .db import WechatMessages


def save_item(engine, room_id, content, sender_id, sender_name, receiver_id, receiver_name, create_time):
    with engine.connect() as connection:
        with Session(connection) as session:
            wm = WechatMessages(
                    room_id=room_id or '',
                    content=content,
                    sender_id=sender_id,
                    sender_name=sender_name,
                    receiver_id=receiver_id,
                    receiver_name=receiver_name,
                    create_time=create_time
            )
            session.add(wm)
            session.commit()


@register
class Store(Plugin):
    name = "store"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.config:
            return

        self.engine = create_engine(
            self.config.get('mysql', {}).get('url', ''), echo=False,
            pool_pre_ping=True,
            connect_args={'connect_timeout': 10},
        )

    def did_receive_message(self, event: Event):
        msg = event.message
        # if not msg.room_id in self.config.get('record_room_id', []):
        #     return
        try:
            save_item(self.engine,
                msg.room_id, msg.content, msg.sender_id, msg.sender_name,
                msg.receiver_id, msg.receiver_name, msg.create_time)
        except Exception as e:
            logger.info("Can't save for", msg, e)

        # record = self.Records()
        # record.set('create_time', msg.create_time)
        # record.set('room_id', msg.room_id)
        # record.set('sender_id', msg.sender_id)
        # record.set('sender_name', msg.sender_name)
        # record.set('receiver_id', msg.receiver_id)
        # record.set('receiver_name', msg.receiver_name)
        # record.set('content', msg.content)
        # record.set('is_group', msg.is_group)
        # record.set('is_at', msg.is_at)
        # record.set('type', msg.type)
        # record.save()

    def will_generate_reply(self, event: Event):
        pass

    def will_decorate_reply(self, event: Event):
        pass

    def will_send_reply(self, event: Event):
        pass

    def help(self, **kwargs) -> str:
        return "Use the command #tiktok(or whatever you like set with command field in the config) to get a wonderful video"
