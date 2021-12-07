# -*- coding: utf-8 -*-
"""
@author: Tas
"""
import unittest
import json
from JobAssignment import ValueChecker

with open(r"C:\Users\Dator\OneDrive\Desktop\DataCamp\JobAssignment/existingOperators.json", "r") as read_file:
    data = json.load(read_file)
    
class ValueCheckerUnitTests(unittest.TestCase):
   
    def test_NumberCheck(self):
        
        # Arrange
        number = "+46296865"
        #Act
        result = ValueChecker(data,number)
        self.assertEqual(result, [(0.17, 'A', '46'), (0.2, 'B', '46')])

    def test_LongestPrefix(self):
        
        # Arrange
        number = "+4673296865"
        #Act
        result = ValueChecker(data,number)
        self.assertEqual(result, [(1.1, 'A', '46732'), (1.0, 'B', '467')])

    def test_ShortestPrefix(self):
        
        # Arrange
        number = "+4485947543"
        #Act
        result = ValueChecker(data,number)
        self.assertEqual(result, [(0.5, 'B', '44')])
    
    def test_PrefixDoesNotExist(self):
        
        # Arrange
        number = "2347386234"
        #Act
        result = ValueChecker(data,number)
        self.assertEqual(result, [])
        
if __name__ == '__main__':
    unittest.main()