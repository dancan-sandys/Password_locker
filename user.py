class User:
    '''
    class to create a new user
    '''
    
    users_list = []    
    
    def __init__(self,fname,lname,usname,psword):
        self.first_name = fname
        self.last_name = lname
        self.user_name = usname
        self.password = psword
    
   
    
            
    def save_user(self):
        '''
        A function to save the user
        '''
        
        User.users_list.append(self)
    
    def generate_user():
        
        '''
        Pick user input when creating an account and store the user 's details
        '''
        user = User(input("Enter your first name: "), input("Enter your last name: "), input("Enter your prefered username: "), input("Enter your password: "))
        
        return user
        
    @classmethod
    def find_account_by_username(cls,login):
        
        '''
        Find a user's account details by username
        '''
        print(login)
        for account in User.users_list:
            if login == account.user_name :
                print("...Acount exists")
                return account
            
                
        
    def ask_for_password():
        
        case_password = input("Enter your password: ")
        return case_password
        
        
new_user = User("Dancan","Oruko", "Sandys", "Stanford1*")
new_user.save_user()