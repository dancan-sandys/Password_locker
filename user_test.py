import unittest

from user import User

class Test_user(unittest.TestCase):
    
    '''
    Test class to test if the user class functions
    
    Args:
        Unittest.Testcase:
            test case class that helps create test cases
    '''
    
    
    
    def setUp(self):
        
        self.new_user = User("Dancan","Oruko", "Sandys", "Stanford1*")
        
    
    def test_init(self):
        
        '''
        Test if the user class has been initialized
        '''
        self.assertEqual(self.new_user.first_name, "Dancan")
        self.assertEqual(self.new_user.last_name, "Oruko")
        self.assertEqual(self.new_user.user_name, "Sandys")
        self.assertEqual(self.new_user.password, "Stanford1*")
        
    def test_saved_users(self):
        
        '''
        test if the user's details have been saved
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),2)
    
    def test_take_new_user_input_details(self):
        '''
        test if user input on his/her account credentials can be tacken
        '''
        
        
        second_user = User.generate_user()
        second_user.save_user()
        self.assertEqual(second_user.first_name, "Dancan")
        self.assertEqual(len(User.users_list),3)
    
    def test_find_user_by_username(self):
        
        self.new_user.save_user()
        login = input("Enter your username")
        account_username = User.find_account_by_username()
        self.assertEqual(account_username,login)
   
        
        
        
if __name__ == "__main__":
    unittest.main()