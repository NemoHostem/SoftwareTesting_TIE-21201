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


def view_list_guard():
    try:
        not_hidden = browser.find_element_by_id('view-list').get_attribute('class')
    except SeleniumExceptions as e:
        logging.error(e)
    try:
        assert not_hidden != 'hidden', line_info+'\nNot in list view'
    except AssertionError as e:
        logging.error(e)
    

def view_full_guard():
    try:
        not_hidden = browser.find_element_by_id('view-full').get_attribute('class')
    except SeleniumExceptions as e:
        logging.error(e)
    try:
        assert not_hidden != 'hidden', line_info+'\nNot in full view'
    except AssertionError as e:
        logging.error(e)

def assert_empty():
    try:
        browser.find_element_by_id('0')
        assert False, line_info+'\nFound content where there should have been none!'
    except SeleniumExceptions:
        pass
        # Here the exception is desired as no element should be found
    except AssertionError as e:
        logging.error(e)

def create_tags_post(tags):
    try:
        text = browser.find_element_by_id('view-full-keywords').get_attribute('value')
    except SeleniumExceptions as e:
        logging.error(e)
    try:
        a = False
        for tag in tags:
            if not tag in text:
                print('Tag '+tag+' was not created')
                a = True
        assert not a, line_info+'\nSome tags were not created'
    except AssertionError as e:
        logging.error(e)


def clear_tags_post():
    try:
        text = browser.find_element_by_id('view-full-keywords').get_attribute('value')
    except SeleniumExceptions as e:
        logging.error(e)
    try:
        assert len(text) == 0, line_info+'\nTags were not removed (tags: '+text+')'
    except AssertionError as e:
        logging.error(e)


def click_element_by_id(el):
    try:
        elem = browser.find_element_by_id(el)
        elem.click()
    except SeleniumExceptions as e:
        logging.error(e)
        
        
def fill_tags(id_,tags):
    try:
        elem = browser.find_element_by_id(id_)
        if len(elem.get_attribute('value')) > 0:
            elem.send_keys(',')
        if len(tags) > 0:
            for tag in tags:
                elem.send_keys(tag+',')
            elem.send_keys(Keys.BACKSPACE)
        else:
            elem.clear()
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
    

def previous_photos():
    view_list_guard()
    click_element_by_id('view-previous')
    sleep(W)
    
    
def next_photos():
    view_list_guard()
    click_element_by_id('view-next')
    sleep(W)
    
    
def previous_photo():
    view_full_guard()
    click_element_by_id('view-full-previous')
    sleep(W)
    
    
def next_photo():
    view_full_guard()
    click_element_by_id('view-full-next')
    sleep(W)


def open_photo(i): 
    view_list_guard()
    click_element_by_id(i)
    sleep(W)
   
    
def close_photo():
    view_full_guard()
    click_element_by_id('view-full-close')
    sleep(W)
        

def clear_tags():
    view_full_guard()
    try:
        elem = browser.find_element_by_id('view-full-keywords')
        elem.clear()
        click_element_by_id('view-full-save-keywords')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)
    clear_tags_post()


def insert_tags(tags):
    view_full_guard()
    try:
        fill_tags('view-full-keywords',tags)
        sleep(W)
        click_element_by_id('view-full-save-keywords')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)
    create_tags_post(tags)
    
    
def replace_tags(tags):
    view_full_guard()
    clear_tags()
    insert_tags(tags)
    
    
def search_tags(tags):
    view_list_guard()
    try:
        fill_tags('view-searchbar-keywords',tags)
        sleep(W)
        click_element_by_id('view-search')
    except SeleniumExceptions as e:
        logging.error(e)
    sleep(W)
    
    
def clear_search():
    view_list_guard()
    try:
        fill_tags('view-searchbar-keywords',[])
        sleep(W)
        click_element_by_id('view-search')
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

for run_name in run_names:
    test_run = my_o(run_name)
    
    for line_num,line in enumerate(test_run):
        line_info = 'On line ' + str(line_num+1) + ' Command: ' + line
        eval(line)













