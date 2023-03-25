import unittest
from implemented_function import speed_level,score_level

"""
Using Boundary Value Analysis

-1=> Invalid   39=>low         119=>Normal     199=>High      219=>V.High
 0 =>lOW       40 => Normal    120=>High       200=>V.high    220 =>Invalid
 1 =>LOW       41=> Normal     121=>High       201=>V.high    221=>Invalid

"""

# class SpeedTest(unittest.TestCase):
#     def test_speed(self):
#         self.assertEqual('',speed_level(40))



class TestSpeed(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Set up test suite for Evaluate Speed Level")
        
    def setUp(self):
        print("Set up test case")
    



    def test_Invalid_scores(self):
        self.assertEqual('Invalid',speed_level(-1))
    def test_Invalid_scores(self):
         self.assertEqual('Low',speed_level(0))
    def test_low_scores(self):
        self.assertEqual('Low',speed_level(39))
    def test_mormal_scores(self):
        self.assertEqual('Normal',speed_level(40))
    def test_mormal_scores(self):
        self.assertEqual('Normal',speed_level(119))      
    def test_high_scores(self):
        self.assertEqual('High',speed_level(120)) 
    def test_high_scores(self):
        self.assertEqual('High',speed_level(199))
    def test_very_high_scores(self):
        self.assertEqual('V.High',speed_level(200))
    def test_very_high_scores(self):
        self.assertEqual('V.High',speed_level(219))
    def test_very_high_scores(self):
        self.assertEqual('Invalid',speed_level(220))   
    def test_very_high_scores(self):
        self.assertEqual('Invalid',speed_level(221)) 
    def tearDown(self):
        print("Tear down test case")

    @classmethod
    def tearDownClass(cls):
        print("Tear down test suite for Evaluate Speed Level")

"""
Using Boundary Value Analysis

Score Evaluate Level Test

-1 =Invalid      49 =Failed    64 =Passed     74 =Good      84=V.Good        99 =Excellent
 0=Failed        50 =Passed    65  =Good      75 =V.Good    85 =Excellent    100 Invalid
 1=Failed        51 =Passed    66  =Good      76 =V.Good    86 =Excellent    101=Invalid
"""
class TestScore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Set up test suite for Evaluate Score Level function")
        
    def setUp(self):
        print("Set up test case")
    



    def test_Invalid_scores(self):
        self.assertEqual('Invalid',score_level(-1))
    def test_low_scores(self):
        self.assertEqual('Failed',score_level(0))
    def test_low_scores(self):
        self.assertEqual('Failed',score_level(49))
    def test_mormal_scores(self):
        self.assertEqual('Passed',score_level(50))
    def test_mormal_scores(self):
        self.assertEqual('Passed',score_level(64))
    def test_high_scores(self):
        self.assertEqual('Good',score_level(65))
    def test_high_scores(self):
        self.assertEqual('Good',score_level(74))
    def test_very_high_scores(self):
        self.assertEqual('V.Good',score_level(75))
    def test_very_high_scores(self):
        self.assertEqual('V.Good',score_level(84))
    def test_very_high_scores(self):
        self.assertEqual('Excellent',score_level(85))      
    def test_very_high_scores(self):
        self.assertEqual('Excellent',score_level(99))   
    def test_Invalid_scores(self):
        self.assertEqual('Invalid',score_level(100))
    def tearDown(self):
        print("Tear down test case")

    @classmethod
    def tearDownClass(cls):
        print("Tear down test suite for Evaluate Score Level function")

test_suite = unittest.TestSuite()
test_suite.addTest(unittest.makeSuite(TestScore))
test_suite.addTest(unittest.makeSuite(TestSpeed))



if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite)
    # unittest.main()