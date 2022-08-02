import sqlite3

def open_db():
    global conn
    conn = sqlite3.connect('accounts.db')

    global c
    c = conn.cursor()

def close_db():
    c.close()
    conn.close()

def create_table():
    open_db()

    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            password TEXT,
            date_registered TEXT
        )
    ''')

    close_db()

def register(first, last, username, password, date):
    open_db()

    c.execute('''
        INSERT INTO accounts VALUES (?,?,?,?,?)
    ''', (first, last, username, password, date))

    conn.commit()

    close_db()

def login(username, password):
    open_db()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?)
        AND password = (?)
    ''', (username, password))

    data = c.fetchone()
    if data:
        close_db()
        return True
    else:
        close_db()
        return False
 
def get_account_info(username, password):
    open_db()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?)
        AND password = (?)
    ''', (username, password))

    data = c.fetchone()
    close_db()
    return data
#print(get_account_info('NinoDulay','PogiAko123'))
#login('NinoDulay', 'PogiAko123')

def update_first_name(username, password, new_first):
    open_db()

    c.execute('''
        UPDATE accounts 
        SET first_name = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_first, username, password))

    conn.commit()

    close_db()

def update_last_name(username, password, new_last):
    open_db()

    c.execute('''
        UPDATE accounts 
        SET last_name = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_last, username, password))

    conn.commit()

    close_db()

def update_username(username, password, new_user):
    open_db()

    c.execute('''
        UPDATE accounts 
        SET username = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_user, username, password))

    conn.commit()

    close_db()

def update_password(username, password, new_pass):
    open_db()

    c.execute('''
        UPDATE accounts 
        SET password = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_pass, username, password))

    conn.commit()

    close_db()

create_table()
#register('Nino', 'Dulay', 'NinoDulay', 'PogiAko123', '08-02-2022')

#update_first_name('NinoDulay', 'PogiAko123', 'Nino')