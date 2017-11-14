f = open('sushi3-2016/sushi3b.5000.10.score')
lines = f.readlines()  # ファイル終端まで全て読んだデータを返す
f.close()

print(type(lines))
print(lines[0])
for line in lines:
    words = line.split(' ')  # カンマで区切って格納


print(lines[0])
# with open('hello.csv', 'w') as f:
#     for line in lines:
#         datas = line.split(' ')
#         for data in datas:
#             f.write(data)
#             f.write('\n')# 文字列の最後に改行を加えて1行ずつ書き込み



sentence = "-1 0 1 2 3 4"
words = sentence.split(' ')
# print(type(words))
# print(words)

# with open('hello.csv', 'w') as f:


import pandas as pd

# データフレームを作成
# df = pd.DataFrame([
#     ["0001", "John", "Engineer"],
#     ["0002", "Lily", "Sales"]],
#     columns=['id', 'name', 'job'])

# CSV ファイル (employee.csv) として出力
# df.to_csv("employee.csv")


