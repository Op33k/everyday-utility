from requests import get
from sys import argv
import socket
import os


def request_data(query=''):
    request = get(
        f'http://ip-api.com/json/{query}?fields=status,message,country,regionName,city,zip,lat,lon,timezone,isp,org,reverse,proxy,query'
    )
    return request.json()


def renderUi(func):
    def wrapper(*args, **kwargs):
        print(f"-----| {response['query']}\n--")
        ###################################

        func()

        ###################################
        print()

    return wrapper


@renderUi
def clean_data(*args):
    for name, value in response.items():
        if value:
            print(f'-- {name}: {value}')


@renderUi
def invalid_data(*args):
    if msg := response['message']:
        print(f'ERROR: {msg}')


def verify_response(*args):
    if response['status'] == 'success':
        clean_data(response)
    else:
        invalid_data(response)


for argument in argv:
    if len(argv) == 1:
        response = request_data()
        verify_response(response)
        break

    if os.path.basename(__file__) in argument:
        continue

    try:
        if socket.inet_aton(argument):
            response = request_data(query=argument)
            verify_response(response)

    except socket.error:
        print('ERROR: Invalid argument(s), must be an ip address')
        break
