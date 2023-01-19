import asyncio
import websockets
import subprocess
import os

async def recv_msg(websocket):
    recv_text = await websocket.recv()
    print('Message received from,', websocket.remote_address[0])
    if 'grep' == recv_text[0:4]:
        ms = 'grep -H' + recv_text[4:]
        out_bytes = subprocess.check_output(ms, shell=True, universal_newlines=True)
        await websocket.send(out_bytes)
    else:
        await websocket.send(recv_text)
        

async def main_logic(websocket, path):
    await recv_msg(websocket)

start_server = websockets.serve(main_logic, '0.0.0.0', 9001)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
