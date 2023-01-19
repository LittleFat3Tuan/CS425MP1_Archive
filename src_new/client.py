import asyncio
import websockets
async def send_msg(websocket, _text):
    #_text = input("please enter your context: ")
    if _text == "exit":
        print(f'you have enter "exit", goodbye')
        await websocket.close(reason="user exit")
        return False
    await websocket.send(_text)
    recv_text = await websocket.recv()
    print(f"{recv_text}")
    return int(recv_text.split(":")[1])

    
async def main_logic(command=None, num=10):
    total_Count = 0
    if not command:
        command = input("please enter your command:")
    ipAddress = open("../ipAdressess.txt")
    ipFile = ipAddress.readlines()
    for n, i in enumerate(ipFile):
        address = i.split(" ")[1].strip()
        ip="ws://"+address+":9001"
        try:
            async with websockets.connect(ip) as websocket:
               result =  await send_msg(websocket, command)
               total_Count += result
        except:
            pass
        if n >= num-1:
            break
    ipAddress.close()
    return total_Count
if __name__ == '__main__':
    total_Count = asyncio.get_event_loop().run_until_complete(main_logic())
    print("In total:"+str(total_Count))
