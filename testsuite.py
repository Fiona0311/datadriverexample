import unittest
from scenarios.user_operate_flow import UserActionTest

def suite():
    #@方法1
    # suite = unittest.TestSuite()
    # suite.addTest(UserActionTest('test_login'))
    # suite.addTest(UserActionTest('test_register'))
    # return suite

    #@方法2
    # useroperation = unittest.TestLoader().loadTestsFromTestCase(UserActionTest)
    # return unittest.TestSuite([useroperation])

    #@方法3
    suites = unittest.TestSuite()
    suites.addTests(unittest.TestLoader().loadTestsFromTestCase(UserActionTest))
    return suites

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
    