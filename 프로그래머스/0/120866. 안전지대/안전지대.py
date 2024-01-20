def solution(board):
    risk_num = 0
    n = len(board)

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    risk = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                risk_num += 1
                continue
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    if board[nx][ny] == 1:
                        risk[x][y] = True
            if risk[x][y]:
                risk_num += 1
    
    answer = n * n - risk_num
    
    return answer