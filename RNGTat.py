# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:13:38 2022

@author: Panaj
"""

import random
import os
#import time

styles_list = []
shapes_list = []
colors_list = []

global restart
restart = True

global styles_result
styles_result = []
global shapes_result
shapes_result = []
global colors_result
colors_result = []

def create_list(name):
    first_inp = input('Enter first option: \n')
    with open(name + '.txt', 'w') as file:
        file.write(first_inp)
    
def styles_roll():
    styles_list.clear()
    with open('styles.txt', 'r') as file:
        for line in file:
            styles_list.append((line).replace('\n', ''))
    global styles_result
    styles_result = random.sample(styles_list, 1)                
                
def shape_roll():
    shapes_list.clear()
    with open('shapes.txt', 'r') as file:
        for line in file:
            shapes_list.append((line).replace('\n', ''))
    global shapes_result
    shapes_result = random.sample(shapes_list, 1)  
                
def colors_roll():
    colors_list.clear()
    with open('colors.txt', 'r') as file:
        for line in file:
            colors_list.append((line).replace('\n', ''))
    global colors_result
    number = input('Enter a number of colors: \n')
    colors_result = random.sample(colors_list, int(number))
    
def main_roll():
    styles_roll()
    shape_roll()
    colors_roll()
    print('Your new tattoo: \n'
          'Style:  {}'.format(styles_result), '\n'
          'Shape:  {}'.format(shapes_result), '\n'
          'Colors: {}'.format(colors_result))
    
def add_aThing():
    num = input('Choose a list to add option to: \n'
          '1 - Styles list \n'
          '2 - Shapes list \n'
          '3 - Colors list \n')
    if num == '1':
        list_name = 'styles'
    elif num == '2':
        list_name = 'shapes'
    elif num == '3':
        list_name = 'colors'
    with open(list_name + '.txt', 'a') as file:
        file.write('\n' + (input('Write a position to add: \n')))    

def start():
    op = input('1 - Generate a tattoo \n'
               '2 - Add an option to the list\n'
               '3 - Exit\n')
    if op == '1':
        main_roll()
    elif op == '2':
        add_aThing()
    elif op == '3':
        print('Goodbye!')
        global restart
        restart = False        
        
print('Welcome to a random tattoo generator!')

if os.path.isfile(os.path.abspath(os.getcwd()) + '\styles.txt') == False:
    print('Styles list missing')
    print('Creating Styles list.')
    create_list('styles')

if os.path.isfile(os.path.abspath(os.getcwd()) + '\shapes.txt') == False:
    print('Shapes list missing.')   
    print('Creating Shapes list.')
    create_list('shapes')
    
if os.path.isfile(os.path.abspath(os.getcwd()) + '\colors.txt') == False:
    print('Colors list missing')
    print('Creating Colors list.')
    create_list('colors')
                
while restart:
    start()
                
                
                
                
                
                
                
                
                
                
