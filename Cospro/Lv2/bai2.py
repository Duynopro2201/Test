# Có thể sử dụng import như dưới đây.
#import math

def solution(watering_can, N, M):

    NO_WATER = 0
    WATER = 1

    garden = [[NO_WATER] * N for i in range(N)]

    for i in range(M) :
        can = watering_can[i]
        garden[can[0]][can[1]] = WATER
        for j in range(1,can[2]+1):
            if can[0]+j < N:
                garden[can[0]+j][can[1]] = WATER
            if can[0]-j >= 0:
                garden[can[0]-j][can[1]] = WATER
            if can[1]+j < N:
                garden[can[0]][can[1]+j] = WATER
            if can[1]-j >= 0:
                garden[can[0]][can[1]-j] = WATER

    answer = 0

    for i in range(N):
        for j in range(N):
            if garden[i][j] == NO_WATER:
                answer += 1

    return answer


# Dưới đây là code kiểm thử output testcase, code này đã chính xác nên vui lòng không chỉnh sửa, chỉ chỉnh sửa nội dung code phía trên.
watering_can1 = [[2,2,2],[0,0,1]]
N1 = 5
M1 = 2
ret1 = solution(watering_can1, N1, M1)
# Bạn có thể xem các giá trị đầu ra bằng cách nhấn nút [Run].
print("solution 함수의 반환 값은", ret1, "입니다.")


