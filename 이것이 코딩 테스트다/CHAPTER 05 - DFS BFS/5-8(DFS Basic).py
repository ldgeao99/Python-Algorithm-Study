def dfs(graph, v, visited):
  # 함수가 호츨된다함은 곧 해당 노드에 대한 방문이다.
  print(v, end=" ")
  visited[v] = True
  # 노드 자신과 연결된 다른 노드가 방문되지 않았을 경우 방문을 재귀적으로 진행한다.
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


# 1~8번 까지의 노드가 존재. 그리고 각각의 노드는 다음과 같이 연결되어있음
# (가중치 없는 인접리스트 형태)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

visited = [False] * 9

dfs(graph, 1, visited)

#142p.에 존재하던 기본 DFS 코드
# 정답은 1 2 7 6 8 3 4 5