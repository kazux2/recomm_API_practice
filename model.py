import numpy as np
import pandas as pd

csv_file = 'data_storage/scores1.csv'
npy_file = 'data_storage/scores1.npy'

# scores = np.load(npy_file)
scores_pd = pd.read_csv(csv_file, header=None)
df = pd.DataFrame(data=scores_pd)
df.columns = [i for i in range(len(df.columns))]


def reset():
    scores = np.loadtxt('sushi3b.5000.10.score', delimiter=' ')
    np.save(npy_file, scores)
    scores = np.load(npy_file)
    np.savetxt(csv_file, scores, delimiter=',', fmt='%d')

    scores_pd = pd.read_csv(csv_file, header=None)
    df = pd.DataFrame(data=scores_pd)
    df.columns = [i for i in range(len(df.columns))]
    return "reset"


def createU():
    df.loc[len(df.index)] = -1 # add a new row with values of -1
    np.savetxt(csv_file, df, delimiter=',', fmt='%d')
    new_user_id = len(df.index)
    return new_user_id


def createI():
    df.loc[:, len(df.columns)] = -1 # add a new column with values of -1
    np.savetxt(csv_file, df, delimiter=',', fmt='%d')
    new_item_id = len(df.columns)
    return new_item_id


def update(user_id, item_id, evaluation):
    # (unsolved problem) router couldn't set data type
    user_id = int(user_id)
    item_id = int(item_id)
    evaluation = int(evaluation)

    df.at[user_id, item_id] = evaluation
    result = df.at[user_id, item_id]
    np.savetxt(csv_file, df, delimiter=',', fmt='%d')
    return int(result)


def deleteU(user_id):
    df.at[user_id] = -1# renew all values of a target user to -1
    np.savetxt(csv_file, df, delimiter=',', fmt='%d')
    return "Success"


def deleteI(item_id):
    df.at[:,item_id] = -1 # renew all values of a target item to -1
    np.savetxt(csv_file, df, delimiter=',', fmt='%d')
    return "Success"

