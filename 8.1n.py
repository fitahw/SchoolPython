import re

def find_logged_in_users(log_file):
    with open(log_file, 'r') as file:
        logs = file.read()
    users = re.findall(r'User: (\w+) logged in.', logs)
    return list(set(users))  

users = find_logged_in_users('log_file_zad8.1.txt')
print(users)