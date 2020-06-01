def login(userid, userpw):
    id = 'KIT'
    pw = '2B'

    if id == userid and pw == userpw:
        return True
        
    else:
        return False

id = input("아이디 : ")
pw = input("패스워드 : ")

if login(id, pw):
    print("로그인 성공")
else:
    print("로그인 실패")


name = input("이름을 입력해 주세요 : ")
age = input("나이를 입력해 주세요 :")
if age.isdigit():
    number_age_a = int(age)
    print("%d 살로 지정되었습니다.", age)
else:
    print("숫자만 입력해 주십시오.")


아이템 = {
    "무기": ['1 : 주먹','2 : 칼'],
    "아이템": ["후레쉬","조명탄"]        
}

print(name, "님 반갑습니다. 게임을 시작 합니다.")
print("....")
print("어떤 건물을 발견하였습니다. 들어가 보시겠습니까?")
print("....")
print("1.들어가본다 2.들어가지 않는다.")
sel = input("당신의 선택 : ")
if float(sel) < 2 :
    print("당신은 건물을 들어가보기로 했습니다.")
    print("...")
    print("당신은 건물 내부에 들어왔습니다. 무엇을 하시겠습니까?")
    print("1.수색하기 2.나가기")
    sel2 = input("당신의 선택 : ")
    if float(sel2) < 2:
        print("건물 내부를 수색합니다.")
        print("...")
        print("건물 내부에는 좀비가 있었습니다! 어떻게 하시겠습니까?")
        print("1.싸운다 2.도망친다")
        sel3 = input("당신의 선택 : ")
        if float(sel3) < 2:
            print("어떤 무기를 사용하시겠습니까?", 아이템["무기"])
            sel4 = input("사용할 무기 : ")
            if float(sel4) < 2:
                print("당신은 주먹을 이용해 좀비와 싸웠으나 사망했습니다.")
                print("GAME OVER")
            else:
                print("당신은 칼을 이용해 좀비를 물리쳤습니다.")
        else:
            print("당신은 도망치는데 성공했습니다.")
    else:
        print("건물을 나갑니다.")
else:
    print("당신은 건물을 그냥 지나치기로 했습니다.")

