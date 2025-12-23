# Có thể sử dụng import như dưới đây.
#import math

def solution(arr, N, M):
    min_sum = 50000
    max_sum = 0

    for i in range(N-M+1):
        temp_max = 0
        for j in range(i, i+M):
            temp_max += arr[j]
        if temp_max > max_sum:
            max_sum = temp_max
        if temp_max < min_sum:
            min_sum = temp_max

    return max_sum - min_sum

# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
arr1 = [3,1,1,4,5,9]
N1 = 6
M1 = 3
ret1 = solution(arr1, N1, M1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")

arr2 = [3,1,1,4,5,9]
N2 = 6
M2 = 2
ret2 = solution(arr2, N2, M2)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret2, "입니다.")

arr3 = [1,2,3,4,5,6]
N3 = 6
M3 = 4
ret3 = solution(arr3, N3, M3)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret3, "입니다.")




