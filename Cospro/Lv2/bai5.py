#Có thể sử dụng import như dưới đây.
#import math

def solution(board):
    min_avg = 100
    max_avg = 0

    for i in range(5):
        sum_x = 0
        sum_y = 0
        for j in range(5):
            sum_x += board[i][j]
            sum_y += board[j][i]

        sum_x = int(sum_x / 5)
        sum_y = int(sum_y / 5)

        if max_avg < sum_x:
            max_avg = sum_x
        if max_avg < sum_y:
            max_avg = sum_y
        if min_avg > sum_x:
            min_avg = sum_x
        if min_avg > sum_y:
            min_avg = sum_y

    sum_d1 = 0
    sum_d2 = 0
    for i in range(5):
        sum_d1 += board[i][i]
        sum_d2 += board[-i][-i]

    sum_d1 = int(sum_d1 / 5)
    sum_d2 = int(sum_d2 / 5)

    if max_avg < sum_d1:
        max_avg = sum_d1
    if max_avg < sum_d2:
        max_avg = sum_d2
    if min_avg > sum_d1:
        min_avg = sum_d1
    if min_avg > sum_d2:
        min_avg = sum_d2

    return min_avg + max_avg

# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
board1 = [[25,11,82,61,34],[87,98,91,76,95],[44,2,39,57,65],[69,32,51,16,41],[94,27,74,37,9]]
ret1 = solution(board1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")


