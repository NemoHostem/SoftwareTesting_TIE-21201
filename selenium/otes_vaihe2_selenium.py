#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 20:45:32 2019

@author: jonis
"""

import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException


MY_USER_NAME = 'jonis'
WEB_URL = 'http://localhost:8080/ps/v1/index.html'
USERNAME = 'user'
PASSWORD = 'password'

W = 1 # wait time

browser = webdriver.Chrome(executable_path='/Users/'+ MY_USER_NAME+'/Downloads/chromedriver')
browser.maximize_window()

browser.get(WEB_URL)


def viewListGuard():
    not_hidden = browser.find_element_by_id('view-list').get_attribute('class')
    try:
        assert not_hidden != 'hidden', 'Not in list view'
    except AssertionError as e:
        logging.error(e)
    

def viewFullGuard():
    not_hidden = browser.find_element_by_id('view-full').get_attribute('class')
    try:
        assert not_hidden != 'hidden', 'Not in full view'
    except AssertionError as e:
        logging.error(e)


def clickElementById(el):
    try:
        elem = browser.find_element_by_id(el)
        elem.click()
    except (NoSuchElementException, ElementNotInteractableException) as e:
        logging.error(e)
        
        
def fillTags(id_,tags):
    try:
        elem = browser.find_element_by_id(id_)
        if len(tags) > 0:
            for tag in tags:
                elem.send_keys(tag+',')
            elem.send_keys(Keys.BACKSPACE)
    except (NoSuchElementException, ElementNotInteractableException) as e:
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
    except (NoSuchElementException, ElementNotInteractableException) as e:
        logging.error(e)
    sleep(W)


def insertTags(tags):
    viewFullGuard()
    try:
        fillTags('view-full-keywords',tags)
        sleep(W)
        clickElementById('view-full-save-keywords')
    except (NoSuchElementException, ElementNotInteractableException) as e:
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
    except (NoSuchElementException, ElementNotInteractableException) as e:
        logging.error(e)
    sleep(W)
        
   
login()
searchTags('asd')
openPhoto(1)
replaceTags(['a','b','c'])
closePhoto()
openPhoto(2)
closePhoto()
nextPhotos()
openPhoto(1)
nextPhoto()
previousPhoto()













