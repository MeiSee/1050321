score123 = []
f = 0

while True:
    score = input("請輸入分數：")
    if score == "":
        break
    score = int(score)
    score123.append(score)

    if score < 60:
        f = f+1

print(sum(score123)/len(score123))
print(max(score123))
print(min(score123))
print(f)
