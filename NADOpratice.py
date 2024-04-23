# print("a" + "b")
# print("a","b")

# 방법 1
# print("나는 %d살입니다." % 20) #여기서 d는 정수값이다.
# print("나는 %s을 좋아해요" % "파이썬") #여기서 s는 str 문자열을 의미한다,
# print("Apple은 %c로 시작해요." % "A") #여기서 c는 charecter 문자의 의미 
# %s로만 써도 모두 출력 가능한가봄
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." %("오렌지","구름"))

# 방법2

# print("나는 {}살 입니다." .format(20))
# print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

#방법 3
# print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨강"))
# print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨강", age = 20))

# #방법 4
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

#저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
# print("/Users/subinoh/Desktop/untitledfolder/pratice.py")


# \r : 커서를 맨 앞으로 이동
# print("purple Apple\rPwine")

# \b : 백스페이스 ( 한 글자 삭제)
# print("reddA\bpple")

# \t : 텝
# print("red\tApple")

# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 객수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호 : nave51!

# site = "http://naver.com"
# site = "http://daum.net"
# site = "http://google.com"
# site = "http://youtube.com"
# my_str = site.replace("http://","") #규칙1
# # print(my_str)
# my_str = my_str[:my_str.index(".")]
# # print(my_str)
 
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(password)
# print("{0}의 비밀번호는 {1}입니다.".format(site, password))

#리스트 []

#지하철 칸별로 10명, 20명, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #조세호씨가 몇번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# #하하씨가 다음 정류장에서 다음 칸에 탔다.
# subway.append("하하") #append의 경우, 제일 마지막 순서에 붙게된다.
# print(subway)

# #정형돈씨를 유재석 / 조세호 사이에 태워봄
# subway.insert(1,"정형돈")
# print(subway)

# #지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop()) #pop은 젤 마지막 순서부터 차례로 빠지는거
# print(subway)

# # print(subway.pop()) #pop은 젤 마지막 순서부터 차례로 빠지는거
# # print(subway)

# # print(subway.pop()) #pop은 젤 마지막 순서부터 차례로 빠지는거
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용 가능
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# mix_list.extend(num_list)
# print(mix_list)

# 사전
# 사전의 경우 중괄호를 사용

# cabinet = {3:"유재석", 100:"김태호"} #key는 3이고 그 Key의 value는 유재석이다 라는 뜻
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# # print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능")) #5라는 key가 있으면 해당하는 value를 출력하고
# #없다면 "사용 가능"을 출력하라는 의미
# print("hi")

# print(3 in cabinet) # 3이라는 key가 cabinet 안에 있다면 "TRUE"
# print(5 in cabinet) # 5라는 key가 cabinet 안에 없다면 "False"

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호" 
# # 이 문장의 의미는 cabinet 안에 "C-20"이라는 key를 만들고 value값으로 "조세호"를 추가한다는 뜻
# # 만일 이미 "C-20"이 있다면 새롭게 업데이트 한다는 의미
# print(cabinet)

# # 손님이 떠난 경우
# del cabinet["A-3"]
# print(cabinet)

# # 현재 사용중인 Key 정보들만 출력
# print(cabinet.keys())

# # 현재 사용중인 value 정보들만 출력
# print(cabinet.values())

# # 현재 사용중인 key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플
# list처럼 내용 변경 및 추가가 쉽지 않지만 속도가 list보다 빠름
# 변경되지 않는 값에 대해서 사용 가능

# menu = ("돈까스" , "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") 튜플은 추가가 안되기 때문에 오류발생함

# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# #괄호가 들어가면 튜플 형태임

# print(name, age, hobby)

