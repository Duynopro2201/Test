# Có thể sử dụng import như dưới đây.
#import math

RED = 1
BLUE = 2
GRAY = 3

def solution(N, M, area, C):
    paper = [[0] * N for _ in range(N)]

    for i in range(M):
        target = area[i]
        from_r, from_c = target[0], target[1]
        to_r, to_c = target[2], target[3]
        color = target[4]

        for r in range(from_r, to_r + 1):
            for c in range(from_c, to_c + 1):
                if paper[r][c] == 0:
                    paper[r][c] = color
                elif (paper[r][c] != color):
                    paper[r][c] = GRAY

    answer = 0

    for r in range(N):
        for c in range(N):
            if C == paper[r][c]:
                answer += 1

    return answer


# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
N1 = 10
M1 = 2
area1 = [[1,1,5,4,1],[2,3,6,6,2]]
C1 = 3
ret1 = solution(N1, M1, area1, C1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")

N2 = 10
M2 = 2
area2 = [[1,1,5,4,1],[2,3,6,6,1]]
C2 = 3
ret2 = solution(N2, M2, area2, C2)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret2, "입니다.")


