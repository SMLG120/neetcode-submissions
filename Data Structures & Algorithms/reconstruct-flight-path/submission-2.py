class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not adj[curr]:
                # pop the airport and add it to the result.
                res.append(stack.pop())
            else:
                # If it has outgoing flights, pop one and push the destination.
                stack.append(adj[curr].pop())
        return res[::-1]
