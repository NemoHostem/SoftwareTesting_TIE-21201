#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:45:32 2019

@author: jonis
"""

from time import sleep
from selenium import webdriver

MY_USER_NAME = 'jonis'
WEB_URL = 'http://localhost:8080/ps/v1/index.html'
USERNAME = 'user'
PASSWORD = 'password'

browser = webdriver.Chrome(executable_path='/Users/'+ MY_USER_NAME+'/Downloads/chromedriver')
browser.maximize_window()

browser.get(WEB_URL)

elem = browser.find_element_by_id('input-username')
elem.send_keys(USERNAME)

elem = browser.find_element_by_id('input-password')
elem.send_keys(PASSWORD)

elem = browser.find_element_by_id('album-login')
elem.click()

