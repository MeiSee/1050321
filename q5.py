e = input("請輸入：")

if e < 50:
    print("100")
elif 50<= e <= 100:
    e = 100+(e-50)*10
    print(e)
elif e > 100:
    e = 100+(e-50)*10+(e-100)*20
    print(e)
