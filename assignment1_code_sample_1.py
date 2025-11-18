import os
import pymysql
from urllib.request import urlopen

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}


def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

# Injection again, 

# OWASP Category: Injection
#Fix: avoid using os.system as it just pases what you write into the shell
def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')


# Insecure because the url is not encrypted, uses http instead of https
# No validation or timeout in urlopen

# OWASP Category: Security Misconfiguration & Cryptographic Failures
# Fix: Use https and add timeouts
def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

# SQL Injection

# Injection
def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
