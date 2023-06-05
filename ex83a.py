import re
expressao = input('Digite uma expressão: ')
def chandler(s):
    regex = r'\d+( [+*/-] \d+)*'
    if re.fullmatch(regex, s):
        return True
    else:
        return False
print(chandler(expressao))