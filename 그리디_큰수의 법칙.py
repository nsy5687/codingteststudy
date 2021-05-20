import time#시간에 대한 라이브러리

n, m, k = map(int,input().split())
 #map함수는 고차함수이며 리스트의 항목마다 각각 함수를 적용해주는 함수
 #map(함수,리스트)
data = list(map(int,input().split()))

start_time=time.time()

data.sort()
first = data[n-1]
second = data[n-2]#파이썬에서 n보다 뺏기수의 절대값이 커서 마이너스가 되어도 실행은 되지만 이상해질 수 있다 (예 : 인덱스 -1은 n-1과 같다)

result = 0

while True :
    for i in range(k):#for문으로 제일 큰 수를 k번을 더한다
        if m == 0: #m번을 다하면 for문 탈출
            break
        result += first
        m-=1 #아니면 더하면서 횟수(m)를 감소
    if m == 0:#제일 큰 수를 k번만큼 다 더하고 횟수(m)를 확인
        break
    result += second#횟수가 남아 있으면 두번째로 큰 수를 더함
    m-=1#횟수(m)를 감소
end_time=time.time()


print(result)
print(end_time-start_time)