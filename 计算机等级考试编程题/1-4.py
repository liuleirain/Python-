# 系统循环提示输入用户三个小爱好并一起输出。
hobbies = ""
for i in range(3):
	s = input('请输入你的小爱好(最多三个，按Q或q结束):')
	if s.upper() == 'Q':
		break
	hobbies += s + ' '
print('你的小爱好是：',hobbies)