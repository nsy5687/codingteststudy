array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()

print(array)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

print(sorted(array))

array2 = [('바나나',2),('사과',1),('배',3)]

def setting(data):
    return data[1]

#sorted함수에서 key파라미터 변수를 통해 정렬 기준을 지정할 수 있다
#sorted(리스트, key=함수나 람다식 함수)

print(sorted(array2, key=lambda x:x[1]))

#람다식 함수
# lambda 파라미터 : 리턴 값

F=lambda a=1, b=2: a+b
print(F())