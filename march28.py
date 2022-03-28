
# 몫과 나머지 함께 구하려면 divmod()함수 사용
divmod(5,2) #(몫, 나머지)

int() #정수
float() #실수
str() #문자형

type() #자료형 확인

ap = float(input())
DMG = (ap*0.6) + 225
print(DMG)

# 변수 여럿 한 번에 만들기: ,(콤마)로 구분
x, y, z = 10, 20, 30


a = int(input('첫 번째 숫자를 입력하세요: '))
b = int(input('두 번째 숫자를 입력하세요: '))
 
print(a + b)


#a, b = input('문자열 두 개를 입력하세요: ').split()
a, b = map(str, input('문자열 두 개: ').split()) #map()함수 사용
print(a)
print(b)


#print()내 sep = '' 통해 여러 개 출력 사이에 구분점 삽입 가능
#end = '' print 여러 번 사용해 한 줄에 표현 시 사용 *sep과 반대 개념
# '\n' 줄바꿈!
year, month, day, hour, minute, second = input().split()
print(year, month, day, sep = '-', end = 'T')
print(hour, minute, second, sep = ':')


10 == 10 #True
10 != 5 #True
10 > 20 #False
# 정수 객체와 실수 객체가 서로 다른 것을 확인하기 위해 id()함수 사용

# 작은따옴표 안에 작은땅옴표 넣으려면 작은따옴표 앞에 \ (역슬래시) 붙이면 됨


# range(시작값, 종료값, 증가폭)
# 리스트 언패킹 : 리스트에서 변수 여러 개로
x = [1, 2, 3]
a, b, c = x

# len()함수 통해 시퀀스 개수(길이) 구함
# a[0]처럼 [숫자]라는 인데스 통해 해당 요소에 접근[-1]은 뒤에서 첫번째
# __getitem__ 메서드로도 호출 가능

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4]) #인덱스 0부터 3까지 (0이상 4미만)
# 인덱스 증가폭 a[2:8:3] (2이상 8미만 인덱스 중 3씩 증가시키며 호출)

x = input().split()
del x[-5:]
print(tuple(x))

a = input()
b = input()
print(a[1::2] + b[0::2])


# 딕셔너리 {key: value}
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health']) #딕셔너리명[키값]
# 기존 할당과 마찬가지로, 없는 키에 값을 할당하면 해당 키가 추가되고 값이 할당됨
lux['mana_regen'] = 3.28
print(lux)
# in 연산자로 키 있는지 확인
'health' in lux # True 반환


a = input().split()
b = map(float,input().split())
jax = dict(zip(a,b))
print(jax)