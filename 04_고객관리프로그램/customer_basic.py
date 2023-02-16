#콘솔형 고객 정보 관리 시스템 구축

import re
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()  

    
    if choice=="I":
        customer={'name':'','gender':'',"email":'',"birthyear":''}        
        print("고객 정보 입력")
        customer['name'] = input('이름 >>> ')
        while True:
            customer['gender'] = input('성별(M,m or F,f) >>> ').upper()
            if customer['gender'] in ('M', 'F'):
                break
        
        while True:
            customer['email'] = input('이메일 >>> ')
            check = None
            for idx, i in enumerate(custlist):
                if i['email'] == customer['email']:
                    check = idx
                    break
            if check == None:
                p = re.compile('@[a-z]{2,}[.][a-z]{2,}')
                if p.search(customer['email']) != None:
                    break
                else:
                    print('@를 포함해 정확한 이메일을 입력하세요.')
            else:        
                print('중복되는 이메일이 있습니다.')

        while True:
            customer['birthyear'] = input('출생년도(4자리) >>> ')
            try:
                int(customer['birthyear'])
            except:
                print('숫자를 입력하세요.')
            else:
                if len(customer['birthyear']) == 4:
                    break
                else:
                    print('4자리로 입력해주세요.')
            print(customer)
            custlist.append(customer)
            page = len(custlist)-1


    elif choice=="C":
        print("현재 고객 정보 조회")

    elif choice == 'P':
        print("이전 고객 정보 조회")

    elif choice == 'N':
        print("다음 고객 정보 조회")


    elif choice=='D':
        print("고객 정보 삭제")
        key = email
        if email == custlist(email):
            del(email)
            print("고객 정보 삭제")
            delok = 1
        else:
            print('등록되지 않은 이메일입니다.')
            delok = 0
        pass

    elif choice=="U": 
        # print("고객 정보 수정")
        # key = email
        # if email == a:
        pass
    elif choice=="Q":
        print("프로그램 종료")
        break
    else:
        print('메뉴를 잘못 선택했습니다.')




# 절차적 - 함수 / 프로그램 -클래스
