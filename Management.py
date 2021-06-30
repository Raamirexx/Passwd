import string
import secrets
from datetime import date
import pyperclip
import FileHandler as fh


cellspaces = {
    0: 20,
    1: 32,
    2:20
}

def generate_passwd():
    symbols = '!"#$%&()*+,-./:<=>?@[]^_`{|}~.'
    basechars = string.ascii_letters + string.digits + symbols
    psswd = ''
    for i in range(17):
        char = secrets.choice(basechars)
        if char not in psswd:
            psswd+=char
        else:
            i-=1
    return psswd

def insert_account(*args):
    place = input('Digite a plataforma que você irá criar a conta: ')
    name = input('Digite o seu login nessa plataforma: ')
    content = place +';'+ name +';'+ generate_passwd() +';'+ str(date.today()) + '\n'
    fh.insert_line(content=content)

def list_account(*args):
    print('ID\t\tLUGAR\t\t\t\tLOGIN\t\t\t\t\t\t\tSENHA\t\t\t\tDATA')
    i = 0
    lst = fh.read_lines()
    for line in lst:
        print(str(i) +'\t\t' + create_line(line))
        i+=1

def create_line(lst):
        i = 0
        formatedline = ''
        for cell in lst.split(';'):
            if i < 3:
                cell += ((cellspaces[i] - len(cell)) * ' ')
            formatedline += cell
            i += 1
        return formatedline


def edit_account(md):
    list_account()
    lg,nm,dt = '','',''
    action = 'del'
    id = int(input('Digite o ID da conta que deseja realizar a ação: '))
    if md == '3':
        action = 'up'
        lg = input('Digite o lugar da conta: ')
        nm = input('Digite o login da conta: ')
        dt = str(date.today())

    fh.rewrite_file(id,action,lg,nm,dt)
