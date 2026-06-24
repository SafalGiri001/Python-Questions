def create_user(username, email, password,
                is_active = True,
                is_admin = False,
                country = 'Nepal'):
    user = {
        'username' : username,
        'email' : email,
        'is_active' : is_active,
        'is_admin' : is_admin,
        'country' : country
    }
    return user

new_user = create_user (
    username = 'ram kc',
    email = 'abc123@gmail.com',
    password = '1234abc',
    country = "Canada"
)
print(new_user)
