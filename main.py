import sys
clients = ['pablo','ricardo']

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already in the client\'s list')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx,client))


def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
        print('client '+ client_name+' was replaced for '+updated_client_name)
    else:
        print('client is not in clients list')


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in clients list')


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True

    return False


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


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('What is the client name? >  ')
        if client_name.upper() == 'Q' or client_name.upper() == 'QUIT':
            client_name = None
            break

    return client_name

if __name__ == '__main__':

    _quit = False

    while not _quit:
        _print_welcome()

        command = input().upper()

        if command == 'C':
            client_name = _get_client_name()
            create_client(client_name)
            list_clients()
            continue
        elif command == 'L':
            list_clients()
            continue
        elif command == 'U':
            client_name = _get_client_name()
            updated_client_name = input( 'what is the updated client name > ')
            update_client(client_name,updated_client_name)
            list_clients()
            continue
        elif command=='D':
            client_name = _get_client_name()
            delete_client(client_name)
            list_clients()
        elif command == 'S':
            client_name = _get_client_name()
            found = search_client(client_name)
            if found:
                print('the client is in the client\'s list')
            else:
                print('client {} is not in our client\'s list'.format(client_name))
            continue
        elif command == 'Q':
            _quit = True
        else:
            print("invalid conmmand")
