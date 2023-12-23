import os
import time

# 게임 맵
game_map = [
    "--------------------------------------",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "-                                    -",
    "--------------------------------------"
]

# 마리오 초기 위치
mario_x = 1
mario_y = 19

# 게임 루프
while True:
    # 게임 맵 출력
    os.system("cls" if os.name == "nt" else "clear")
    for row in game_map:
        print(row)

    # 사용자 입력 받기
    move = input("이동하실 방향을 입력하세요 (w: 위, s: 아래, a: 왼쪽, d: 오른쪽, q: 종료): ")

    # 종료
    if move == "q":
        print("게임을 종료합니다.")
        break

    # 이동
    next_x, next_y = mario_x, mario_y
    if move == "w":
        next_y -= 1
    elif move == "s":
        next_y += 1
    elif move == "a":
        next_x -= 1
    elif move == "d":
        next_x += 1

    # 이동 가능한지 확인
    if game_map[next_y][next_x] == " ":
        game_map[mario_y] = game_map[mario_y][:mario_x] + " " + game_map[mario_y][mario_x + 1:]
        mario_x, mario_y = next_x, next_y

    # 장애물에 부딪힘
    elif game_map[next_y][next_x] == "-":
        print("장애물에 부딪혔습니다!")
        time.sleep(1)

    # 목표지점 도착
    elif game_map[next_y][next_x] == "X":
        print("축하합니다! 목표지점에 도착했습니다!")
        break
