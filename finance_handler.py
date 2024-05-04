import asyncio
from discord import Message, Client
from finance import Finance



async def handle_expense(message: Message, client: Client) -> None:
    if message.content.lower().startswith("!exp"):        
        category_message = await message.channel.send(print_categories())

        for emoji in get_emoji():  
            await category_message.add_reaction(emoji)

        def reaction_check(reaction, user):
            return user == message.author and reaction.message.id == category_message.id

        try:
            reaction, _ = await client.wait_for('reaction_add', timeout=60.0, check=reaction_check)
            categories = ['Food', 'Transport', 'Fun', 'Miscellaneous']
            chosen_category = categories[get_emoji().index(reaction.emoji)]
            print(reaction.emoji)
        except asyncio.TimeoutError:
            await message.channel.send("You took too long to choose a category. Please try again.")
            return

        await message.channel.send("Please provide the amount:")

        def amount_check(m):
            return m.author == message.author and m.content.replace('.', '', 1).isdigit()

        try:
            amount_message = await client.wait_for("message", check=amount_check, timeout=60.0)
            amount = float(amount_message.content)
        except asyncio.TimeoutError:
            await message.channel.send("You took too long to provide the amount. Please try again.")
            return
        except ValueError:
            await message.channel.send("Invalid amount. Please provide a valid number.")
            return

        try:
            Finance().expense(message.author.id, amount, reaction.emoji)
            await message.channel.send(f"Expense of {amount} in category {chosen_category} added.")
        except Exception as e:
            await message.channel.send("An error occurred while processing. Please try again later.")
            print(e)


async def handle_income(message: Message, client: Client) -> None:
    if message.content.lower().startswith("!inc"):
        await message.channel.send("Please provide the amount:")

        def amount_check(m):
            return m.author == message.author and m.content.replace('.', '', 1).isdigit()

        try:
            amount_message = await client.wait_for("message", check=amount_check, timeout=60.0)
            amount = float(amount_message.content)
        except asyncio.TimeoutError:
            await message.channel.send("You took too long to provide the amount. Please try again.")
            return
        except ValueError:
            await message.channel.send("Invalid amount. Please provide a valid number.")
            return

        try:
            Finance().income(message.author.id, amount, '💰')
            await message.channel.send(f"Income of {amount} added.")
        except Exception as e:
            await message.channel.send("An error occurred while processing. Please try again later.")
            print(e)

def print_categories() -> str:
    out: str = '```'
    for i, choice in enumerate(get_categories()):
        out += f'{i + 1}. {choice}\n'
    out += '```'
    return out

def get_categories() -> list:
    return ['Food', 'Transport', 'Fun', 'Miscellaneous']
    

def get_emoji() -> list:
    return['🍳', '🚙', '🎉', '💡']

