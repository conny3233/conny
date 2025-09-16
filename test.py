def dfs(graph, start):
    visited = set()      # 방문한 정점 기록
    stack = [start]      # 탐색 후보 (LIFO 스택)
    route = []           # 실제 방문 순서 기록

    while stack:
        v = stack.pop()              # 스택에서 하나 꺼냄
        if v not in visited:         # 아직 방문 안 했으면
            visited.add(v)           # 방문 처리
            route.append(v)          # 방문 경로에 기록
            # 이웃들을 스택에 추가 (뒤에 넣은 게 먼저 나오므로 역순으로 넣으면 재귀 DFS 순서와 같음)
            for neighbor in reversed(graph[v]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return route

# 그래프 예시
graph = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [],
    5: []
}

print(dfs(graph, 0))   # 출력: [0, 1, 3, 4, 2, 5]
