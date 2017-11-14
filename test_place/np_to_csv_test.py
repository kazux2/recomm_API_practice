import numpy as np
import sys

scores = np.loadtxt('sushi3b.5000.10.score', delimiter=' ')
np.save('scores1.npy', scores)

scores = np.load('scores1.npy')

np.savetxt('scores1.csv', scores, delimiter=',', fmt='%d')
