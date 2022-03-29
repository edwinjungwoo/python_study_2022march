'''
# if문
if 조건식:
    코드 #pass 사용해 코드 생략 가능 (TODO FIXME BUG NOTE)
# 들여쓰기가 매우 중요 ": 이후에는 무조건 들여쓰기"

x = 5

if x!= 10:
    print('ok')
'''

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
