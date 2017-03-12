# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from TestChessGui import *
from TestChessPiece import *

if __name__ == '__main__':
    testCases = [TestChessGui]
    testLoader = unittest.TestLoader()
    suiteList = []
    for test in testCases:
        testSuite = testLoader.loadTestsFromTestCase(test)
        suiteList.append(testSuite)
    allTests = unittest.TestSuite(suiteList)
    testRunner = unittest.TextTestRunner()
    testRunner.run(allTests)