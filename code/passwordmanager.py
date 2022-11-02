from cryptography.fernet import Fernet

'''
def createKey():
    generatekey = Fernet.generate_key()
    with open('private.key', 'wb') as keyfile:
        keyfile.write(generatekey)
        
createKey()

--> Uncomment this and use this function once to create the key. 
'''

def loadKey():
    readKey = open('private.key','rb')
    key = readKey.readline()
    readKey.close()
    return key

master_key = input('Enter the master key: ')
add_key = loadKey() + master_key.encode()
final_key = Fernet(add_key)

def add():
    accountname = input('Type in Account: ')
    username = input('Username: ')
    password = input('Password: ')
    with open("password.txt", 'a') as file:
        file.write(final_key.encrypt(accountname.encode()).decode()+'|||'
                   +final_key.encrypt(username.encode()).decode()+'|||'
                   +final_key.encrypt(password.encode()).decode()+'\n')

def view():
    try:
        print('Opening the file')
        fileread = open('password.txt', "r")
        for read in fileread:
            data = read.rstrip()
            account, user, passwd = data.split("|||")
            print('Account: ',final_key.decrypt(account.encode()).decode(),
                  'User: ',final_key.decrypt(user.encode()).decode(),
                  'Password: ',final_key.decrypt(passwd.encode()).decode())
        fileread.close()
    except:
        print("Some issue opening the file or it doesn't exist. Press Q to quit\n")

while True:
    operation = input('What operation you want to perform? \n Type 1. Add password. \n Type 2. View Password'
                      ' \nQ to Quit ')

    if operation.lower().strip() == 'q':
        break
    if operation == "1":
        add()
    elif operation == "2":
        view()
    else:
        print('Type in valid input')
        continue
