n = 1260
count = 0

coin_form = [500,100,50,10]
#coin_form=list(500,100,50,10)로 해서 넣으면 출력시 coin_form=list(500,100,50,10)로 출력 됨

for coin in coin_form:
    count += n//coin#//은 나눗셈을 하되 실수가 아닌 정수로 값을 반환

    n%=coin

print(count)