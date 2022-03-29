
# if문
if 조건식:
    코드 #pass 사용해 코드 생략 가능 (TODO FIXME BUG NOTE)
# 들여쓰기가 매우 중요 ": 이후에는 무조건 들여쓰기"

x = 5

if x!= 10:
    print('ok')


price = int(input())
coup = input()
if coup == "Cash3000":
    a = price - 3000
if coup == "Cash5000":
    a = price - 5000
print(a)

#else 사용
if 조건식:
    코드1
else:
    코드2

# True - if의 코드, False&None - else의 코드 실행
# 파이썬에서 False: False, None, 0, 0.0, 0j, 비어있는 시퀀스(문자열, 리스트, 튜플, 딕셔너리)..

# 14.7 연습문제
kor, eng, math, sci = map(int,input().split())
avg = ((kor+eng+math+sci)/4)
if kor<0 or kor>100 or eng<0 or eng>100 or math<0 or math>100 or sci<0 or sci>100:
    print("잘못된 점수")
else:
    if avg >= 80:
        print("합격")
    else:
        print("불합격")

# elif
button = int(input())
 
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

x = int(input())
if 11<= x <=20:
    print("11~20")
elif 21<= x <=30:
    print("21~30")
else:
    print("아무것도 해당하지 않음")

age = int(input())
balance = 9000
if 7 <= age <= 12:
    charge = 650
elif 13 <= age <= 18:
    charge = 1050
elif 19 <= 19:
    charge = 1250
balance -= charge
print(balance)

# 반복문
for 변수 in range(): #in 뒤에 횟수 지정
    반복할 코드
# 변수 i를 루프 인덱스라고도 부르며 index의 첫 머리글자를 따서 i 를 주로 사용
# range()처럼 시퀀스 객체도 똑같이 작동 가능

#구구단
n = int(input())
for i in range(1,10):
    print(n, '*', i,'=', n*i)

#while문
초기식
while 조건식:
    반복할 코드
    변화식

import random
#주사위
random.randint(1, 6) # 1~6 사이 랜덤한 정수
random.choice() # ()내에서 랜덤히 추출

n = int(input())
fee = 1350
while n >= 1350:
    n -= fee
    print(n)
# break는 for와 while 에서 제어흐름을 벗어나기 위해 사용 (루프 중단)
# continue는 제어흐름 유지, 코드 실행만 건너뜀 (거른다고 생각하면 될 듯?)

i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
    if i >73:
        break
    print(i, end = ' ')
    i += 1

#18.6연습문제
start, stop = map(int, input().split())

i = start

while True:
    if i%10 ==3:
        i+=1
        continue
    if i > stop:
        break
    print(i, end =' ')
    i+=1

# 중첩 루프
for i in range(5):  #세로 방향
    for j in range(5): #가로 방향
        print('j', j, sep='',end=' ') # 줄바꿈X
    print('i', i, '\\n', sep='')
# 이처럼 중첩 루프는 2차원 평면을 다룰 수 있어 이미지 처리, 영상 처리, 좌표계 처리 등에 사용
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='')
    print()

for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j == i:                # 세로 방향 변수와 같을 때
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:                     # 세로 방향 변수와 다를 때
            print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

n = int(input())
for i in range(n):
    for j in range(i+n):
        if j > n-i-2:
            print('*', end='')
        else:
            print(' ', end='')
    print()
