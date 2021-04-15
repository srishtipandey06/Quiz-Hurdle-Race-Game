a = int(input("Please choose the number of levels you want to play between (0-3) : "))
for i in range(a):
 import quiz
 exec(open("main.py").read(), globals())
 exec(open("main1.py").read(), globals())
 break


