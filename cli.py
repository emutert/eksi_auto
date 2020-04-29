"""
    eksi_engelle command prompt user interface
"""

from __future__ import unicode_literals
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from getpass import getpass
from eksi_engelle import eksi_engelle

#Commands
commands = WordCompleter(['EntryNo','Suser','Blocked Count'], ignore_case=True)


login_status = False

def main():
    global login_status
    session = PromptSession()
    print('Eksi Suser Engelle')
    print('Browser is initializing...')
    
    engelle = eksi_engelle()
    
    while True:
        try:
            while login_status == False:
                print('You need to Login')
                USERNAME = input("email adresi : ")
                PASSWORD = getpass("password : ")
                
                if engelle.login(USERNAME,PASSWORD) == True:
                    print('Login successful')                
                    login_status = True
                else:
                    print('Login Failed')

            try:
                text = session.prompt('>',completer=commands)
                command = text.split()[0]
                value = text.split()[1]

            except IndexError:
                print('S for Suser ')
                print('E for EntryNo ')
                print('B for Blocked Count ')
                continue

            # command Suser 
            if  command== 'Suser':
                engelle.bySuser(value)
                print('Suser:', value, ' Blocked')
            #command EntryNo
            elif command == 'EntryNo':
                print('EntryNo:', value, ' Susers are Blocking')
                engelle.byEntry(value)
            #command Blocked_List
            elif command == 'Blocked':
                print(engelle.blockedSuserList())

            #wrong command 
            else:
                print('wrong command')
                print('You entered:', text.split()[1])

        except KeyboardInterrupt:
            continue
        except EOFError:
            break

    engelle.logout()
    engelle.close() 
    engelle.quit()
    login_status = False
    print('GoodBye!')

if __name__ == '__main__':
    main()

