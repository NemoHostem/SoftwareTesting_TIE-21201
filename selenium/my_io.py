#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:48:51 2019

@author: jonis
"""

import sys

def my_o(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as INFILE:
            return INFILE.read().split('\n')
    except FileNotFoundError:
        print("Could not find file '%s'" % file_name)
        sys.exit(1)