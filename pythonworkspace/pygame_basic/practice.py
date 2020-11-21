'''
# 표준체중 공식 (여)=키m*키m*21 / (남)=키*키*22

def std_weight(height, sex):
    if sex=="여자" :
        return height**2*21
    else :
        return height**2*22
    
height=input("키(cm) : ")
sex=input("성별 : ")
weight=round(std_weight(float(height)/100, sex), 2)

print("키 {0}(cm) {1}의 표준체중은 {2}(kg)입니다".format(height, sex, weight))
'''
'''
- X 주차 주간 보고 -
부서 : 
이름 : 
업무요약 :

1주차부터 50주차까지 보고서 만드는 프로그램 작성
조건 : 파일명은 1주차.txt, 2주차.txt...

for i in range(1,51):
    with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0}주차 주간 보고 -\n부서 :\n이름 :\n업무요약 :".format(i))
'''
'''
서명
import byme
byme.sign()
'''