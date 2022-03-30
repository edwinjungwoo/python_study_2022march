# FizzBuzz 문제
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
# 공배수를 가장 먼저 if문에 두고 elif로 이어나가는 것이 핵심
# 20.8 문제

a, b = map(int,input().split())
for i in range(a, b+1):
    if i%5 == 0 and i%7 == 0:
        print("FizzBuzz")
    elif i%5 == 0:
        print("Fizz")
    elif i%7 == 0:
        print("Buzz")
    else:
        print(i)

import turtle as t
t.shape('turtle')
while True:
#    t.forward(100)
#    t.right(90)

    for i in range(5):      # 오각형이므로 5번 반복
        t.forward(100)
        t.right(360 / 5)    # 360을 5로 나누어서 외각을 구함

import turtle as t
 
n = 60    # 원을 60번 그림
t.shape('turtle')
#t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전

# 21.6 별그리기
import turtle as t

n, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(n):
    t.forward(line)
    t.right((360/n)*2)
    t.forward(line)
    t.left(360/n)

# 리스트 메소드
a = []
a.append(요소) #요소 하나 추가 (요소란 하나의 값일 수도, 리스트일 수도 ...)
a.extend(리스트) #리스트를 연결해 확장, 요소 여러 개 추가할 때 (리스트만 값으로 받음)
a.insert(인덱스, 요소) #특정 인덱스에 요소 추가 
# ㄴ(인덱스에 len(a)시 마지막 인덱스보다 크기 때문에 리스트 끝에 추가할 때 자주 활용)
a.pop() #마지막 요소 삭제, 인덱스 지정도 가능
a.remove(값) #리스트에서 특정 값 찾아내 삭제
a.count(요소) #리스트 내 요소의 개수를 반환
a.reverse() #리스트에서 요소의 순서를 반대로 뒤집음
a.sort() #리스트 요소를 오름차순으로 정렬 (Reverse = True 시, 내림차순 정렬)
# * sorted() 함수는 정렬된 새 리스트를 생성
a.clear() #리스트 모든 요소 삭제
# 22.2
a = [0, 0, 0, 0, 0]
b = a.copy()
# a is b 는 False 반환하지만 a == b 는 True 반환

# for 반복문에서 인덱스로 요소 출력
a = [38, 21, 53, 62, 19]
for i in range(len(a)):
    print(a[i])

# 리스트 컴프리헨션 - 리스트 표현식, 리스트 안에 식, for 반복문 등 지정
a = [i for i in range(10)] # 0부터 9까지 숫자 생성해 리스트 생성
a = [i for i in range(10) if i % 2 ==0]

# 리스트에 map 사용
a = list(map(str, range(10)))
print(a)

 # 22.10 문제
a, b = map(int, input().split())
c = [2**i for i in range(a, b+1)]
del c[1]
del c[-2]
print(c)
