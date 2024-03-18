from random import choice, randint
from finance import Finance
from utilities import view_entries


def get_response(user_input: str, user_id: int) -> str:
    lowered: str = user_input.lower()

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
    elif 'inc' in lowered:
        try:
            lowered = lowered.split(' ')[1:]
            desc: str = lowered[0]
            amount: float = float(lowered[1])
            Finance().income(user_id, amount, desc)
        except ValueError as e:
            if str(e) == 'Snor... Description is too long':
                return e
            return 'Snor... the correct syntax is "!exp [desc] [amount]"'
        except Exception as e:
            return 'Snor... an error has occured"'
        return f'Your new balance is {Finance().get_balance(user_id)}'
    elif 'exp' in lowered:
        try:
            lowered = lowered.split(' ')[1:]
            desc: str = lowered[0]
            amount: float = float(lowered[1])
            Finance().expense(user_id, amount, desc)
        except ValueError as e:
            if str(e) == 'Snor... Description is too long':
                return e
            return 'Snor... the correct syntax is "!exp [desc] [amount]"'
        except Exception as e:
            return 'Snor... an error has occured"'
        return f'Your new balance is {Finance().get_balance(user_id)}'
    elif 'view' in lowered:
        entries: list = Finance().view_entries(user_id)
        return view_entries(entries)
    elif 'flip' in lowered:
        return choice(['Heads', 'Tails'])
    elif 'say' in lowered:
        return user_input.split(' ', 1)[1]
    else:
        return choice(['Snor?',
                       'Snor doesnt understand',
                       'Snor is confused',
                       'zzz... snor... zzz...',
                       'what did you say to me'
        ])