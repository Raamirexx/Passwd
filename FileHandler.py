import io,os


def open_file(mode):
    return open('passwds.txt',mode)

def read_lines():
    return open_file('r').readlines()

def insert_line(content):
    f = open_file('a')
    f.write(content)
    f.close()


def rewrite_file(line_index,*argv):
    f = open_file('r+')
    d = f.readlines()
    f.seek(0)
    j = 0
    for i in d:
        if line_index != j:
            f.write(i)
        elif argv[0] == 'up':
             f.write(argv[1] + ';' + argv[2] + ';' + i.split(';')[2] + ';' +  argv[3] + '\n')
        j+=1
    f.truncate()
    f.close()
