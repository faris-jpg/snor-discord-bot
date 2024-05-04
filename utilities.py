from datetime import datetime
import asyncio
from discord import Message

# async def remind(time: str, desc: str, message: Message) -> str:
#     unit: str = time[-1]
#     duration: float = time[0]
#     if unit.lower() not in ['s', 'm', 'h', 'd']:
#         raise ValueError
#     await message.channel.send(f'Timer set for {duration}{unit}.')
#     if unit == 's':
#         await asyncio.sleep()
#     elif unit == 'm':
#         await asyncio.sleep(duration * 60)
#     elif unit == 'h':
#         await asyncio.sleep(duration * 60 * 60)
#     elif unit == 'd':
#         await asyncio.sleep(duration * 60 * 60 * 24)
    
#     await f'Timer complete. {duration}{unit} has passed.'


def format_list(entries: list) -> str:
    balance: float = 0
    out : str = '```'
    out += f'{"+/- "} {"Date":<9} {"Desc":<8}  {"Amount":<8}\n'
    for entry in entries:
        date_confirm = datetime.strptime(entry['date'], '%Y-%m-%d')
        formatted = date_confirm.strftime('%d/%m/%y')
        out += '[' + ('+' if entry['category'] == 'income' else '-') + ']  '
        out += f'{formatted:<10}'
        out += entry['desc'] + ''.join(' ' for i in range(8))
        out += f'{abs(float(entry["amount"])):<10.2f}\n'
        balance += float(entry['amount'])
    out += '-' * 37
    out += '\nBalance:' + ' ' * 17 +  f'{balance:.2f}'
    out += '```'

    return out