# set (집합) : 중복 X, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set) #{1,2,3}만 출력, 중복이 없기 때문에

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java와 python 모두 가능한 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (jave 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java는 할 수 있는데 python 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # 위 인원들을 교육해서 python할 수 있는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java할 줄 알았는데 까먹어버림
# java.remove("김태호")
# print(java)

#자료구조의 변경
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# # {'우유', '커피', '주스'} <class 'set'> 이렇게 나오는데, 자료 형태가 set이라는 의미

# menu = list(menu)
# print(menu, type(menu))
# #['우유', '커피', '주스'] <class 'list'> 결과, 자료 형태가 list로 바뀜

# menu = tuple(menu)
# print(menu, type(menu))
# #('커피', '우유', '주스') <class 'tuple'> , 자료 형태가 tuple로 바뀜

# #set일때는 {}, list일때는 [], tuple일때는 () 

# menu = set(menu)
# print(menu, type(menu))

# from random import *
# # event = list(range(1,21))
# # print(event)
# # shuffle(event)
# # print(event)

# # chicken = sample(event,1)
# # print(chicken)
# # coffee = sample(event,3)
# # print(coffee)

# # print("당첨자 발표\n 치킨 당첨자 : {0} \n 커피 당첨자 : {1} \n 축하합니다" .format(chicken, coffee))

# users = range(1,21)
# # print(type(users))
# users =list(users)
# # print(type(users))

# print(users)
# shuffle(users)
# print(users)

# #중복이 되면 안된다고 했고, 치킨 당첨자는 1명이고, 커피 당첨자는 3명이니까 
# #한꺼번에 4명 뽑기!

# winners = sample(users, 4) 

# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

# 분기

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <+ temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# 반복문 for

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]:
#     print("대기번호 : {0}". format(waiting_no))
    
    
# 숫자가 순차적으로 커지는거면 range 쓸 수 있음
# for waiting_no in range(5): # 0,1,2,3,4
#     print("대기번호 : {0}". format(waiting_no))
    
# for waiting_no in range(1,6): # 1,2,3,4,5 (6직전까지)
#     print("대기번호 : {0}". format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#while 카페에서 손님을 5번을 불렀는데, 대답이 없으면 버리는 정책을 만들었다.
# customer = "토르"
# index = 5
# # while (조건) -> 특정 조건을 만족할때까지 계속해서 반복하라는 의미
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer =  "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회 ".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer : #
#     print("{0}, 커피가 준비 되었습니다. ".format(customer))
#     person = input("이름이 어떻게 되세요? ")

# Continue
# absent = [2, 5, 13, 16] #결석
# no_book = [15] #책을 깜빡한 7번
# for student in range(1, 21): # 1~20
#     if student in absent:
#         continue # 계속해서 반복문 실행
#     elif student in no_book:
#         print("오늘 수업 끝. {0}은 교무실로 따라와".format(student))
#         break #continue된 값들이 break 사용시, 바로 반복문 탈출
#     print("{0}, 책 읽어봐".format(student))
    
#한 줄 for
#출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students) #[1, 2, 3, 4, 5] 지금은 위처럼 딱 나옴
# students = [i + 100 for i in students]
# print(students)

#학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

#학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#QUIZ) 50명의 승객, 총 탑승 승객 수!
# 조건 1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야하 합니다.

#(출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 손님
# 내가 만들어본 것
# customer = [range(1,51)]
# time_list = list(range(5,51))
# shuffle(time_list)
# for customer in range(1,51):
#     if time_list in range(1,16)
#     continue 
# elif time_list in range(16,51):

# from random import *

# cnt = 0 #총 탑승 승객 수
# for i in range(1, 51): # i는 1~50이라는 승객 수
#     time =  randrange(5, 51) # 5~50분 소요 시간
#     if 5 <= time <= 15: #5분~ 15분 이내의 손님(매칭 성공), 탑승 승객 수 증가 처리
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else: #매칭 실패한 경우
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print("총 탑승 승객 : {0} 분".format(cnt))

#함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# open_aacount()

# def deposit(balance, money): #입금(잔액, 입금할 금액)
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금(잔액, 출금할 금액)
#     if balance >= money: #잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁에 출금, 수수료가 발생한다고 가정
#     commission = 100 #수수료 100원
#     return commission, balance - money -commission

# balance = 0 #잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)   
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500) 
# print("수수료는 {0}원이며, 잔액은 {1}입니다.".format(commission, balance))

#기본값
# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))
    
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교 같은 학년 같은 반 같은 수업. -> 기본 값

# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang))
    

# profile("유재석")
# profile("김태호")

#keyword값 이용 함수 호출
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
    
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age = 26, name="김태호")


#QUIZ
# from random import *
# cnt = 0 
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt +=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        
#     print("총 탑승 승객 : {0} 분".format(cnt))
    

