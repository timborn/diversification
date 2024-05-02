# import random
# import numpy as np
# import plotly.graph_objs as go
# from plotly.offline import plot
# import sys

### CONSTANTS
### WINNING_BALANCE = 250	# in the original game, >=$250 is a winner
INITIAL_PRICE = 100

### if random.random() < probability_of_heads:

### def user_bets(balance, idx):
###   dispatch = {
###     0: user_bets_simpleton,
###     1: user_bets_thirds,
###     2: user_bets_cheapskate,
###     3: user_bets_ten,
###     4: user_bets_ten_percent
###   }
###   return dispatch[idx](balance)

def play_the_game(strat_selector):
  ### returns strategy string and balance over time (array)
  balance=INITIAL_BALANCE

  # keep track of balance for all [0..NFLIPS-1] turns
  balance_over_time = [0] * NFLIPS

  for i in range(NFLIPS):
    # when we plot, make sure it looks like we all started from the same place
    if i==0: 
      balance_over_time[i] = INITIAL_BALANCE
      continue

    # Flip an unfair coin 
    coin_flip = flip_coin()
    strategy, guess, bet = user_bets(balance, strat_selector)
  
    # a bit of error checking, please
    if (bet > balance):
      bet=0
  
    if coin_flip == guess:
      balance += bet
    else:
      balance -= bet
  
    balance_over_time[i] = balance
    if (balance <=0 ): 
      break

  # return balance, i+1	# zero based iter
  return strategy, balance_over_time

def simulate_many_games(games, strat_selector):
# returns strategy name and an array of arrays of the balance over time
  results = []	# it's an array - is this necessary?
  for i in range(games):
    strategy, ary = play_the_game(strat_selector)
    results.append(ary)

  # print(results)
  return strategy, results
  
### main

### strat_selector = 0
### if len(sys.argv) >= 2:
###   strat_selector = int(sys.argv[1])


# plot a share price for some number of years
price = {}
price["IBM"] = INITIAL_PRICE
