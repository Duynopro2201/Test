# Có thể sử dụng import như dưới đây.
#import math

def solution(arr):
    answer = 1
    N = 10

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                length = 0
                for w in range(2, 11):
                    is_square = True
                    for di in range(i, [[quiz]]):
                        for dj in range(j, [[quiz]]):
                            if [[quiz]]:
                                is_square = False
                                break
                        if not is_square:
                            break

                    if is_square:
                        length = w
                    else:
                        break

                if length > 1:
                    for di in range(i, [[quiz]]):
                        for dj in range(j, [[quiz]]):
                            arr[di][dj] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                return 0

    return 1

# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
arr1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]]
ret1 = solution(arr1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")

arr2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
ret2 = solution(arr2)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret2, "입니다.")

arr3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0, 1, 1], [0, 1, 1, 1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]]
ret3 = solution(arr3)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret3, "입니다.")


