from urllib.request import urlopen

try:
    with urlopen('http://pudim.com.br/', timeout=3) as connection:
        code = connection.getcode()
    print(f'Site está acessível')
except:
    print(f'Site não está acessível')
