#https://school.programmers.co.kr/learn/courses/30/lessons/1844
#DFS/BFS

from collections import deque

def solution(maps):
    answer = 0

    # 이동할 네 방향 정의(상,하,좌,우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # BFS 소스코드 구현
    def bfs(x, y):
        
        queue = deque()
        queue.append((x, y))

        # 큐가 빌 떄까지 반복
        while queue:
            x, y = queue.popleft()

        # 현재 위치에서 네 방향으로부터의 위치 확인
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                # 미로 찾기 공간을 벗어난 경우 무시
                if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]): continue
                # 벽인 경우 무시
                if maps[nx][ny] == 0: continue
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))

        # 가장 오른쪽 아래까지의 최단 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0,0)
    return -1 if answer == 1 else answer