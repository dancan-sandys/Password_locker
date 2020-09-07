import random

class Credentials:
    '''
    A class to store and generate credentials for the user's accounts
    '''
    
    Credentials_list = []
    '''
    A list to store the credentials
    '''
    
    search_credential = None
        
    def __init__(self, site, password):
        
        '''
        initialize the Credentials class
        '''
            
        self.site_name = site
        self.site_password = password
    
    def add_credentials():
        
        '''
        a function to add the credentials
        '''
        
        new_credentials = Credentials(input('Enter the site you would like to secure:  '), input('Enter the site password:  '))
        return new_credentials
    
    
    def save_credentials(self):
        
        '''
        a function to save the credentials
        '''
        
        Credentials.Credentials_list.append(self)
        
    def display_credentials():
        '''
        A function to display the credentials
        '''
        
        return Credentials.Credentials_list
    
    def delete_account(self):
        '''
        A function to delete a site the user no longer wants in the database
        '''
        Credentials.Credentials_list.remove(self)
        
    
    def generate_random_password():
        
        random_passwords = ['Lorem', 'ipsum', 'dolor', 'sitamet', 'consectetur', 'adipiscing', 'elitInteger', 'interdum', 'nonfelis', 'ateuismod', 'Nullaornare', 'viverra', 'justo']
        random_index = random.randint(0,len(random_passwords) - 1)
        random_password = random_passwords[random_index]
        new_credentials = Credentials(input('Enter the site you would like to secure:  '), random_password)
        print(f"Your random password is {random_password}")
        return new_credentials
            
    @classmethod
    def find_credentials(cls):
        '''
        A function to find credentials by site name
        '''
        
        search_credential = input('Enter the site whose passoword you would like to search: ')
        
        for site in Credentials.Credentials_list:
            try:
                if site.site_name == search_credential:
                    print(f'Your {site.site_name} password is {site.site_password}')
                    search_credential = site.site_password
                    
                    return site
                
                else:
                    print('The site you entered does not exist in our data base. You can add it below.')
            
            
            except:
                print('The site you entered does not exist in our data base. You can add it below.')
                
