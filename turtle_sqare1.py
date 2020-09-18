from turtle import *

color('red','black')               # (경계선, 채움색)
shape('turtle')  # Turtle 모양(classic,circle,square,turtle)
for i in range(4):
    forward(100)  # size만큼 turtle머리 방향으로 전진
    right(90)  # turtle의 머리 방향을 수치만큼 회전

bk(100) # 뒤로 100만큼 이동
penup()  #펜을 들기 때문에 그림이 그려지지 않음
write("거북아 달려~~~!!") # 문자열 출력
forward(80) # 앞으로 80만큼 이동
write("거북아 달려~~~!!")

left(45)
fd(100)
write("거북아 달려~~~!!")
pendown() # 펜을 내려  그림을 그림
shapesize(3,4,2)  # turtle의 크기  (가로,세로 윤곽선)
setheading(120) # 원점을 기준으로 지정한 각도만큼 머리방향 회전
forward(100)
penup()
setposition(100, 50) #turtle 객체 이동
print(isdown())  #pen의 상태  down :True  Down : False
print(position()) # turtle 위치 출력

home()   # turtle  초기위치로
clear()  # 화면 clear
#done()  # turtle 멈춤
exitonclick() #click으로 turtle창 닫힘
