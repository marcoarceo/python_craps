# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:37:23 2016

@author: marco
"""
'''
Programmer: Marco Arceo
Class: CptS 111-01, Fall 2016
Programming Assignment #4
10/24/16

Description: "Game of craps"
'''

import random

def display_game_rules():
    '''
    Shows the user what the rules of "craps" are
    '''
    print("A player rolls two dice. Each die has six faces. These faces contain 1, 2, 3, 4, 5, and 6 spots. After the dice have come to rest, the sum of the spots on the two upward faces is calculated. If the sum is 7 or 11 on the first throw, the player wins. If the sum is 2, 3, or 12 on the first throw (called 'craps'), the player loses (i.e. the 'house' wins). If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, then the sum becomes the player's 'point.' To win, you must continue rolling the dice until you 'make your point.' The player loses by rolling a 7 before making the point.")
    print("")
    
def get_bank_balance():
    '''
    prompts the user to enter the balance they wish to begin with
    '''
    balance = float(input("Enter your initial bank balance: $"))
    print("")
    return balance
    
def get_wager_amount(balance):
    '''
    prompts the user to enter a wager
    '''
    wager = float(input("Enter your wager: $"))
    print("")
    if wager <= 2:
        print("You are a low baller")
    elif wager <= 5:
        print("I feel like you are scared to wager more")
    elif wager >= 10 and wager <= balance: 
        print("You must be confident!")
    elif wager > balance:
        pass
    return wager
    
def is_valid_wager_amount(wager, balance):
    '''
    validates whether or not the wager is valid
    '''
    correct = False
    while not correct:
        if wager <= balance:
            print("Your wager is valid")
            print("")
            correct = True
        else:
            print("Your wager is invalid, please enter one equal to or below $%d" %(balance))
            wager = int(input("Please enter your new wager: $"))
            print("")
    return wager
    
def roll_die():
    '''
    simulates a roll of dice
    '''
    roll = random.randrange(1,7)
    return roll
    
def calculate_sum_dice(die1_value, die2_value):
    '''
    adds both the sums of the dice to make the point
    '''
    sum_dice = die1_value + die2_value
    return sum_dice
    
def is_win_lose_or_point(sum_dice):
    '''
    Determines whether the sum is a winning sum, losing sum, or just a point
    '''
    if sum_dice == 7 or sum_dice == 11:
        print("Congrats! You won!")
        print("")
        print("You probably wish you wagered more!")
        return 1
    elif sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        print("Sorry you lost! Please try your luck again.")
        print("")
        return 0
    else:
        print("Point!")
        print("")
        print("Keep your fingers crossed, you'll need the luck!")
        print("")
        point_value = sum_dice
    return point_value
            
def is_point_loss_or_neither(sum_dice, point_value):
    '''
    Determines whether the user got another point, lost, or neither
    '''
    if sum_dice == point_value:
        print("Point")
        return point_value
    elif sum_dice == 7:
        print("Sorry you lost! Please try your luck again.")
        return 0
    else:
        print("Neither")
        print("")
        
    
def main():
    '''
    '''
    display_game_rules()
    balance = get_bank_balance()
    total = 0
    remaining = balance
    while balance > 0:
        wager = get_wager_amount(balance)
        wager = is_valid_wager_amount(wager, balance)
        total += wager
        remaining -= wager 
        print("Your remainging balance is $%d" %(remaining))
        roll_die()
        die1_value = roll_die()
        die2_value = roll_die()
        print("die1: %d die2: %d" %(die1_value, die2_value))
        sum_dice = calculate_sum_dice(die1_value, die2_value)
        print("sum: %d" %(sum_dice))
        point = is_win_lose_or_point(sum_dice)
        if point == 1: #If the user wins
            print("")
            balance = balance + total 
            total = 0
            remaining = balance
            print("Your new balance is $%d" %(balance))
        elif point == 0: #If the user loses
            balance = balance - total
            total = 0
            remaining = balance
            print("Your new balance is $%d" %(balance))
            print("")
        if point != 0 and point != 1: #If the user doesnt win or lose
            while balance > 0:
                if remaining > 0:
                    wager = get_wager_amount(balance) 
                    wager = is_valid_wager_amount(wager, balance)
                    total += wager
                    remaining -= wager 
                    print("Your remainging balance is $%d" %(remaining))
                roll_die()
                die1_value = roll_die()
                die2_value = roll_die()
                print("die1: %d die2: %d" %(die1_value, die2_value))
                sum_dice = calculate_sum_dice(die1_value, die2_value)
                print("sum: %d" %(sum_dice))
                result = is_point_loss_or_neither(sum_dice, point)
                if result == sum_dice: #If the user gets point
                    print("")
                    print ("Congrats! You won!")
                    balance = balance + total 
                    total = 0
                    remaining = balance
                    print("")
                    print("Your new balance is $%d" %(balance))
                    print("")
                    break
                if result == 0: #If the user gets 7
                    balance = balance - total
                    total = 0
                    remaining = balance
                    print("")
                    print("Your new balance is $%d" %(balance))
                    print("")
                    break
                    
main()