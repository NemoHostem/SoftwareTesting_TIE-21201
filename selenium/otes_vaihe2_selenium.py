#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:45:32 2019

@author: jonis
"""

import sys
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException

from my_io import my_o


SeleniumExceptions = (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException)
r = RunState()


def viewListGuard():
    try:
        not_hidden = browser.find_element_by_id('view-list').get_attribute('class')
    except SeleniumException:
        logging.error(e)
    try:
        assert not_hidden == 'hidden', line_info+'\nNot in list view'
    except AssertionError as e:
        logging.error(e)
    

def viewFullGuard():
    try:
        not_hidden = browser.find_element_by_id('view-full').get_attribute('class')
    except SeleniumException:
        logging.error(e)
    try:
        assert not_hidden == 'hidden', line_info+'\nNot in full view'
    except AssertionError as e:
        logging.error(e)


def clickElementById(el):
    try:
        elem = browser.find_element_by_id(el)
        elem.click()
    except SeleniumExceptions as e:
        logging.error(e)
        
        
def fillTags(id_,tags):
    try:
        elem = browser.find_element_by_id(id_)
        if len(tags) > 0:
            for tag in tags:
                elem.send_keys(tag+',')
            elem.send_keys(Keys.BACKSPACE)
    except SeleniumExceptions as e:
        logging.error(e)


def login():
    elem = browser.find_element_by_id('input-username')
    elem.send_keys(USERNAME)
    
    elem = browser.find_element_by_id('input-password')
    elem.send_keys(PASSWORD)
    
    elem = browser.find_element_by_id('album-login')
    elem.click()
    
    elem = browser.find_element_by_id('view-album')
    
    sleep(W)
    

def previousPhotos():
    viewListGuard()
    clickElementById('view-previous')
    sleep(W)
    
    
def nextPhotos():
    viewListGuard()
    clickElementById('view-next')
    sleep(W)
    
    
def previousPhoto():
    viewFullGuard()
    clickElementById('view-full-previous')
    sleep(W)
    
    
def nextPhoto():
    viewFullGuard()
    clickElementById('view-full-next')
    sleep(W)


def openPhoto(i): 
    viewListGuard()
    clickElementById(i)
    sleep(W)
   
    
def closePhoto():
    viewFullGuard()
    clickElementById('view-full-close')
    sleep(W)
        

def clearTags():
    viewFullGuard()
    try:
        elem = browser.find_element_by_id('view-full-keywords')
        elem.clear()
        clickElementById('view-full-save-keywords')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)


def insertTags(tags):
    viewFullGuard()
    try:
        fillTags('view-full-keywords',tags)
        sleep(W)
        clickElementById('view-full-save-keywords')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)
    
    
def replaceTags(tags):
    viewFullGuard()
    clearTags()
    insertTags(tags)
    
    
def searchTags(tags):
    viewListGuard()
    try:
        fillTags('view-searchbar-keywords',tags)
        sleep(W)
        clickElementById('view-search')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)
        

file_name = 'test_config.txt'
test_config = my_o(file_name)


for line in test_config:
    exec(line)


browser = webdriver.Chrome(executable_path='/Users/'+ MY_USER_NAME+'/Downloads/chromedriver')
browser.maximize_window()

browser.get(WEB_URL)


file_name = 'test_run.txt'
test_run = my_o(file_name)


for line_num,line in enumerate(test_run):
    line_info = 'On line ' + str(line_num+1) + ' Command: ' + line
    eval(line)













