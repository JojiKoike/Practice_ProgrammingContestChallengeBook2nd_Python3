# Get Number of vertex and edge
V, E = map(int, input().split(" "))

# Build Graph Data
G = [[] for i in range(E)]
for i in range(E):
    s, t = map(int, input().split(" "))
    G[s].append(t)
    G[t].append(s)

for g in G:
    print(g)



