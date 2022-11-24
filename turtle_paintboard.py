# turtle_paintboard

import turtle as t

color_status = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'violet']
thickness = 1

print("<Turtle Paint-board>")
print("- 키보드 방향키로 거북이를 움직여 그림을 그려봅시다 -")
print("")

print("사용법:")
print("1. 터틀 스크린에 마우스를 클릭하면 클릭 위치로 거북이가 이동합니다.")
print("2. 거북이를 마우스로 드래그하여 움직일 수 있습니다.")
print("3. 키보드 방향키로 거북이를 움직일 수 있습니다.")
print("   - 좌 우 방향키는 거북이의 방향을 결정합니다.")
print("   - 위 아래 방향키로 거북이를 움직입니다.")
print("4. Enter키로 '선 그리기'를 활성화 혹은 비활성화 할 수 있습니다.")
print("5. Tab키로 선 굵기를 조절할 수 있습니다.")
print("6. 숫자 키로 색을 지정할 수 있습니다.")
print("   - 0: 검정  1: 빨강  2: 주황  3: 노랑  4: 초록  5: 파랑  6: 보라")
print("7. 그림을 리셋하려면 r, 프로그램을 종료하려면 q를 누르세요.")
print("8. 도형을 그리려면 스페이스바를 누르고 아래의 안내를 따르세요.")

def key_Return():
    pen_status = t.isdown()
    
    if pen_status == True:
        t.penup()
        print("")
        print("'선 그리기' 비활성화")
        
    else:
        t.pendown()
        print("")
        print("'선 그리기' 활성화")
    
def key_Up():
    t.forward(10)

def key_Down():
    t.backward(10)

def key_Left():
    t.left(90)

def key_Right():
    t.right(90)

def color(status):
    t.pencolor(color_status[status])

def key_0():
    color(0)
    print("")
    print("검정색")

def key_1():
    color(1)
    print("")
    print("빨간색")

def key_2():
    color(2)
    print("")
    print("주황색")

def key_3():
    color(3)
    print("")
    print("노란색")

def key_4():
    color(4)
    print("")
    print("초록색")

def key_5():
    color(5)
    print("")
    print("파란색")

def key_6():
    color(6)
    print("")
    print("보라색")

def key_space():
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

            while True:
                radius = float(input(" -> 반지름을 입력하세요: "))

                if radius < 0:
                    print("")
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print("")
                    continue

                else:
                    break
            
            t.speed(6)
            t.circle(radius)
            t.speed(0)

            print("")
            print("원을 그렸습니다!")
            print("도형을 더 그리려면 스페이스바를 한번 더 누르세요.")
            break
        
        elif shape == 'other':
            print("정n각형을 그립니다.")

            while True:
                n = int(input(" -> n을 입력하세요: "))

                if n < 0:
                    print("")
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print("")
                    continue
                
                else:
                    break

            while True:
                side = float(input(" -> 한 변의 길이를 입력하세요: "))

                if side < 0:
                    print("")
                    print("잘못 입력하셨습니다. 다시 입력하세요.")
                    print("")
                    continue

                else:
                    break

            t.speed(3)
            for i in range(n):
                t.forward(side)
                t.left(int(360/n))
            t.speed(0)

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

def key_Tab():
    global thickness
    thickness += 2

    if thickness > 10:
        thickness = 1
        
    t.pensize(thickness)
    
    print("")
    print("선 굵기:", thickness)

def key_r():
    t.goto(0, 0)
    t.clear()

t.shape("turtle")
t.speed(0)
t.pensize(thickness)
t.ondrag(t.goto)

s = t.Screen()

s.onkey(key_Return, 'Return')

s.onkey(key_Tab, 'Tab')

s.onscreenclick(t.goto)

s.onkeypress(key_Up, 'Up')
s.onkeypress(key_Down, 'Down')

s.onkey(key_Left, 'Left')
s.onkey(key_Right, 'Right')

s.onkey(key_0, '0')
s.onkey(key_1, '1')
s.onkey(key_2, '2')
s.onkey(key_3, '3')
s.onkey(key_4, '4')
s.onkey(key_5, '5')
s.onkey(key_6, '6')

s.onkey(key_space, 'space')

s.onkey(s.bye, 'q')
s.onkey(key_r, 'r')

s.listen()









    
