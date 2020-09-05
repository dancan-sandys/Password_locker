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
        
if __name__ == "__main__":
    unittest.main()