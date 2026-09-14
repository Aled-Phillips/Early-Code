import random 

def one_game(balance, bet = 10, win_prob = 0.5):
    place = random.random()
    if place < win_prob:
        balance += bet
    else:
        balance -= bet
    return balance

def simulate_run(num_rounds):
    current_balance = 200
    tracker = []
    while len(tracker) < num_rounds  and current_balance > 0:
        current_balance = one_game(current_balance)
        tracker.append(current_balance)
    return tracker

results = [simulate_run(100) for i in range(500)]

final_results = [run[-1] for run in results]
avarage_profit = sum(final_results) / len(final_results) - 200

win_rate = sum([run[-1] > 200 for run in results]) / len(results) * 100

print( avarage_profit)
print(win_rate)



