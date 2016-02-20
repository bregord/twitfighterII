import tweepy
import pprint
import time
import emu

consumer_key = "8vY1DFoK47n0mol2uzD7p1FtT"
consumer_secret = "aysBMg9mcYbJp58nahDT2HxmeQMbb8L1mtU5rGPCe6JxkYN65b"
access_token ="2484767203-bapj1TnALxD1NR2mAKLViUHraWo1jlIzKEGPDdc"
access_token_secret = "Ui6zLQx6nKy2fTakfb8NbF8kOg9hZJP5NwV4v4es9U3wQ"

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

player1Tag = "TeamScorpion"
player2Tag = "TeamSubZero"

#init game
#emu.initGame

timeLimit = 4*60

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

            if(tag != player1Tag):
                moveListPlayer1.append(tweet.text)
                turnSequence.append(1)

            elif(tag == player2Tag):
                moveListPlayer2.append(text)
                turnSequence.append(2)
            break

    print (moveListPlayer1)

    buildMoveList(moveListPlayer1, movelistPlayer2, turnSequence)

    preTime = time.time()
    #compute moves here

    #print and send off each move here.


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

#takoes 2 lists of moves.
#sends each sequence of moves, and prints off the tweets. One for Player 1, one for player 2
def buildMoveList(player1, player2, sequence):

    for el in sequence:
        #player 1 goes
        if el == 1:
            emu.sendMove()

        #player 2 goes
        elif el == 2:
            emu.sendMove()

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
