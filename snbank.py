import random
import string
import os

staff = open('staff.txt','w') #to create the file for staff details
staff.write ('1.Username CSH11YP \nPassword T335577 \nEmail: \nFullname: \n2.Username CSH11ZQ \nPassword T446699 \nEmail: \nFull Name: \n')
staff.close()

staff = open('staff.txt', 'r')        # to open and read the file after appending details

customer = open('customer.txt','w')
customer.close()

details = ['Username', 'Password', 'Account name', 'Opening Balance', 'Account Type', 'Account email']

while True:
    print('1. Staff Login \n2. Close App \n')
    enter = int (input('Enter 1 to Login and 2 to close the app: \n'))
    if enter == 1:
        username = input('Username: ')
        password = input('This field is case sensitive \nPassword: ')

        with open('staff.txt','r') as staff:
            userdetail = staff.readline()
            str = userdetail.split()
            userdetail = (str[1])
            

        with open('staff.txt','r') as staff:
            detail = staff.readline()
            detail = staff.readline()
            str = detail.split()
            detail = (str[1])

        with open('staff.txt','r') as staff:
            userdetail2 = staff.readline()
            userdetail2 = staff.readline()
            userdetail2 = staff.readline()
            userdetail2 = staff.readline()
            userdetail2 = staff.readline()
            str = userdetail2.split()
            userdetail2 = (str[1])

        with open('staff.txt','r') as staff:
            detail2 = staff.readline()
            detail2 = staff.readline()
            detail2 = staff.readline()
            detail2 = staff.readline()
            detail2 = staff.readline()
            detail2 = staff.readline()
            str = detail2.split()
            detail2 = (str[1])    
            

            if username.casefold() == userdetail and password == detail:
                with open('newlogin.txt','a') as session:
                    session.write (username + '\n')
                    session.write (password+ '\n')
                session = open('newlogin.txt','r')  
                print(session.read())

            elif username.casefold() == userdetail2 and password == detail2:
                with open('newlogin.txt','a') as session:
                    session.write (username + '\n')
                    session.write (password+ '\n')
                session = open('newlogin.txt','r')  
                print(session.read())        

            msg = int(input('Please enter the appropriate number \n1. Create new bank account \n2. Check account details \n3. Logout \n'))
            if msg == 1:
                Account_name = input('Please input the following details \nAccount Name:') 
                try:
                    Opening_balance = int(input('Opening Balance:'))
                except ValueError:
                    print('Please enetr a correct account number')
                Account_type = input('Account Type:')      
                Account_email = input('Account email:') 

                def generateacctnumber():
                    n = 10
                    ''. join(['{}'. format(randit(0,9)) for num in range (0,n)])
                acct_number = generateacctnumber()    
                print('Here is your Account Number', acct_number)  

            
                with open('customer.txt','a') as customer: 
                    customer.write (Account_name + '\n')
                    customer.write (Opening_balance + '\n')
                    customer.write (Account_type + '\n')
                    customer.write (Account_email + '\n')
                    customer = open('customer.txt','r')

                
                msg = int(input('Please enter the appropriate number \n1. Create new bank account \n2. Check account details \n3. Logout \n'))
                if msg == 2:
                    try:
                        Account_details = int(input('Please enter your account number'))
                    except ValueError:
                        print('Please enter a correct account number')
                  

                    with open('customer.txt','r') as customer:
                        print(customer.read())

                elif msg == 3:      
                    os.remove('newlogin.txt')        
            
            elif username.casefold() != userdetail and password != detail:
                print('The username or password you enetered is incorrect \n')
                username = input('Username: ')
                password = input('This field is case sensitive \nPassword: ')          
    
               
    elif enter == 2:
        print('Your session has ended')
    break        
        