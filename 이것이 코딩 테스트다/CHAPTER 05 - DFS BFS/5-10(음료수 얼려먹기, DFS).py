"""
#N, M 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

print(graph)
"""

graph = [
  [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
  [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
  [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
  [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
  [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
  [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
  [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
  [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
  [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
  [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
  [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
  [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
]

print(graph)

def dfs(x, y):
  #주어진 범위를 벗어나는 경우에는 즉시 종료(x, y 값은 각각 0~n, 0~m 이어야 함)
  if x<= -1 or x>= n or y<= -1 or y>= m:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    

result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1
      
print(result)


if x<0 or x>(n-1) or y<0 or y>(m-1)   :
  return False
if x<=-1 or x>=n or y<=-1 or y>=m   :
  return False
