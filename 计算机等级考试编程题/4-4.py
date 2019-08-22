# 猜数游戏续。当用户输入的不是整数（如字母、浮点数等）时，程序会终止执行退出。改编题目1中的程序，当用户输入出错时给出“
# 输入内容必须是整数！"的提示，并让用户重新输入。
import random

num = random.randint(1,1001)
count = 0
while True:
    try:
        guess = eval(input('请猜猜是多少?(1-1000)：'))
        if type(guess) == int :
            if guess < num:
                print('猜小了！')
                count += 1
            elif guess > num:
                print('猜大了！')
                count += 1
            else:
                count += 1
                print('恭喜你！猜对了！总共猜了{}次！'.format(count))
                break
        else:
            raise NameError
    except  NameError:
        print('输入内容必须是整数！')