#가변인자를 활용한 함수 호출

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {}\t나이 : {}\t".format(name,age), end=" ")
#     #end= " " -> 위 문장 다음에 이어서 다른 문장을 출력하겠다는 뜻
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
#     #end= " " -> 위 문장 다음에 이어서 다른 문장을 출력하겠다는 뜻
#     for lang in language:
#         print(lang, end=" ")
#     print()    
# profile("유재석", 20, "python", "java", "C","C++","C#","javascript")
# profile("김태호", 24, "kortlin","swift")

#이런식으로 김태호는 언어를 두개밖에 못하지만 조건에 맞추기 위해 ""처리를 해서 추가로 3개를 넣어줬고
#유재석의 경우 언어를 하나 더 공부해서 하나 더 넣고 싶은데, 조건이 5개의 언어만 되어 있기 때문에
#lang6을 추가로 넣어줘야한다. 이 복잡한 경우를 해결할 수 있는게 가변인자!!!
#indentation(들여쓰기)가 매우 중요한데, for 구문에서 마지막 print()를
#for keyword에 적용되지 않게 써야 (들여쓰기 안되도록)
#이름 : 유재석   나이 : 20        python java C C++ C# javascript 
#이름 : 김태호   나이 : 24        kortlin swift
#이런식으로 선생님과 동일한 결과값이 노출이 되고
#for keyword에 적용되게 (들여쓰기 되도록) 쓰면
# 이름 : 유재석   나이 : 20        python 
# java 
# C 
# C++ 
# C# 
# javascript 
# 이름 : 김태호   나이 : 24        kortlin 
# swift 
#이렇게 노출됨..!!! indentation 주의 !!!!

#지역 변수와 전역 변수
#지역 변수 : 함수 내에서만 쓸 수 있는 것, 함수 호출될때만 만들어졌다가 함수 호출 끝나면 사라진다.
#전역 변수 : 모든 프로그램 내에, 모든 공간 내에서 어디서든 부를 수 있는 변수를 전역 변수라고 한다.

#군대 예를 들어보자
# gun = 10

# def checkpoint(soldiers): #경계근무
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))
    
#이대로 출력하면 
# 전체 총 : 10
# [함수 내] 남은 총 : 18
# 남은 총 : 10
#이렇게 출력되는데, 이게 바로 지역 변수다!
#처음 지정한 gun은 변하지 않는 외부 변수값이고
#def 함수 내에서 gun을 다시 지정해 주지 않으면 오류가 생기고(지역 변수 특징)
#def 함수내에서 gun을 반드시 설정해야지만 출력하면 "[함수 내] 남은 총 : 18"이 출력되고
#아닌 경우는 출력되지 않는다!!!

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun  #global 넣어주면 전역 공간의 gun을 쓰겠다(위의 gun = 10를 쓰겠다는 뜻)
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# print("전체 총 : {0}".format(gun))
# checkpoint(2) #2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8
#이렇게 출력됨!!

#전역 변수는 권장되는 방법은 아니다! 많이 쓰면 코드 관리가 떨어짐!!
#가급적 함수의 전달값 = 파라미터로 던져서 계산하고, 반환값을 받아서 쓰는 방법이 일반적!

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun  #global 넣어주면 전역 공간의 gun을 쓰겠다(위의 gun = 10를 쓰겠다는 뜻)
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
    
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
    
# print("전체 총 : {0}".format(gun))
# # checkpoint(2) #2명이 경계 근무 나감
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))

##출력값
# 전체 총 : 10
# [함수 내] 남은 총 : 8
# 남은 총 : 8
# 위와 같은 결과지만 다르게 적용됨!
# gun = checkpoint_ret(gun,2) 여기서 바로 checkpoint_ret함수로 적용되는데,
# checkpoint_ret(gun,2) 이 괄호안 gun이 외부의 gun = 10이 적용된 값이고!
# 이걸 def checkpoint_ret(gun, soldiers): 함수 내에서 계산 적용한 값으로!
# gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun
#이 순서대로 적용되고 마지막으로 계산된 8이라는 값이 return gun으로 출력되어
# gun-> 이 gun에 출력값 8이 들어가고 = checkpoint_ret(gun,2) 
# 그 다음 마지막 print("남은 총 : {0}".format(gun))여기에 gun=8이 적용되어
# 보여지는 것임!!!

