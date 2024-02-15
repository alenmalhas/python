'''
------------------------------------------------------------------------------------------------------------------------------------------------------------------
    Matrix Challenge
Have the function MatrixChallenge(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's of some arbitrary size, and determine if a path of 1's exists from the top-left of the matrix to the bottom-right of the matrix while moving only in the directions: up, down, left, and right. If a path exists your program should return the string true, otherwise your program should return the number of locations in the matrix where if a single 0 is replaced with a 1, a path of 1's will be created successfully. If a path does not exist and you cannot create a path by changing a single location in the matrix from a 0 to a 1, then your program should return the string not possible. For example: if strArr is ["11100", "10011", "10101", "10011"] then this looks like the following matrix:

1 1 1 0 0
1 0 0 1 1
1 0 1 0 1
1 0 0 1 1

For the input above, a path of 1's from the top-left to the bottom-right does not exist. But, we can change a 0 to a 1 in 2 places in the matrix, namely at locations: [0,3] or [1,2]. So for this input your program should return 2. The top-left and bottom-right of the input matrix will always be 1's.
Examples
Input: ["10000", "11011", "10101", "11001"]
Output: 1
Input: ["1000001", "1001111", "1010101"]
Output: not possible
------------------------------------------------------------------------------------------------------------------------------------------------------------------
ref: https://leetcode.com/discuss/interview-question/1001809/amazon-oa-matrix-challenge

First, represent the array as undirected, unweighted graph. Then here is the algorithm

Perform DFS or BFS from top-left with target node being bottom-right
If bottom-right can be reached, return True
Otherwise, keep track of all nodes visited by search above. Save the set of all "0" nodes that are adjacent to any visited node, do this by iterating over all visited nodes
Next repeat DFS/BFS but this from bottom-right and top-left as target. Keep track of all visited nodes here too. Similar to above, save all "0" nodes that are adjacent to any visited node.
Count the intersection of the sets from Step 3 and 4. If it is zero, return "not possible", otherwise return the size of the set.
------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def matrix_challenge(arr):
  for i, row in enumerate(arr):
    arr[i] = [c for c in row]

  rows = len(arr)
  cols = len(arr[0])
  possible, visited_start = search((0, 0), (rows-1, cols-1), arr)
  if possible:
    return True

  _, visited_end = search((rows-1, cols-1), (0, 0), arr)

  neighbors_start = get_all_neighbors(visited_start, arr)
  neighbors_end = get_all_neighbors(visited_end, arr)

  num_intersect = len(neighbors_start.intersection(neighbors_end))
  if num_intersect == 0:
    return "not possible"
  else:
    return num_intersect

def get_all_neighbors(vertices, arr):
  neighbors = set()
  for v in vertices:
    neighbors = neighbors.union(get_neighbors(v, arr, "0"))
  return neighbors

def search(start, target, arr):
  stack = [start]
  visited = {start}

  while stack:
    v = stack.pop()
    if v == target:
      return True, None

    for n in get_neighbors(v, arr, "1"):
      if n in visited:
        continue
      stack.append(n)
      visited.add(n)

  return False, visited

def get_neighbors(v, arr, val):
  rows = len(arr)
  cols = len(arr[0])
  i, j = v

  neighbors = []
  neighbors.extend(valid(i-1, j, rows, cols, arr, val))
  neighbors.extend(valid(i+1, j, rows, cols, arr, val))
  neighbors.extend(valid(i, j-1, rows, cols, arr, val))
  neighbors.extend(valid(i, j+1, rows, cols, arr, val))
  return neighbors

def valid(i, j, rows, cols, arr, val):
  result = []
  if i >= 0 and j >= 0 and i < rows and j < cols and arr[i][j] == val:
    result = [(i, j)]
  return result