import random

with open('flag.txt', 'r') as f:
	flag = f.read()

TREE_SIZE = 16
QUERY_LIMIT = 4

# --- start util functions ---
# convert preufer sequence to tree
def decode_preufer(sequence):
	degree = [1] * TREE_SIZE
	for item in sequence:
		degree[item] += 1
	
	leaves = set()
	for i in range(TREE_SIZE):
		if degree[i] == 1:
			leaves.add(i)
	
	edges = []
	for item in sequence:
		leaf = min(leaves)
		leaves.remove(leaf)
		edges.append((leaf, item))
		degree[item] -= 1
		if degree[item] == 1:
			leaves.add(item)
	
	edges.append((min(leaves), TREE_SIZE - 1))
	return edges

def set_labels(adj, u, e, cur_label, label):
	label[u] = cur_label
	
	for v in adj[u]:
		if v != e:
			set_labels(adj, v, u, cur_label, label)

def generate_labels(adj, search_space, guess):
	in_search_space = [False] * TREE_SIZE
	label = [-1] * TREE_SIZE
		
	for neighbour in adj[guess]:
		set_labels(adj, neighbour, guess, neighbour, label)
	
	for node in search_space:
		in_search_space[node] = True
	
	for node in range(TREE_SIZE):
		if not in_search_space[node]:
			label[node] = -1
	
	label[guess] = -1
	
	return label	

# --- end util functions


# generate random preufer sequence
sequence = [random.randrange(0, TREE_SIZE - 1) for _ in range(TREE_SIZE - 2)]

# decode preufer sequence
edges = decode_preufer(sequence)

adj = [0] * TREE_SIZE

for node in range(TREE_SIZE):
	adj[node] = []

# initialise adjacency list
for u, v in edges:
	adj[u].append(v)
	adj[v].append(u)

# output edges
for u, v in edges:
	print(u, v)

search_space = [node for node in range(TREE_SIZE)]

flag_found = False

for i in range(QUERY_LIMIT):
	guess = int(input("Guess where the flag is hidden: "))

	direction = -1
		
	labels = generate_labels(adj, search_space, guess)
	
	if guess not in search_space:
		# only one appropriate direction
		direction = labels[search_space[0]]
	else:
		# reduce search space based on guess
		if len(search_space) == 1:
			flag_found = True
			break
		
		freq = [0] * TREE_SIZE
		
		for label in labels:
			if label != -1:
				freq[label] += 1
		
		direction = max(range(len(freq)), key=freq.__getitem__)
		new_search_space = []
		
		for node in search_space:
			if labels[node] == direction:
				new_search_space.append(node)
		
		search_space = new_search_space
	
	print(f"The flag is in the direction of node {direction}")

if flag_found:
	print(flag)
else:
	print("No flag for you, try again :p")

exit()
