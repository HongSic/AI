import pandas as pd
import numpy as np

#s = pd.Series([1, 3, 5, 7, 9])  # Series 데이터 생성, index 디폴트 생성
#print(s)
#s1=s.drop(3) #3번 index 삭제
#print(s1)

#arr=np.array([0,2,4,8,10])  #numpy 배열로  Series 데이터 생성
#s=pd.Series(arr)

# s=pd.DataFrame([[1,2,3],[4,5,6]])  #DataFrame 데이터 생성
# s = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])

# index
#s = pd.Series([1, 3, 5, 7, 9], index=['a','b','c','d','e'])  # Series 데이터 생성
#s1=s.drop('c')
#print(s1)

s = pd.DataFrame(np.random.randn(10, 7), columns=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# print(s[(5<s.index) & (s.index<10)]) # 5보타 크고 10보다 작은 인덱스에 해당되는 행을 출력
# print(s.head()) # 인덱스번소 상위 5개 출력
# print(s.head(7)) # 인덱스번호 상위 7개 출력
# print(s.tail())  # 인덱스번소 하위 5개 출력
#print(s.columns)  # columns 출력
# print(s.index)    # Index 출력
# print(s.describe()) #컬럼별로 통계 출력
# print(s['c'])  #'c' 컬럼 데이터만 출력
# print(s[['c','d']])  #'c','d' 컬럼 데이터만 출력
# print(s[2:5])  #index값 2 부터 4번까지 출력