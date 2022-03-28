'''
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
'''

