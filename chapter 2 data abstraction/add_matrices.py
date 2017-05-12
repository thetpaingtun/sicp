#function to add 2 two-d matrices
#mat = [[x,y],[x,y]]
def add_matrices(mat1,mat2):
	return [[mat1[i][j]+mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]





mat1 = [[1, 3] , [2, 0]]
mat2 = [[-3, 0], [1, 2]]

print(add_matrices(mat1,mat2))