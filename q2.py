'''
score123 = []
f = 0

while True:
    score = input("請輸入分數：")
    if score == "":
        break
    score = int(score)
    score123.append(score)

    if score >= 60:
        f = f+1
        
def a(f,y):
    result = f / y
    return result

#指定
result = a(f,len(score123))
print(result)
'''
def pass_percentage(scores):
    total_num = len(scores)
    pass_num = 0
    for score in scores:
        if score >= 60:
            pass_num += 1
    return (pass_num/total_num)*100

score = []

