# treasure tree
Category: misc

Creator: pavement

Flag: `sctf{tr33_gr4ph_th30ry_sp3c14l1st}`

## Description
There is a treasure hidden in one of the nodes of the tree. You can guess... but there's a limit to how many guesses you have. Can you find the treasure?

## Solution
Let us consider the simpler case where the tree is a line. Intuitively, it makes sense to make the first guess in the middle of this line, because no matter the direction returned by the process, we can discard half of the nodes from consideration. By applying this process repeatedly (guessing in the middle of the search space), we can determine where the treasure is in log_2(16) = 4 queries. This algorithm is known as binary search (https://en.wikipedia.org/wiki/Binary_search_algorithm).

Now, we return to the case where the tree may not be a line. In this case, there seems to be no well-defined "middle" of the tree. However, by drawing out the tree (there are only 16 nodes, you can also use a graph visualiser tool) and intuitively deciding where the "middle" is (and perhaps restarting the process a few times), it is possible to similarly find the treasure in 4 queries.

A more rigorous solution: the analog of the "middle" in the line case is the "centroid" of the tree (https://usaco.guide/plat/centroid?lang=cpp). This can be interpreted as the "center of mass" (NOT the "center") of the tree. The centroid(s) of a tree with N nodes refers to any node such that if it were removed, all remaining connected components would have a size not exceeding N/2. At least one centroid exists for all trees. By repeatedly guessing the "centroid" at each step, it is always possible to find the treasure in 4 queries.

Bonus: this strategy may not always yield the minimum number of guesses (in a deterministic setup). There exists a greedy algorithm that yields the "shallowest" possible "decision tree", effectively minimising the number of guesses (https://codeforces.com/blog/entry/125018).