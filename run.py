#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

login_status = False
''' 
the login status of any account which will change when user successfully logs in
'''

authentic_username = False
'''
global variable to check if the user's enteredepassword is authentic
'''

satisfactory_password = False
'''
global variable to store the satisfaction of the user with the generated password
'''



def creating_an_account():
    
    global authentic_username
       
    new_user = User.generate_user()
    '''
    A function for creating the user account
    '''
    
    new_user_username = new_user.user_name
    
    
    existing_account = User.find_account_by_username(new_user_username)
    '''
    checking if username already exists
    '''
    
    try:
        if existing_account.user_name == new_user_username:
                print("The account details you entered are already in use, please use another username")
    except:
        print("Your account has successfully been created")
        
        authentic_username = True
        
        new_user.save_user()
        '''
        saving the user's account
        '''
 
def loging_in():    
    global login_status
    
    entered_username = input("Enter your username")
    
    case_account = User.find_account_by_username(entered_username)
    
    account_password = input("Enter the password") 
    
    if case_account.password == account_password:
        print("You have successfully loged into your account")
        login_status = True
    
    else:
        print("You have entered a wrong password or username. Please try again")
    

def account_management():
    global login_status
    
    global satisfactory_password
 
    
    while login_status == False:
        '''
        facilitating account creation and log in
        '''
        
        first_response = int(input('''Hello, Respond with:  
                                1 to create an account. 
                                2 to login into an existing account.
                                                '''))    
        '''
        global variable to store the first response of the user on whether he/she wants to create an account or log 
        into an existing one
        '''
    
        if first_response == 1:
                
            '''
            function to run when the user does not have an account with us
            '''
            while authentic_username == False:    
                creating_an_account()  
            '''
            loop as long as the username of the account created is not authentic i.e has been used before
            '''


        elif(first_response == 2):
            
            '''
            Function to login if the user already has an account
            '''
            loging_in()

    
    if login_status == True:
    
        while login_status == True:
            second_response = int(input('''Choose an option from the following : 
                                        1 => to add a new site and input your own passowrd.
                                        2 => to add a new site but let the app generate the password for you.
                                        3 => to search site passwords by sitename.
                                        4 => to display all sites and their passords.
                                        5 => to delete a site you no longer use.
                                        6 => to log out of your account.
                                                      '''))
            
            
            if second_response == 1:
                new_credentials = Credentials.add_credentials()
                new_credentials.save_credentials()
                print(f"You have successfully added your new site credentials ")   
            
            elif second_response == 2:
                '''
                to generate a user's passord automaticaly
                '''
                
                while satisfactory_password == False:
                    new_credentials = Credentials.generate_random_password()
                    password_generation_response = int(input('''Respond with:
                        1 => If you are Ok with the password
                        2 => If you are not Ok with the password and would like another one to be generated for you
                        3 => If you would like to go back to the main menu and input a password of your own
                                                '''))
                    if password_generation_response == 1:
                        new_credentials.save_credentials()
                        print(f"You have successfully added your new site credentials ")
                        satisfactory_password = True
                    
                    elif password_generation_response == 2:
                        continue
                    
                    elif password_generation_response == 3:
                        satisfactory_password = True
                    else:
                        print("invalide response please sselect an option once more")  
            
            elif second_response == 3:
                Credentials.find_credentials()        
            
            elif second_response == 4:
                credential_list = Credentials.display_credentials()
                
                for credential in credential_list:
                    print(f"{credential.site_name} Account Password = {credential.site_password}")     
            
            elif second_response == 5:
                site_deleting = input("Enter the site name of the site you want to delete")
                site_to_be_deleted = site_deleting.find_credentials
                site_to_be_deleted.delete_account()
                print("Site success fully deleted")
                        
            elif second_response == 6:
                print("Thank you and see you later!")
                login_status = False    
            
            else:
                print ("Invalide Response! Please try once more")




    
if __name__ == "__main__":
    account_management()     
        

    
    
    
    
    



