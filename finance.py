from data_util import load_json, save_json
from datetime import date

class Finance:
    def __init__(self) -> None:
        self.file_path: str = 'data/finance.json'
        self.data: list = load_json(self.file_path)
        self.balance: float = 0

    def get_balance(self, user_id: int) -> float:
        self.data = load_json(self.file_path)
        for entry in self.data:
            if int(entry['user']) == user_id:
                self.balance += float(entry['amount'])
        return self.balance
    
    def income(self, user_id: int, amount: float, desc: str) -> None:
        self.create_entry(user_id, amount, 'income', desc)

    def expense(self, user_id: int, amount: float, desc: str) -> None:
        self.create_entry(user_id, -amount, 'expense', desc)
    
    def create_entry(self, user_id: int, amount: float, category: str, desc: str) -> None:
        self.data : list = load_json(self.file_path)
        self.data.append({'id': len(self.data), 'user': user_id, 'date': str(date.today()), 'amount': str(amount), 'category': category, 'desc': desc})
        save_json(self.file_path, self.data)

    def view_entries(self, user_id: int) -> list:
        self.data : list = load_json(self.file_path)
        return [entry for entry in self.data if int(entry['user']) == user_id]