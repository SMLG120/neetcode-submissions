class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            # greedily consumes tickets until there are none left from this airport
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            # if we are stuck, this airport is the end of the current sub-path
            res.append(src)
        dfs('JFK')
        return res[::-1]
        
        