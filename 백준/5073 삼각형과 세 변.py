while 1:
    li = sorted(list(map(int, input().split())))
    if li[0] == li[1] == li[2] == 0:
        break
    if li[0]+li[1] <= li[2]:
        print("Invalid")
    elif li[0] == li[1] == li[2]:
        print("Equilateral")
    elif li[0]==li[1] or li[1]==li[2] or li[2]==li[0]:
        print("Isosceles")
    else:
        print("Scalene")
# 2 2 8 처럼 Invalid 이지만 Equilateral 조건에도 해당할 수 있기 때문에 Invalid를 가장 맨 앞 순서에 넣어주어야 하는 것이 포인트인 문제이다.
