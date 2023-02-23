from collections import deque


def bfs(graph, start, visited):

  deq = deque([start])  #deq=deque(), deq.append(start)와 같은 의미
  visited[start] = True

  # 큐가 완전히 빌 떄 까지 반복
  while deq:

    v = deq.popleft()
    print(v, end=" ")

    for i in graph[v]:
      if not visited[i]:
        deq.append(i)
        visited[i] = True


# 1~8번 까지의 노드가 존재. 그리고 각각의 노드는 다음과 같이 연결되어있음
# (가중치 없는 인접리스트 형태)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

visited = [False] * 9

bfs(graph, 1, visited)
