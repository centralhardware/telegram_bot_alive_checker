import json
import logging
import os
from json.decoder import JSONDecodeError

from aiohttp import web
from telethon.sync import TelegramClient

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
telephone = os.getenv('TELEPHONE')
client = TelegramClient('alex', api_id, api_hash)


async def handle_post(request):
    body = await request.text()
    if not body:
        return web.Response(status=422, body='emtpy body')
    try:
        data = json.loads(body)
        logging.info(data['username'])
        logging.info(data['text'])
        await client.send_message(data['username'], data['text'])
    except JSONDecodeError:
        return web.Response(status=422, body='invalid json')
    except KeyError:
        return web.Response(status=422, body='mission required param username')
    return web.Response(status=200, body='ok')


async def handle_get(request):
    try:
        username = request.query['username']
        text = request.query['text']
    except KeyError:
        return web.Response(status=422, body='mission required param username/text')
    if not username:
        return web.Response(status=422, body='username param can not be empty')
    if not text:
        return web.Response(status=422, body='text param can not be empty')
    logging.info(username)
    logging.info(text)
    await client.send_message(username, text)
    return web.Response(status=200, body='ok')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('start application')

    client.connect()
    client.start(phone=telephone)
    app = web.Application()
    app.add_routes([web.post('/', handle_post),
                    web.get('/', handle_get)])
    web.run_app(app, port=8080)
    client.disconnect()
