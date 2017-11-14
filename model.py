import numpy as np
import pandas as pd

scores = np.loadtxt('sushi3b.5000.10.score', delimiter=' ')
np.save('scores1.npy', scores)

# csv_file = 'scores1.csv'
scores = np.load('scores1.npy')

np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')

scores_pd = pd.read_csv("scores1.csv", header=None)
df = pd.DataFrame(data=scores_pd)
df.columns = [i for i in range(len(df.columns))]

def createU():
    df.loc[len(df.index)] = -1
    new_user_id = len(df.index)
    return new_user_id

def createI():
    df.loc[:, len(df.columns)] = -1
    new_item_id = len(df.columns)
    return new_item_id


def update(user_id, item_id, evaluation):
    user_id = int(user_id)
    item_id = int(item_id)
    evaluation = int(evaluation)
    scores[user_id, item_id] = evaluation
    np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')
    return scores[user_id, item_id]


def deleteU(user_id):
    df.at[user_id] = -1
    np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')
    return "Success"


def deleteI(item_id):
    df.at[:,item_id] = -1
    np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')
    return "Success"