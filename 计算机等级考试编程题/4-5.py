'''
羊车门问题。有三扇关闭的门，一扇门后面停着汽车，其余门后是山羊，只有主持人知道每扇门后面是什么。参赛者可以选择一扇门，在
开启它之前，主持人会开启另外一扇门，露出门后的山羊，然后允许参赛者更换自己的选择。请问：参赛者更换选择后能否增加猜中汽车
的机会？---这是一个经典问题。请使用random库对这个随机事件进行预测，分别输出参赛者改变选择和坚持选择获胜的概率。
'''
import random
TIMES = 10000
my_first_choice = 0
my_change_choice = 0
for i in range(TIMES):
    car_in_door = random.randint(0,2)
    my_guess = random.randint(0,2)
    if car_in_door == my_guess:
        my_first_choice += 1
    else:
        my_change_choice += 1
print('参赛者改变选择：{:.2f}\%,坚持选择：{:.2f}\%'.format(my_change_choice/TIMES*100,
                                                                        my_first_choice/TIMES*100))