# QUIZ

# 표준 체중을 구하는 프로그램을 작성하시오

# *표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1: 표준 체중은 별도의 함수 내에서 계산
#         *함수명 : std_weight
#         *전달값 : 키(height), 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# def std_weight(height, gender):
#     height = height * 0.01
#     if gender == "woman":
#         std_weight = height * height * 21
#         print("키 {0}m 여자의 표준 체중은 {1:.2f}kg 입니다.".format(height,std_weight))
#     else: 
#         std_weight = height * height * 22
#         print("키 {0}m 남자의 표준 체중은 {1:.2f}kg 입니다.".format(height, std_weight))

# std_weight(175, "man")
# print(std_weight)

#####내가 만든 답변의 결과값 #####
# 키 1.75m 남자의 표준 체중은 67.38kg 입니다.

#정답은
# def std_weight(height,gender): #키 m단위(실수), 성별 "남자"/ "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
    
# height = 175 #cm 단위
# gender = "남자"
# weight = std_weight(height / 100, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
#결과값 = 키 175cm 남자의 표준 체중은 67.375kg 입니다. 로 보여짐!
#but 우리는 소수점 둘째 자리까지 표시해야함
# def std_weight(height,gender): #키 m단위(실수), 성별 "남자"/ "여자"
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
    
# height = 175 #cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#표준 입출력

# print("python", "java") # python java 요케 출력
# print("python"+ "java") # pythonjava 요렇게 출력


# print("python", "java", sep=",") # python,java
# print("python", "java", "javascript", sep=" vs ") 
# python vs java vs javascript 이렇게 콤마 사이 값을 sep을 활용하여 대체값을 넣어 줄 수 있음.

# print("python", "java", sep=",", end="?") #end="?"는 문장 끝부분에 ?를 붙여라.
# print("무엇이 더 재밌을까요?")
# # python,java?무엇이 더 재밌을까요? -> 한 줄에 나온다!

# import sys
# print("python", "java", file=sys.stdout) #python java
# print("python", "java", file=sys.stderr) #python java

#두 경우 모두 파이썬에서는 차이 없이 동일한 결과값으로 노출된다.
#stdout = 표준 출력
#stderr = 표준 에러
# 표준 출력(stdout)과 표준 에러(stderr)는 모두 출력을 다루지만, 용도가 다릅니다. stdout은 주로 프로그램이 의도하는 작업 결과를 보여줄 때 사용되며, stderr는 주로 예상치 못한 에러나 경고를 출력하는 데 사용됩니다

#시험 성적 딕셔너리!!(key, value 필요!!)
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #여기서 subject가 key, score가 value로 쌍으로 tuple 형태로 보여준다.
#     # print(subject.ljust(8), score)
#     # 수학       0
#     # 영어       50
#     # 코딩       100
    
#     print(subject.ljust(8), str(score).rjust(4), sep=":")
    # 수학      :   0
    # 영어      :  50
    # 코딩      : 100
    
# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num))
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5
# 대기번호 : 6
# 대기번호 : 7
# 대기번호 : 8
# 대기번호 : 9
# 대기번호 : 10
# 대기번호 : 11
# 대기번호 : 12
# 대기번호 : 13
# 대기번호 : 14
# 대기번호 : 15
# 대기번호 : 16
# 대기번호 : 17
# 대기번호 : 18
# 대기번호 : 19
# 대기번호 : 20

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
# 대기번호 : 004
# 대기번호 : 005
# 대기번호 : 006
# 대기번호 : 007
# 대기번호 : 008
# 대기번호 : 009
# 대기번호 : 010
# 대기번호 : 011
# 대기번호 : 012
# 대기번호 : 013
# 대기번호 : 014
# 대기번호 : 015
# 대기번호 : 016
# 대기번호 : 017
# 대기번호 : 018
# 대기번호 : 019
# 대기번호 : 020

# answer = input("아무 값이나 입력하세요.")
# answer = 10
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")

# 아무 값이나 입력하세요.123
# 입력하신 값은123입니다.

# 아무 값이나 입력하세요.나도코딩
# 입력하신 값은나도코딩입니다.

#이런식으로 숫자도 스트링도 잘 출력되는걸 볼 수 있음.

