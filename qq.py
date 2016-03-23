import random
article = ["那個","這個","一個","這些"]
subject = ["超人","殺手","屍體","小偷","鹹魚","恐龍","帥哥","小明","明星","淑女"]
verb = ["大笑","竊笑","傻笑","奸笑","譏笑","狂笑","微笑","不笑","開槍","殺人","大便","瘙癢","泡妞","撒尿","中槍","握手","喝茶"]
adverb = ["忽然","悄悄","大聲","粗魯","公然","連忙","默默","索性","僅僅"]

for i in range(5):
    if random.randint(1,2)==1:
        print (random.choice(article)+""+random.choice(subject)+""+random.choice(adverb)+""+random.choice(verb))
    else:
        print (random.choice(article)+""+random.choice(subject)+""+random.choice(verb))
