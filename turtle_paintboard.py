# turtle_paintboard

import turtle as t

t.shape("turtle")
s = t.Screen()

color_status = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'violet']

print("<Turtle Paint-board>")
print("- 키보드 방향키로 거북이를 움직여 그림을 그려봅시다 -")
print("")

print("사용법:")
print("1. 터틀 스크린에 마우스를 클릭하면 클릭 위치로 거북이가 이동합니다.")
print("2. 키보드 방향키로 거북이를 움직일 수 있습니다.")
print("   - 좌 우 방향키는 거북이의 방향을 결정합니다.")
print("   - 위 아래 방향키로 거북이를 움직입니다.")
print("3. Enter키를 누르면 거북이가 선을 그립니다. Tab키를 누르면 거북이가 선을 그리지 않습니다.")
print("4. 숫자 키로 색을 지정할 수 있습니다.")
print("   - 0: 검정  1: 빨강  2: 주황  3: 노랑  4: 초록  5: 파랑  6: 보라")
print("5. 그림을 리셋하려면 r, 프로그램을 종료하려면 q를 누르세요.")
print("6. 도형을 그리려면 스페이스바를 누르고 아래의 안내를 따르세요.")

def keyReturn():
    t.pendown()

def keyTab():
    t.penup()

def keyUp():
    t.forward(10)

def keyDown():
    t.backward(10)

def keyLeft():
    t.left(90)

def keyRight():
    t.right(90)

def color(status):
    t.pencolor(color_status[status])

def key0():
    color(0)

def key1():
    color(1)

def key2():
    color(2)

def key3():
    color(3)

def key4():
    color(4)

def key5():
    color(5)

def key6():
    color(6)

def keyspace():
    print("")
    print("- 도형 그리기 -")
    print("shell 창에 입력하여 거북이가 도형을 그리도록 명령합니다.")
    print("원을 그리려면 'circle', 정n각형을 그리고 싶다면 'other'을 입력하세요.")
    print("도형 그리기를 취소하려면 'cancel'을 입력하세요.")

    while True:
        print("")
        shape = input(" -> 여기에 입력: ")
        print("")
    
        if shape == 'circle':
            print("원을 그립니다.")
            radius = float(input(" -> 반지름을 입력하세요: "))
            t.circle(radius)

            print("")
            print("원을 그렸습니다!")
            print("도형을 더 그리려면 스페이스바를 한번 더 누르세요.")
            break
        
        elif shape == 'other':
            print("정n각형을 그립니다.")
            n = int(input(" -> n을 입력하세요: "))
            side = float(input(" -> 한 변의 길이를 입력하세요: "))

            for i in range(n):
                t.forward(side)
                t.left(int(360/n))

            print("")
            print("정" + str(n) + "각형을 그렸습니다!")
            print("도형을 더 그리려면 스페이스바를 한번 더 누르세요.")
            break
    
        elif shape == 'cancel':
            print("도형 그리기를 취소하셨습니다.")
            print("도형을 그리려면 스페이스바를 한번 더 누르세요.")
            break

        else:
            print("잘못 입력하셨습니다. 다시입력하세요.")
            continue

def keyr():
    t.reset()

s.onkey(keyReturn, 'Return')
s.onkey(keyTab, 'Tab')

s.onscreenclick(t.goto)

s.onkeypress(keyUp, 'Up')
s.onkeypress(keyDown, 'Down')

s.onkey(keyLeft, 'Left')
s.onkey(keyRight, 'Right')

s.onkey(key0, '0')
s.onkey(key1, '1')
s.onkey(key2, '2')
s.onkey(key3, '3')
s.onkey(key4, '4')
s.onkey(key5, '5')
s.onkey(key6, '6')

s.onkey(keyspace, 'space')

s.onkey(s.bye, 'q')
s.onkey(t.reset, 'r')

s.listen()









    
