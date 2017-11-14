import numpy as np
import pandas as pd

# scores = np.loadtxt('sushi3b.5000.10.score', delimiter=' ')
# np.save('scores1.npy', scores)
#
# scores = np.load('scores1.npy')
#
# np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')

scores_pd = pd.read_csv("scores1.csv", header=None)
df = pd.DataFrame(data=scores_pd)
df.columns = [i for i in range(len(df.columns))]



