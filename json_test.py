import numpy as np
scores = np.loadtxt('sushi3b.5000.10.score', delimiter=' ')

target_user_index = 0

similarities = []
target = scores[target_user_index]

print('This is target')
print(target)

for i, score in enumerate(scores):
    # 共通の評価が少ない場合は除外
    indices = np.where(((target + 1) * (score + 1)) != 0)[0]

    if len(indices) < 3 or i == target_user_index: #自分との比較は飛ばす
        continue


    print('This is i')
    print(i)

    print('This is indices')
    print(indices)

    print('This is target[indices]')
    print(target[indices])

    print('This is score[indices]')
    print(score[indices])

    # if len(indices) > 4:
    #     print(i)

    similarity = np.corrcoef(target[indices], score[indices])[0, 1]

    print('This is similarity')
    print(similarity)

    if np.isnan(similarity):
        continue

    similarities.append((i, similarity))

result = sorted(similarities, key=lambda s: s[1], reverse=True)


print(result)
print(result.tolist())