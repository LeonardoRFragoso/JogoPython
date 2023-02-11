import random
import math

def play():
    user = input("Qual é a sua escolha? 'r' para pedra, 'p' para papel, 's' para tesoura\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, opponent):
    # return true se o jogador vencer o oponente
    # condições de vitória: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

def play_best_of(n):
    # joga contra o computador até que alguém ganhe o melhor de n jogos
    # para vencer, você deve vencer ceil(n/2) jogos (ou seja, 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n/2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play()
        # tie
        if result == 0:
            print('É um empate. Você e o computador escolheram {}. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('Você escolheu {} e o computador escolheu {}. Você venceu!\n'.format(user, computer))
        else:
            computer_wins += 1
            print('Você escolheu {} e o computador escolheu {}. Você perdeu :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print('Você ganhou o melhor de {} jogos! Que campeão :D'.format(n))
    else:
        print('Infelizmente, o computador ganhou o melhor de {} jogos. Mais sorte da próxima vez!'.format(n))


if __name__ == '__main__':
    play_best_of(3) # 2