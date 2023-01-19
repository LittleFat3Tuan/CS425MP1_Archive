import io
import client
import asyncio
import sys


asyncio.get_event_loop().run_until_complete(client.main_logic('grep -Ec "[1-9]+\.[1-9]+\.[1-9]+\.[1-9]+" *.log', num=4))
