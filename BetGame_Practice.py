import random 
import matplotlib.pyplot as plt

starting_balance = 1000
starting_bet = 25
def one_game(balance, bet, win_prob = 0.5):
    place = random.random()
    if place < win_prob:
        balance += bet
        bet = starting_bet
    else:
        if balance > bet:
            balance -= bet
            bet = bet * 2
        else:
            balance = 0
            bet = 0
    return (balance, bet)

def simulate_run(num_rounds):
    current_balance = starting_balance
    current_bet = starting_bet 
    tracker = []
    while len(tracker) < num_rounds  and current_balance > 0:
        current_balance, current_bet = one_game(current_balance, current_bet)
        tracker.append(current_balance)
    return tracker

results = [simulate_run(1000) for i in range(100)]

final_results = [run[-1] for run in results]
avarage_profit = sum([final_result - 1000 for final_result in final_results]) / len(final_results)

win_rate = sum([run[-1] > starting_balance for run in results]) / len(final_results) * 100
print(final_results)
print('your avarage profit is', avarage_profit)
print('your win rate is', win_rate, '%')

for run in results:
    plt.plot(run)

plt.xlabel('number of flips')
plt.ylabel('balance')
plt.title('Maritangle Betting on a Monte Carlo Coin Flip Game')
plt.show()

