import unittest
from spamnoot.common import can_user_login


class LoginTest(unittest.TestCase):

    def test_case_sensitivity(self):
        test_users = {"USER": "PASSWORD", "user": "asdasd", "Alice": "PASSWORD"}
        self.assertEqual(can_user_login("USER", "password", test_users), False)
        self.assertEqual(can_user_login("alice", "password", test_users), False)
        self.assertEqual(can_user_login("USER", "ASDASD", test_users), False)


if __name__ == '__main__':
    unittest.main()
    LoginTest.test_case_sensitivity()
