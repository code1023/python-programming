'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

 
(성별에 따른 공식)

 남자 : 키(m) * 키(m) * 22

 여자 : 키(m) * 키(m) * 21

 
조건1 : 표준 체중은 별도의 함수 내에서 계산

        * 함수명 : std_weight 

        * 전달값 : 키(height), 성별(gender)

조건2 : 표준 체중은 소수점 둘째자리까지 표시

 
(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''


def std_weight(height, gender):
    height = height / 100
    if gender == "남자":
        weight = height * height * 22
        return round(weight, 2)
    else:
        weight = height * height * 21
        return round(weight, 2)


height = int(input('키 (cm) : '))
gender = input('성별 (남자/여자) : ')
weight = std_weight(height, gender)
print(f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.')
