from random import choice, randint
from finance import Finance
from utilities import format_list
from discord import Message, Client


async def get_response(message: Message, client: Client) -> str:
    lowered: str = message.content.lower()
    user_id: int = message.author.id
    
    if lowered[0] != '!':
        raise ValueError('Snor not found')
    if 'hello' in lowered:
        return 'Snor!'
    elif 'goodbye' in lowered:
        return 'Snor...'
    elif 'roll dice' in lowered:
        return f'Snor: {randint(1, 6)}'
    elif 'get_id' in lowered:
        return f'Your ID is {user_id}'
    elif 'bal' in lowered:
        return f'Your balance is {Finance().get_balance(user_id)}'
    elif 'view' in lowered:
        entries: list = Finance().view_entries(user_id)
        return format_list(entries)
    elif 'flip' in lowered:
        return choice(['Heads', 'Tails'])
    else:
        return choice(['Snor?',
                       'Snor doesnt understand',
                       'Snor is confused',
                       'zzz... snor... zzz...',
                       'what did you say to me'
        ])