"""
    eksi_engelle user command prompt user interface
"""

from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from getpass import getpass
from eksi_engelle import eksi_engelle

#Commands
commands = WordCompleter(['EntryNo','Suser','Logout','Blocked_list'], ignore_case=True)


login_status = False

def main():
    global login_status
    session = PromptSession()
    print('Eksi Suserler ENGELLE V2')
    print('You need to Login First')
    USERNAME = input("email adresi : ")
    PASSWORD = getpass("password : ")
    
    engelle = eksi_engelle()
    
    while True:
        try:
            if login_status == False:
                
                if engelle.login(USERNAME,PASSWORD) == True:
                    print('Login successful')                
                    login_status = True
            
            text = session.prompt('>',completer=commands)
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        else:
            command = text.split()[0]
            # command Suser 
            if  command== 'Suser':
                print('You entered:', text.split()[1])
            #command EntryNo
            elif command == 'EntryNo':
                print('You entered:', text.split()[1])
            #command Blocked_List
            elif command == 'Blocked_list':
                print('You entered:', text.split()[1])
            #Logout
            elif command == 'Logout':
                engelle.logout()
            #wrong command 
            else:
                print('wrong command')
                print('You entered:', text.split()[1])

    if login_status == True:
        engelle.logout()
        login_status = False
        print('GoodBye!')

if __name__ == '__main__':
    main()

