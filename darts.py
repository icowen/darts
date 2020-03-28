import matplotlib.pyplot as plt
import pandas as pd

player1 = "Colton"
player2 = "Kykes"
scores = pd.DataFrame(columns=[f'{player1}_scores', f"{player2}_score", "Round"])
round_num = 0
# scores = pd.read_csv('kykes_scores.csv', index_col=0)
# round_num = scores["Round"].max() + 1
while True:
    score = 0
    player_score = int(input(f"Enter {player1} score for round {round_num}: "))
    ian_score = int(input(f"Enter {player2}'s score for round {round_num}: "))
    fig, ax = plt.subplots(3)
    scores.loc[len(scores)] = [player_score, ian_score, round_num]
    # print(scores.to_string())
    scores.plot('Round', f'{player1}_scores', ax=ax[0])
    scores.plot('Round', f'{player2}_score', ax=ax[1])
    scores.plot('Round', [f'{player1}_scores', f'{player2}_score'], ax=ax[2])
    ax[0].plot(scores['Round'], [scores[f'{player1}_scores'].mean() for i in range(len(scores))])
    ax[1].plot(scores['Round'], [scores[f'{player2}_score'].mean() for i in range(len(scores))])
    ax[0].set_title(player1)
    ax[1].set_title(player2)
    plt.show()
    round_num += 1
    print("Total:\n" + scores[[f'{player1}_scores', f'{player2}_score']].sum().to_string())
    print(scores[[f'{player1}_scores', f'{player2}_score']].describe())
    scores.to_csv(f'{player1}_vs_{player2}_scores.csv')

