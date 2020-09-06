from user import User
from credentials import Credentials

login_status = False
''' 
the login status of any account which will change when user successfully logs in
'''

first_response = int(input("Hello, Respond with  1 to create an account and 2 to login into an existing account"))    



def creating_an_account():   
    new_user = User.generate_user()
    '''
    Creating the user account
    '''
    
    
    
    new_user_username = new_user.user_name
    
    
    
    print(f"Hang on {new_user_username} as we check if your details have been used in our databasse before")
    existing_account = User.find_account_by_username(new_user_username)
    '''
    checking if username already exists
    '''
    try:
        if existing_account.user_name == new_user_username:
            print("The account details you entered are already in use, please log in or try using another username")
    except:
        print("Your account has successfully been created")
    
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
        print("You have entered a wrong. Please try again")
    

def account_management():
    
    '''
    responsible for creating accounts and loging in
    '''
    if first_response == 1:
            
        '''
        function to run when the user does not have an account with us
        '''
        
        creating_an_account()  
        
        '''
        first user's response to determine wehter or not he/she has an account
        '''  


    elif(first_response == 2):
        
        '''
        function to login if the user already has an account
        '''
        loging_in()    
        
        
account_management()
    
    
    
    
    



