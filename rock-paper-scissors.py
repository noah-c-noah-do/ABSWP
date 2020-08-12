import random
import sys

print("ROCK, PAPER, SCISSORS")
win_count = 0
loss_count = 0
draw_count = 0
moves = ['ROCK', 'PAPER', 'SCISSORS']
accepted = (['r', 'p', 's', 'q'])
print(f"{win_count} Wins, {loss_count} Losses, {draw_count} Ties")
print("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
move_dict = dict({'r': 'ROCK'}, s='SCISSORS', p='PAPER')
winning_ = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}

while True:
    user_move = input()
    while user_move not in accepted:
        print('Type one of r, p, s, or q.')
        print("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit")
        user_move = input()
    if user_move == 'q':
        sys.exit()
    else:
        print(f"{move_dict[user_move]} versus...")
    computer_move = random.choice(moves)
    print(computer_move)
    if computer_move == move_dict[user_move]:
        print('It is a tie!')
        draw_count += 1
        print(f"{win_count} Wins, {loss_count} Losses, {draw_count} Ties")
    elif winning_[computer_move] == move_dict[user_move]:
        print('You Lose!')
        loss_count += 1
        print(f"{win_count} Wins, {loss_count} Losses, {draw_count} Ties")
    elif winning_[move_dict[user_move]] == computer_move:
        print('You Win!')
        win_count += 1
        print(f"{win_count} Wins, {loss_count} Losses, {draw_count} Ties")
