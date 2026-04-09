def countComponents(n, links):
    # Build graph
    graph = {i: [] for i in range(n)}
    
    for u, v in links:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    count = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                stack.extend(graph[curr])

    # Count components
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1

    return count


# Input handling (HackerRank)
m = int(input("INPUT M****>").strip())
_ = int(input("INPUT _*****>").strip())  # always 2, ignore

links = []
for _ in range(m):
    u, v = map(int, input("U and V input ***>").split())
    links.append([u, v])

n = int(input().strip())

print(countComponents(n, links))
