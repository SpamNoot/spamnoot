import unittest
from .. import common

class LoginTest(unittest.TestCase):

    def test_case_sensitivity(self):
        test_users = {"USER": "PASSWORD", "user": "asdasd", "Alice": "PASSWORD"}
        self.assertEqual(common.can_user_login("USER", "password", test_users), False)
        self.assertEqual(common.can_user_login("alice", "password", test_users), False)
        self.assertEqual(common.can_user_login("USER", "ASDASD", test_users), False)


if __name__ == '__main__':
    unittest.main()
    LoginTest.test_case_sensitivity()
