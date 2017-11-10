"""numpy save test"""
print('This is scores')
print(scores)
np.save('scores1.npy', scores)

scores1_load = np.load('scores1.npy')
print('This is scores_load saved as scores.npy')
print(scores1_load)

scores1_load[1,0:99] = 10
print('scores1_load renewed')
print(scores1_load)
np.save('scores2.npy', scores1_load)

scores2_load = np.load('scores2.npy')
print('This is scores2_load saved as scores2.npy')
print(scores2_load)