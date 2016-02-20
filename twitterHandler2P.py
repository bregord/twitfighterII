import tweepy
import pprint
import time
import emu

#takoes 2 lists of moves.
#sends each sequence of moves, and prints off the tweets. One for Player 1, one for player 2
def buildMoveList(player1, player2, sequence):

    for el in sequence:
        #player 1 goes
        if el == 1:
            moves = player1.pop()
            emu.sendMove(el, moves)
            print(moves + "\n")

        #player 2 goes
        elif el == 2:
            moves = player2.pop()
            emu.sendMove(el, moves)
            print(moves + "\n")


consumer_key = "q8kbC8wm9pSZqkE0vuSe6gZZ9"
consumer_secret = "SjJ1iMmxjLv86DApyJskCJ1Mx5Xd1Ox8uCl6SzRidBBwzeDJ1g"
access_token ="3209355825-R6dkFlqBsT2bB4rIRDpXv5V8bsK9uIYqtWgVEMC"
access_token_secret = "zb9UDUVRW6UuE0D2rjqh2JsEnw1NwsGu10aE3izZjAiM5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


try:
        redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
        print ('Error! Failed to get request token.')

api = tweepy.API(auth)

recId = 0;
count = 0;
working = True

moveListPlayer1 = []
moveListPlayer2 = []
turnSequence = []

player1Tag = "teamryu"
player2Tag = "teamken"

#init game
emu.initGame

emu.resetState()

timeLimit = 3*100

initTime = time.time()

while working:

    if(time.time() - initTime  > timeLimit):
        initTime = time.time()
        resetState()

    print("THIS IS THE " + str(count) + " request")

    if recId == 0:
        public_tweets = api.home_timeline(count=20)
        print(public_tweets[0].id)
        recId = public_tweets[0].id
    else:
        public_tweets = api.home_timeline(since_id=recId, count=20)
        recId = public_tweets[0].id

    for tweet in public_tweets:
        print (tweet.text + "\n")


        for el in tweet.entities['hashtags']:
            print(el['text'])
            tag = el['text'].lower()

            if(tag == player1Tag):
                moveListPlayer1.append(tweet.text)
                turnSequence.append(1)

            elif(tag == player2Tag):
                moveListPlayer2.append(tweet.text)
                turnSequence.append(2)
            break


    preTime = time.time()


    buildMoveList(moveListPlayer1, moveListPlayer2, turnSequence)


    timeDiff = time.time() - preTime
    turnSequence.clear()
    moveListPlayer1.clear()
    moveListPlayer2.clear()

    #30 second window
    if(30 -timeDiff > 0):
        time.sleep(30-timeDiff)


#This hits the set reset button on xdotool
def resetState():
    print("resetting game")

"""
TO DO:

While Loop: Pool every x seconds. Grab everything that is more recent than that.

--> Should I write to an auxilliary data structure???

--> better yet-> go by tweet by tweet

2 processes, one for player 1, one for player 2

"""



"""
More tweets you enter

"""
