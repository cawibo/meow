
import sys

# bfs too slow for third to last test case
def solve_dfs(sr, sc, gr, gc):
	global map	
	
	# must be neither if different numbers
	if map[sr][sc] != map[gr][gc]:
		return "neither"

	kind = map[sr][sc]
	visited = set()
	queue = [(sr, sc)]

	while queue:
		current = queue.pop()
		visited.add(current)

		if current == (gr, gc):
			return "decimal" if kind else "binary" 

		r, c = current
		for n_r, n_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
			if n_r < 0 or n_c < 0 or n_r > len(map)-1 or n_c > len(map[0])-1:
				continue

			if map[n_r][n_c] == kind and (n_r, n_c) not in visited:
				queue.append((n_r, n_c))

	return "neither"

def get_cluster(sr, sc):
	global map

	cluster = set()
	kind = map[sr][sc]
	queue = [(sr, sc)]

	while queue:
		current = queue.pop()
		cluster.add(current)

		r, c = current
		for n_r, n_c in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
			if n_r < 0 or n_c < 0 or n_r > len(map)-1 or n_c > len(map[0])-1:
				continue

			if map[n_r][n_c] == kind and (n_r, n_c) not in cluster:
				queue.append((n_r, n_c))
	
	return cluster


# read map size from stdin
r, c = [int(e) for e in sys.stdin.readline().split()]

# read map from stdin
map = [[int(e) for e in sys.stdin.readline().rstrip()] for _ in range(r)]

# read n ( number of queries ) from stdin
n = int(sys.stdin.readline())
clusters = []
visited = set()

# handle queries
for _ in range(n):
	sr, sc, gr, gc = [int(e)-1 for e in sys.stdin.readline().split()]

	# print neither if differing kinds
	if map[sr][sc] != map[gr][gc]:
		print("neither")
		continue

	# add cluster if start node is unvisited
	if (sr, sc) not in visited:
		cluster = get_cluster(sr, sc)
		clusters.append(cluster)
		visited |= cluster

		# evaluate whether there is a connection between start and goal node
		if (gr, gc) in cluster:
			print( "decimal" if map[sr][sc] else "binary" )
		else:
			print("neither")
		continue
		
	# check existing clusters for start node
	for cluster in clusters:
		# if there is a connection, handle it
		if (sr, sc) in cluster and (gr, gc) in cluster:
			print( "decimal" if map[sr][sc] else "binary" )
			break

	# if no connection could be found
	else:
		print("neither")