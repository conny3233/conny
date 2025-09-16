# 📌  문제설명
# A는 N x M 크기의  직사각형  형태의  미로에  갇혀  있다. 미로에는  여러  마리의  괴물이  있어  이를  피해  탈출해야 한다.
# 현재  위치는 (1, 1)이고  미로의  출구는 (N,M)의  위치에  존재하며  한  번에  한  칸씩  이동할  수  있다.
# 괴물이  있는  부분은 0으로, 괴물이  없는  부분은 1로  표시되어  있다. 미로는  반드시  탈출할  수  있는  형태로  제시 된다.
# 탈출하기  위해  움직여야  하는  최소  칸의  개수를  구하라. 칸을  셀  때는  시작  칸과  마지막  칸을  모두  포함해서  계 산한다.
# 📌입력
# 첫째  줄에  두  정수 N, M(4 <= N, M <= 200)이  주어진다.
# 다음 N개의  줄에는  각각 M개의  정수(0혹은 1)로  미로의  정보가  주어진다.
# 각각의  수들은  공백  없이붙어서  입력으로  제시된다. 또한  시작  칸과  마지막  칸은  항상 1이다. 📌출력
# 첫째  줄에  최소  이동  칸의  개수를  출력한다.

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    while queue: 
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:   #범위 벗어났을 때
                continue
            if graph[nx][ny] == 0:                       #괴물 만났을 때
                continue
            if graph[nx][ny] == 1:                       # 처음 방문하는 길(1)이면 → 이전 거리 + 1 저장
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(BFS(0, 0))