#input을 활용해서 사용자 입력값을 입력하면 숫자든 글자든 무조건 str형태로 출력해준다.

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print(subject.ljust(8), str(score).rjust(4), sep=":")
# print("{0: >10}".format(500)) #       500
# # print("{0: >10}".format(-500))
# #위의 프린트문에서도       -500 음수값 표시는 가능하나 양수일때는 +없이 숫자만 노출됨
# #따라서 +,- 표시해주고 싶을때는 아래와 같이 표기해줘야한다!!
# # 양수일 때는 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500)) #      +500
# print("{0: >+10}".format(-400)) #      -400
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500)) #+500______
# # print("{0:_<10}".format(500))  #500_______
# # print("{0:_<+10}".format(-500))#-500______
# # 3자리 마다 콤마를 찍어주기
# print("{0:,}".format(1000000000000)) #1,000,000,000,000
# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(1000000000000)) #+1,000,000,000,000
# print("{0:+,}".format(-1000000000000)) #-1,000,000,000,000
# #돈이 많을수록 행복하니까 빈 자리는 ^로 채워주기
# # 왼쪽정렬,부호,30자릿수 확보,3자리마다","찍기
# print("{0:^<+30,}".format(-2000000000000))
# #소수점 출력
# print("{0:f}".format(5/3)) 1.666667
# #소수점을 특정 자릿수까지만 출력하고 싶오!
# # (e.g.소수점 둘째자리까지/ 소수점 3째 자리에서 반올림해줘!!!!!)
# print("{0:.2f}".format(5/3)) #1.67

#파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") 
#                 # score_txt파일을 write(쓰기) 용도로 열고, 
#                 # utf8로 정의해줘야 한글이 안깨짐
# print("수학 : 0", file =score_file)
# print("영어 : 50", file =score_file)
# score_file.close() #-> 연 파일을 꼭 이렇게 닫아줘야 한다!

# score_file = open("score.txt", "a", encoding="utf8") 
#         #이미 존재하는 score_txt에 append 덧붙이겠다는 의미의 "a"
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# #위의 명령문과 달리 줄바꿈이 없기 때문에 \n을 넣어줌!
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# #score_txt 파일을 read(읽어오겠다)라는 뜻
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# abc = "hello"
# print(type(abc))
# print(score_file.readline(), end="") #줄별로 읽기 동작 수행, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print("hello".endswith("o"))
# print(abc.endswith("c"))
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line: 
#         break
#     print(line, end="")
# score_file.close()

# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100
#파일이 몇 줄일지 모를때는, 이런식으로 while반복문 사용해서
#파일 내용 볼 수 있다.

#end=""
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100%  

# score_file = open("score.txt","r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line, end="")
    
# score_file.close()

#pickle = 프로그램 내에서 사용하는 데이터를 파일 형태로 저장하는 것
# import pickle
# profile_file = open("profile.pickle", "wb")
# #"w"를 쓰는 이유는 write하기 위해서 "b"를 붙여 써주는건 binary의 의미
# #pickle을 쓸때는 무조건 wb를 써줘야함.
# # pickle 모듈을 사용할 때 "wb" 모드로 파일을 열라는 조언은 
# # pickle로 데이터를 파일에 쓸 때 사용됩니다. 
# # 여기서 "wb"는 "write binary"의 약자로, 
# # 파일을 이진(binary) 모드로 쓰기 위해 사용됩니다.

# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 정보를 file에 저장 
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #file 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())
#     # 파이썬을 열심히 공부하고 있어요.
    
# Quiz) 당신의 회사에서는 매주 1회 작성해야하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 : 
# 이름 : 
# 업무 요약 :
    
# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt' ...와 같이 만듭니다.
#<내가 만들어본 답>
# score_file = open("X주차.txt", "w", encoding="utf8") 
#                 # score_txt파일을 write(쓰기) 용도로 열고, 
#                 # utf8로 정의해줘야 한글이 안깨짐
# print("- X 주차 주간보고 -", file =score_file)
# print("부서 : ", file =score_file)
# print("이름 : ", file =score_file)
# print("업무 요약 : ", file =score_file)
# score_file.close() #-> 연 파일을 꼭 이렇게 닫아줘야 한다!

# <정답>
# for i in range(1,51):
#     with open(str(i)+"주차.txt", "w", encoding= "utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

#class

