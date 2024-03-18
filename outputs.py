from datetime import datetime

def view_entries(entries: list) -> str:
    out : str = '```'
    out += f'{"+/- "} {"Date":<10} {"Desc":<10} {"Amount":<10}\n'
    for entry in entries:
        date_confirm = datetime.strptime(entry['date'], '%Y-%m-%d')
        formatted = date_confirm.strftime('%d/%m/%y')
        out += '[' + ('+' if entry['category'] == 'income' else '-') + ']  '
        out += f'{formatted:<10} {entry["desc"]:<10} {abs(float(entry["amount"])):<10.2f}\n'
    out += '```'
    return out
    
