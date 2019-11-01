#!/bin/python
# coding: utf-8

import fmbtx11
import unittest
from time import sleep

OPNRO = ":246248" # Käsiteltävän Xephyr näytön tunnus, muuta tähän omasi
DELAY = 1 # Komennon jälkeen odotettava aika sekunneissa

# luodaan olio jonka läpi voidaan käsitellä testikohdetta näytöllä
s = fmbtx11.Screen(OPNRO)
s.setBitmapPath('kuvat')


class PagesTest(unittest.TestCase):
    def setUp(self):
        s.refreshScreenshot()

    def tearDown(self):
        s.tapBitmap("closeTab.png", colorMatch=0.9)
        sleep(DELAY)
        s.refreshScreenshot()


    def test_moveToPage2(self):
        s.tapBitmap("input-username.png", colorMatch=0.9)
        sleep(DELAY)
        s.refreshScreenshot()
        found = s.verifyBitmap("header2.png", colorMatch=0.9)
        self.assertTrue(found, "Header2 not found")

if __name__ == '__main__':
    unittest.main()
