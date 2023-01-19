import io
import client
import asyncio
import sys

#'grep -c "henry" *.log', num=4

asyncio.get_event_loop().run_until_complete(client.main_logic('grep -c "IE" *.log', num=4))
