import sys
import csv
import os

CLIENT_TABLE='.clients.csv'
CLIENT_SCHEMA = ['name', 'company','email', 'position']
clients = []


def _initalize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)
    f.close()



def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    f.close()
    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)



def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in the client\'s list')



def list_clients():
    global clients
    print('uid | name | company | email | position')
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


def update_client(client_uid):
    global clients

    if client_uid>=len(clients) or client_uid<0:
        print("client does not exist")
        return

    print("current client information: ")
    print('uid | name | company | email | position')
    client=clients[client_uid]

    print('{uid} | {name} | {company} | {email} | {position}'.format(
        uid = client_uid,
        name = client['name'],
        company = client['company'],
        email = client['email'],
        position = client['position']
    ))

    new_client = {
        'name': _get_client_field('name'),
        'company': _get_client_field('company'),
        'email': _get_client_field('email'),
        'position': _get_client_field('position')
    }


    clients[client_uid] = new_client



def delete_client(client_uid):
    global clients

    if client_uid>=len(clients) or client_uid<0:
        print("client does not exist")
        return None

    client = clients.pop(client_uid)
    return client


def search_client(client_name):
    global clients
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return clients.index(client)

    return None


def _print_welcome():
    print("welcome to nxp ventas")
    print('*'*50)
    print('what would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('*'*50)
    print('[Q]uit program')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}? >> '.format(field_name))
    return field

def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? >  ')
        if client_name.upper() == 'Q' or client_name.upper() == 'QUIT':
            client_name = None
            break

    return client_name


def _print_query(idx):
    global clients
    client = clients[idx]
    print('uid | name | company | email | position')

    print('{uid} | {name} | {company} | {email} | {position}'.format(
        uid = idx,
        name = client['name'],
        company = client['company'],
        email = client['email'],
        position = client['position']
    ))


if __name__ == '__main__':
    _initalize_clients_from_storage()

    _print_welcome()

    command = input().upper()

    if command == 'C':
        client ={
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position')
        }
        create_client(client)
        #list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_uid = int(input('what is the client id? >'))
        update_client(client_uid)
        #list_clients()

    elif command=='D':
        client_uid = int(input('what is the client id? >'))
        delete_client(client_uid)

    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found != None:
            _print_query(found)

    else:
        print("invalid conmmand")

    _save_clients_to_storage()
