def account(balance):
    current_balance = balance
    def with_draw(amount):
        nonlocal balance
        if balance <= amount:
            balance = balance - amount
            return f'remaining balance: {balance} and with draw amount : {amount}'
        else:
            return 'insufficient fundd'
    return with_draw
user_ram = account(500)
user_hari = account(1000)
print(user_hari(30))
print(user_ram(50))
print(user_ram.__closure__[0].call_contents)