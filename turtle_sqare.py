#import turtle
#turtle.shape('turtle') #커서의 모양

'''
def square():
  for i in range(4): #0부터 4까지 발생
    turtle.forward(100)
    turtle.right(90)
'''
'''
for i in range(60):
       square() #위에서 정의한 함수
       turtle.right(5) # 오른쪽으로 5도씩 움직인다.
       turtle.speed(5) # 5의 속도로 움직인다.
turtle.done()
'''
'''
import turtle as t
t.shape('turtle')
for i in range(4):
    t.circle(100, 180) #반지름 100, 180도 회전
    t.rt(90)


t.pu()
t.goto(-100,0) #왼 쪽으로 100 만큼 이동
t.pd()
t.fillcolor('yellow')
t.begin_fill()
t.circle(100) #반지름 100
t.end_fill()
t.ht()
t.done()
'''



