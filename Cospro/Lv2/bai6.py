# Có thể sử dụng import như dưới đây.
#import math

def solution(arr, N):

    frequency = [0] * (101)

    for i in range(N):
        frequency[arr[i]] += 1

    max = 0
    num = 0

    for i in range(len(frequency)):
        if max <= frequency[i]:
            max = frequency[i]
            if num < i:
                num = i

    return num

# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
arr1 = [1,2,3,4,4,5,6,7,7,8,9,9,9,9,10]
N1 = 15
ret1 = solution(arr1, N1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")

arr2 = [1,1,4,4,8,8,8,8,9,9,9,9,1,4,4,4,5,3,2,2,1,4,8,7]
N2 = 24
ret2 = solution(arr2, N2)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret2, "입니다.")

arr3 = [3,3,3,3,3,5,5,5,5,5,9,9,9,9,9,11,11,11,11,11]
N3 = 20
ret3 = solution(arr3, N3)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret3, "입니다.")


