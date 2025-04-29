import heapq

graph = {
    'A': [['B', 5], ['C', 10]],  # A <-> B with cost 5, A <-> C with cost 10
    'B': [['A', 5], ['D', 3]],   # B <-> A with cost 5, B <-> D with cost 3
    'C': [['A', 10], ['D', 7]],  # C <-> A with cost 10, C <-> D with cost 7
    'D': [['B', 3], ['C', 7],['E',7]],    # D <-> B with cost 3, D <-> C with cost 7
    'E': [['F', 3], ['D', 7]],    # D <-> B with cost 3, D <-> C with cost 7
    'F': [['E', 3], ['C', 4]]    # D <-> B with cost 3, D <-> C with cost 7
}
st=set()
op={'A':0,'B':float("inf"),'C':float("inf"),'D':float("inf"),'E':float("inf"),'F':float("inf")}

hp=[['A',0]]

heapq.heapify(hp)
while hp:
    
    z=heapq.heappop(hp)
    if z[0] in st:
        continue
    for i in graph[z[0]]:
        v=[i[0],i[1]+z[1]]
        if v[1]<op[v[0]]:
            op[v[0]]=v[1]
            heapq.heappush(hp,v)
    st.add(z[0])

print(op)




