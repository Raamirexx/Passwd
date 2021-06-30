from Management import *
import pyperclip

commands = {
    '1':list_account,
    '2':insert_account,
    '3':edit_account,
    '4':edit_account
}

def printmenu():
    print(
        '1 - Ver Contas \n'+
        '2 - Nova conta \n' +
        '3 - Editar conta \n' +
        '4 - Excluir conta \n' +
        '5 - Sair'
    )

if __name__ == '__main__':
    t = ''
    while t == '':
        printmenu()
        t = input('Digite um comando: ')
        if t not in commands.keys():
            print('Esse comando não existe')
        else:
           commands[t](t)
           t = input('Aperte enter para voltar')








