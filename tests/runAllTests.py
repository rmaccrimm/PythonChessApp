# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest
from chessTests.test_chessGui import ChessGui_TestCase
from chessTests.test_chessPieces import ChessPiece_TestCase
from chessTests.test_chessController import ChessController_TestCase
from chessTests.test_moveGenerator import MoveGenerator_TestCase

if __name__ == '__main__':
    testCases = [ChessGui_TestCase, ChessPiece_TestCase, 
                 ChessController_TestCase, MoveGenerator_TestCase]
    testLoader = unittest.TestLoader()
    suiteList = []
    for test in testCases:
        testSuite = testLoader.loadTestsFromTestCase(test)
        suiteList.append(testSuite)
    allTests = unittest.TestSuite(suiteList)
    testRunner = unittest.TextTestRunner()
    testRunner.run(allTests)