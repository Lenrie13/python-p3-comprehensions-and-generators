#!/usr/bin/env python3

# Function to return a list of even numbers from num_list
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

# Function to add exclamation marks to each sentence in sentence_list
def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]
