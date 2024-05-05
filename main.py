from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import finance_handler as fh
import asyncio

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

async def handle_message(message: Message, client: Client) -> None:
    if message.content.lower().startswith("!"):
        if message.content.lower().startswith("!exp"):
            await fh.handle_expense(message, client)
        elif message.content.lower().startswith("!inc"):
            await fh.handle_income(message, client)
        else:
            await send_message(message, client)

async def send_message(message: Message, client: Client) -> None:
    user_id: int = message.author.id
    user_message: str = message.content
    if is_private:= user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = await get_response(message, client)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')
    client.loop.create_task(heartbeat())

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    print(f'{[{channel}]} {username}: "{user_message}"')
    await handle_message(message, client)
    
async def heartbeat():
    channel = client.get_channel(1236567271720357950)
    if not channel:
        print(f"Channel with ID {1236567271720357950} not found.")
        return
    await client.wait_until_ready()
    while not client.is_closed():
        # Send a heartbeat every 30 seconds (adjust as needed)
        await asyncio.sleep(30)
        # Check if the client is connected
        latency = round(client.latency * 1000)
        try:
            # Send a heartbeat message to the channel
            await channel.send(f"Bot latency: {latency} ms")
            # Log heartbeat
            print("Heartbeat sent to channel")
        except Exception as e:
            print(f"Error sending heartbeat message: {e}")
    
def main() -> None:
    client.run(token = TOKEN)

if __name__ == '__main__':
    main()
