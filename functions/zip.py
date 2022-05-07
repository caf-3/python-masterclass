usernames = ['Dude', 'Bro', 'Mister']
passwords = ('p@sswords', 'abc123', 'guest')
login_dates = ['1/1/2021', '1/1/2021', '1/2/2022']
# users = zip(usernames, passwords)
users = zip(usernames, passwords, login_dates)

for i in users:
    print(i)