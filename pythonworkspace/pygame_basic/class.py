'''
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.locaion=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
        print("검색 결과 : {} {} {} {} {}".format(location, house_type, deal_type, price, completion_year))


House("강남", "아파트", "매매", "10억", "2010년")
House("마포", "오피스텔", "전세", "5억", "2007년")
House("송파", "빌라", "월세", "500/50", "2000년")
'''

'''
정답
'''
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.locaion=location
        self.house_type=house_type
        self.deal_type=deal_type
        self.price=price
        self.completion_year=completion_year
    def show_detail(self):
        print(self.locaion, self.house_type, self.deal_type, self.price, self.completion_year)


all_houses=[]
house1=House("강남", "아파트", "매매", "10억", "2010년")
house2=House("마포", "오피스텔", "전세", "5억", "2007년")
house3=House("송파", "빌라", "월세", "500/50", "2000년")
#↑리스트에 넣을 변수 만들 때 꼭! House 클래스 써서 넣기. House 안 쓰고 house1=("강남"...)
#이렇게만 선언해서 for문 house.show_detail()에서 계속 show_detail이 정의되지 않았다고 오류남. 

all_houses.append(house1)
all_houses.append(house2)
all_houses.append(house3)

print("총 {}개의 매물이 있습니다.".format(len(all_houses)))
for house in all_houses :
    house.show_detail()