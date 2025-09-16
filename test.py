# 표준 체중을 구하는 프로그램 작성
# 남자: 키*키*22
# 여자: 키*키*21

# 조건1: 표준체중은 별도의 함수 내에서 계산
# 조건2: 표준체중은 소수점 둘째자리까지 표시

# ex) 키 175cm 남자의 표준 체중은 67.38kg입니다


def std_weight(height,gender):
    if gender == "남자":
        return (height/100)**2*22
    else:
        return (height/100)**2*21

print("키를 입력해주세요: ") 
height = float(input())
print("성별을 입력해주세요: ") 
gender = str(input())
weight = std_weight(height,gender)
print("키 {0:.0f}cm {1}의 표준 체중은 {2:.2f}kg입니다".format(height,gender,weight))