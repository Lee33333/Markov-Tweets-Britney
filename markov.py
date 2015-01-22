#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    infile = open(corpus)
    fulltext = infile.read()
    words = fulltext.split()
    key1=0
    key2=1
    value=2

    for count in range(len(words)-2):
        
        if (words[key1],words[key2]) in markov_dict:
            markov_dict[(words[key1],words[key2])] = markov_dict[(words[key1],words[key2])] + [words[value]]

        else:
            markov_dict[(words[key1],words[key2])] = [words[value]]
        key1 = key1 + 1
        key2 = key2 + 1
        value = value + 1
        

    return markov_dict

def make_text(chains, wpl, tw):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    allkeys = chains.keys()
    key = random.choice(allkeys)
    key1 = key[0]
    key2 = key[1]
    newtext = key1 + " " + key2
    i = 3

     
    while (key1, key2) in chains:
        i = i + 1
        value = random.choice(chains[(key1, key2)])
        newtext = newtext + " " + value
        key1 = key2
        key2 = value
        print "wpl:", wpl
        print "tw:", tw
        print "i:", i
        if i % wpl == 0:
            newtext = newtext + "\n"
        if i > tw :
            break
       
    return newtext


def main():

    # args = sys.argv

    # Change this to read input_text from a file
    input_text = sys.argv[1]
    total_words = int(sys.argv[3])
    words_per_line = int(sys.argv[2])

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict,words_per_line, total_words)
    print random_text

if __name__ == "__main__":
    main()