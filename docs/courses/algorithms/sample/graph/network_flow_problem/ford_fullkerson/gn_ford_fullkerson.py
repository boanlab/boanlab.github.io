from asyncio import Queue

def ford_fullkerson(source, sink, capacity, flow):
    size, total_flow = len(capacity), 0
    INF = 1e8    

    while (True):
        parent = [-1] * size
        queue = Queue()
        parent[source] = source
        queue.put(source)

        # BFS
        while (not queue.empty() and parent[sink] == -1):
            now = queue.get()

            for i in range(0, size):
                if (capacity[now][i] - flow[now][i] > 0 and parent[i] == -1):
                    queue.put(i)
                    parent[i] = now
        
        if (parent[sink] == -1): break

        p, amount = sink, INF

        while (p != source):
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
            p = parent[p]
        
        p = sink

        while (p != sink):
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        
        total_flow += amount
    
    return total_flow 




        

    