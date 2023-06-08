import sys
import argparse

parser = argparse.ArgumentParser(description='Arguments for phonebook assistant')
parser.add_argument('hello', help='This is variable to start dialog with assistant')
parser.add_argument('add', default='', help='Add contact to phonebook')
parser.add_argument('change')
parser.add_argument('phone')
parser.add_argument('show all')
parser.add_argument('good bye', 'close', 'exit', )

args = parser.parse_args()

add = args.add

PHONEB00K = {}


def say_hallo(hallo: str):
    if hallo == "hello":
        print("How can I help you?")
    else:
        print('If you want to start, write "hello", please')


def add_contact(name: str, phone: str):
    PHONEB00K[name] = phone


def change_contact(name: str, phone: str):
    if name in list(PHONEB00K):
        PHONEB00K[name] = phone
    else:
        print(f'There is no {name} in phonebook!')


def show_phone(name: str):
    print(f'The number you have searched: {PHONEB00K[name]}')


def show_all_contacts():
    for k, v in enumerate(PHONEB00K):
        print(f'|{k:^5}|{v:^10}|{PHONEB00K[v]:^15}|')


OPERATIONS = {
    'hello': say_hallo,
    'add': add_contact,
    'change': change_contact,
    'phone': show_phone,
    'show all': show_all_contacts
}


def get_hendler(arg):
    return OPERATIONS[arg]

def main():
    print("Hello!!! I'm your assistant.")
    flag = True



