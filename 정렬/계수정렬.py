array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 계수정렬은 값의 특정범위가 지정 될 때 퀵 정렬보다 더 빨리 정렬할 수 있다
# 하지만 값이 0과 99999 단 두 값만 있으면 메모리낭비가 심하고 느리다

cash = [0] * (max(array)+1) #리스트 중 최대 값을 기준으로 cash(값의 유무와 갯수를 체크)리스트를 생성

#array의 값은 cash의 인덱스 값이며 이 때 cash값(갯수)은 1씩 증가

for i in array:
    cash[i] += 1

#cash의 각 인덱스 값을 cash값(갯수)만큼 출력
for i in range(len(cash)):
    for j in range(cash[i]):
        print(i, end=' ')
