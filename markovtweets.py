#!/usr/bin/env python

import sys
import random
import twitter
import os

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dict = {}
    infile = open(corpus)
    fulltext = infile.read()
    fulltext = fulltext.lower()
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

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    allkeys = chains.keys()
    key = random.choice(allkeys)
    key1 = key[0]
    key2 = key[1]
    newtext = key1 + " " + key2
   

     
    while (key1, key2) in chains:
        value = random.choice(chains[(key1, key2)])
        newtext = newtext + " " + value
        key1 = key2
        key2 = value

        if len(newtext) > 129:
            break

    return newtext


def main():
    input_text = sys.argv[1]

    satisfied = False

    while satisfied == False:

        chain_dict = make_chains(input_text)
        random_text = make_text(chain_dict)
        
        print random_text

        response = raw_input("Are you satisfied? If yes, type y to post. Q to quit.")

        if response == "Y" or response == "y" or response == "yes":

            TWITTER_CONSUMER_KEY = os.environ['CONSUMER_KEY']
            TWITTER_CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
            TWITTER_ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
            TWITTER_ACCESS_SECRET = os.environ['ACCESS_SECRET']

            api = twitter.Api(
                consumer_key = TWITTER_CONSUMER_KEY,
                consumer_secret = TWITTER_CONSUMER_SECRET,
                access_token_key = TWITTER_ACCESS_TOKEN,
                access_token_secret = TWITTER_ACCESS_SECRET
                )

            status = api.PostUpdate(random_text)
            satisfied = True

        if response == "Q" or response == "q" or response == "q":
            break

if __name__ == "__main__":
    main()