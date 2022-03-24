import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(N-1):
    node1, node2 = map(int, input().split())
    nodes[node1].append(node2)
    nodes[node2].append(node1)

def BFS():
    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        for idx in nodes[node]:
            if parents[idx] == 0:
                parents[idx] = node
                queue.append(idx)

BFS()

for parent in parents[2:]:
    print(parent)