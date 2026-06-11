class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod=10**9+7
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        self.max_depth=0
        def dfs(cur, parent, depth):
            if depth > self.max_depth:
                self.max_depth = depth
                
            for neighbor in adj[cur]:
                if neighbor != parent:
                    dfs(neighbor, cur, depth + 1)
        dfs(1,-1,0)
        return pow(2,self.max_depth-1,mod)
