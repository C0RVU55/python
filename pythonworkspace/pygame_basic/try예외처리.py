#1보다 작거나 숫자가 아닌 거 들어오면 valueerror 처리 : "잘못된 값을 입력하였습니다."
#대기 손님이 주문가능한 총 치킨량은 10마리. 소진시 사용자정의에러[soldouterror]발생 : "재고가 소진됐습니다"


class SoldOutError(Exception):
    pass


chicken=10
waiting=1
while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order=int(input("치킨 몇 마리 주문하시겠습니까?"))    
        if order > chicken:
            print("재고가 부족합니다.")
        elif order<=0:
            raise ValueError
        else:
            print("[대기번호{}] {}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting+=1
            chicken-=order

        if chicken==0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하셨습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break


    
