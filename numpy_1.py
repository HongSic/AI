import numpy as np
data1 = [1, 2, 3, 4, 5]   #list  타입
print(data1, type(data1))


arr1 = np.array(data1)      #list타입을 array로 변환
print(arr1, type(arr1))


data2 = [[1., 2., 3., 4.], [5., 6., 7., 8]]
print (data2)

arr2 = np.array(data2)    #2차원 array로 변환
print(arr2, type(arr2))

print(arr1.ndim, arr2.ndim)   # numpy배열이 몇 차원인지 알려 줌

print(arr1.shape, arr2.shape)  #(차원 수, 1 차원 당 원소 갯수)

print(arr1.dtype, arr2.dtype)  #배열에 속한 자료형 타입

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)  # type : np.int32, np.float64
print(x)
x = x.astype(np.float64) #astype : type 바꾸기
print(x)

# 연산
'''
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[2, 3], [4, 5]])
print (arr1, arr2)
'''
# arr3 = arr1 + arr2  #두 배열의 차수가 맞아야 함
#arr2 = np.array([2, 3])
#arr3 = arr1 + arr2  #  [[1,2] + [2,3], [3,4] + [2,3]]  두 배열의 차수가 다를 경우
# arr3 = arr1 - arr2
# arr3 = arr1 * arr2
# arr3 = arr1 / arr2
# arr3 = arr1 ** arr2
# arr3 = np.matmul(arr1,arr2) #매트릭스 곱
