import sys
input = sys.stdin.readline

N = int(input())
voteCnt = int(input())
picture = []
score = []

for studentNum in list(map(int, input().split())):
    if studentNum in picture:   # 사진틀에 있으면
        for j in range(len(picture)):
            if studentNum == picture[j]:
                score[j] += 1
    else:   # 사진틀에 없으면
        if len(picture) >= N:    # 사진이 꽉차면
            for j in range(N):
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break
        picture.append(studentNum)
        score.append(1)
picture.sort()
print(' '.join(map(str, picture)))