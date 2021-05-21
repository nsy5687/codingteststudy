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

print(result)

#단순반복문은 시간초과가 날 수 있기 때문에 특정수열이 일정한 패턴으로 유지되면 수학적으로 풀어본다 

result = 0
count = int(m/(k+1)) * k 
#수열[6,6,6,5]가 반복적으로 나타나므로 이것을 수학적으로 나타내면 k+1이며 제일 큰 수가 나오는 횟수는 m/(k+1) x k이다
count += m%(k+1)# m/(k+1)로 나눠지지 않는 것에 대비하여 나눈 나머지 횟수도 더해준다

result+=count * first # 제일 큰 수를 횟수만큼 더한다
result+=(m-count) * second # 두 번째로 큰 수는 수열만큼 즉 m/(k+1) = m-count만큼 나온다


end_time=time.time()


print(result)
print(end_time-start_time)