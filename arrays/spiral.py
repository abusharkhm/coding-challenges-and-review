def layerTopRight(matrix):
  
  # remove and store the first row from matrix
  top = matrix.pop(0)
  
  # store the right column of the matrix
  right = []
  
  # remove the last column from the matrix
  for i in range(0, len(matrix)):
    e = matrix[i].pop()
    right.append(e)
    
  # return the top row and last column elements as a list
  return top + right

def layerBottomLeft(matrix):
  
  # remove and store the last row from matrix in reverse order
  bottom = matrix.pop()[::-1]
  
  # store the left column of the matrix
  left = []
  
  # remove the first column from the matrix
  for i in range(0, len(matrix)):
    e = matrix[i].pop(0)
    left.append(e)
    
  # return the top row and last column elements as a list
  return bottom + left[::-1]

# our main spiral function that will
# return a final spiral ordered list
def spiral(matrix):
  
  # where we store our final spiraled list
  spir = []
  
  while len(matrix) > 0:
    
    # if only 1 more element left in matrix
    if len(matrix) == 1:
      spir += matrix[0]
      break
      
    # return the spiraled list of the top row and
    # right column for this matrix
    tr = layerTopRight(matrix)
    spir += tr
    
    # return the spiraled list of the bottom row and
    # left column for this matrix
    bl = layerBottomLeft(matrix)
    spir += bl
    
  return spir
  
  
# setup a matrix  
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

N = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

# return it in spiral order
print(spiral(M))
print(N.pop(0))