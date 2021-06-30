from collections import deque
# 처음 문제를 접근할 때는 DFS를 활용하여 진행하였음. 하지만 여러 테스트 케이스에서 문제점이 발견됨
# BFS를 활용하여 문제를 해결하였음. 

def next_step(maps, p):
    nexts = deque()
    n = len(maps) # row size
    m = len(maps[0]) # col size

    # (down, right, up, left)
    for t in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= p[0] + t[0] < n and 0 <= p[1] + t[1] < m:
            if maps[p[0]+t[0]][p[1]+t[1]] == 1:
                nexts.append((p[0]+t[0], p[1]+t[1]))

    return nexts


def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])

    end = (n-1, m-1)
    begin = (0, 0)
    maps[0][0] = 0
    begin_item = [begin, 1] # [point, cnt]

    q = deque([begin_item])
    while q:
        current, cnt = q.popleft()

        if current == end:
            return cnt

        nxts = next_step(maps, current)
        for nxt in nxts:
            q.append([nxt, cnt+1])
            maps[nxt[0]][nxt[1]] = 0

    return answer