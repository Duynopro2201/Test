# Có thể sử dụng import như dưới đây.
#import math

def solution(arr, N):
    answer = 0
    for i in range(N):
        a, b = arr[i]
        c = gcd(a, b)
        if c > answer:
            answer = c

    return answer


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
arr1 = [[15,20],[36,48],[12,7],[121,44],[39,65]]
N1 = 5
ret1 = solution(arr1, N1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")

arr2 = [[356,78],[154,122],[38,190],[44,188],[365,245]]
N2 = 5
ret2 = solution(arr2, N2)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret2, "입니다.")


