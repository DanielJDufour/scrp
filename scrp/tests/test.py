#-*- coding: utf-8 -*-
import unittest
from scrp import *
from time import sleep

class TestScrpMethods(unittest.TestCase):

    """
    def testFirefox(self):
        firefox.start()
        sleep(1)
        firefox.restart()
        sleep(5)
        firefox.stop()
    """

    def testGetTextContentViaMarionette(self):
        #firefox.restart()
        textContent = getTextContentViaMarionette("http://danieljdufour.com/")
        self.assertTrue(len(textContent) > 100)


if __name__ == '__main__':
    unittest.main()
