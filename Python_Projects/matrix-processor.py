def options():  # Main Options
	print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")


def tran_ops():  # Sub options for transpose
	print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")


def make_matrix(row):  # function used to create the matrix
	m, a = row, []
	for i in range(m):  # in range of no of rows
		b = []
		for j in input().split(" "):  # split the values using space
			try:
				j = int(j)  # check if it is integer
				b.append(j)
			except ValueError:
				try:
					j = float(j)  # check if it is float
					b.append(j)
				except ValueError:  # if both are false the print error
					print("Enter a valid input")
		a.append(b)
	return a  # return the matrix


def add_matrix(mat1, mat2):  # function used to add two matrices
	res = []
	for i in range(len(mat1)):  # iterate through the row of matrix
		lst = []
		for j in range(len(mat1[0])):  # iterate through the column of matrix
			lst.append(mat1[i][j] + mat2[i][j])  # adding values from both matrix
		res.append(lst)
	return res  # return value


def print_matrix(mat, trans=False):
	# function for printing matrix, trans is optional and false is default value
	print("The result is: ")
	for i in range(len(mat)):  # iterate through the row of matrix
		for j in range(len(mat[0])):  # iterate through the column of matrix
			if trans:  # if transpose, print the transpose
				print(mat[j][i], end=' ')
			else:  # print the matrix itself
				print(mat[i][j], end=' ')
		print()
	print()
	return 0


def det(mat):  # function for calculating the determinant using recursion
	deter = 0
	if len(mat) == 1:  # base case
		deter = mat[0][0]
	else:  # iterative case
		for i in range(len(mat)):  # in the range of len(mat)
			value = det([mat[row][1:] for row in range(len(mat)) if row != i])  # det is found using 1st(0th)rows
			deter += mat[i][0] * ((-1) ** i) * value  # determinant found by multiplying with cofactor and minor
	return deter


def determinant():  # function to find the determinant
	m, n = map(int, input("Enter size of matrix: ").split())  # input the size of matrix
	print("Enter matrix: ")
	mat = make_matrix(m)  # making matrix
	deter = det(mat)  # calling det function (most of work is done here)
	print("The result is: ")
	print(deter, "\n")


def scalar_multiply():  # function for scalar multiplication
	m, n = map(int, input("Enter size of matrix: ").split())  # input the size of matrix
	print("Enter matrix: ")
	mat = make_matrix(m)  # making scalar
	num = float(input("Enter constant: "))  # take the constant
	res = []
	for i in range(m):
		lst = []
		for j in range(n):
			lst.append(mat[i][j] * num)  # multiply matrix values with constant
		res.append(lst)
	print_matrix(res)  # print the scalar matrix


def multiple(mat1, mat2):  # function for matrix multiplication
	res = []
	for k in range(len(mat1)):  # iterate through rows of mat1
		lst = []
		for i in range(len(mat2[0])):  # iterate through columns of mat2
			value = 0
			for j in range(len(mat2)):  # iterate through rows of mat2
				value += mat1[k][j] * mat2[j][i]
			lst.append(value)
		res.append(lst)
	return res


def transpose():
	tran_ops()  # print Transpose options
	op = int(input("Your choice: "))
	row, col = map(int, input("Enter matrix size: ").split())  # take size of matrix
	a = make_matrix(row)
	if op == 1:  # Transpose by main diagonal
		print_matrix(a, True)  # True is give as it is to make a transpose
	elif op == 2:  # Transpose by side diagonal
		a = a[::-1]
		for i in range(len(a)):
			a[i] = a[i][::-1]  # the reversing of matrix upside down
		print_matrix(a, True)  # when print is called matrix is printed in side transpose
	elif op == 3:  # # Transpose by vertical line
		for i in range(len(a)):
			a[i] = a[i][::-1]  # reverse of matrix side ways
		print_matrix(a)  # direct print with no transpose required
	elif op == 4:  # # Transpose by horizontal line
		a = a[::-1]
		print_matrix(a)  # the reversing of matrix upside down
	else:
		exit()


def matrix(choice):
	""" function for building, adding and multiplying two matrices """
	m, n = map(int, input("Enter size of first matrix: ").split())  # size of first matrix
	print("Enter first matrix: ")
	a = make_matrix(m)  # make first matrix
	p, q = map(int, input("Enter size of second matrix: ").split())  # size of second matrix
	print("Enter second matrix: ")
	b = make_matrix(p)  # make first second
	if choice == 1:
		if m != p and n != q:  # check the matrix
			print("ERROR")
		else:  # if valid
			c = add_matrix(a, b)  # calling add matrix function
			print_matrix(c)
	elif choice == 3:
		if n != p:  # check for validity
			print("ERROR")
		else:  # if valid
			c = multiple(a, b)  # calling matrix multiplication function
			print_matrix(c)
	elif choice == 4:
		tran_ops()  # calling transpose option
	else:
		exit()
	return 0


def inverse():
	res = []
	m, n = map(int, input("Enter size of matrix: ").split())  # input the size of matrix
	print("Enter matrix: ")
	mat = make_matrix(m)
	cofactors = [[  # creating the adjacent of mat
			((-1) ** (x + y)) * det([
				[mat[col][row] for col in range(m) if col != x]
				for row in range(n) if row != y
			]) for x in range(m)
		] for y in range(n)
	]
	if det(mat) != 0:  # checking if determinant is zero
		inv = (1 / det(mat))
		for i in cofactors:  # multiplying each element of cofactors with inv
			res.append([inv * j for j in i])
		print_matrix(res)  # printing the result
	else:
		print("This matrix doesn't have an inverse.")


def main():
	""" Main function where everything is made possible """
	flag, choice = 1, 0
	while flag:
		op = 1
		options()  # print Main options
		while op:  # try asking for choice till a valid choice is given
			try:
				choice = int(input("Your choice: "))  # take the choice
				op = 0
			except ValueError:
				print("Enter the valid option")  # if choice is invalid

		if choice == 1:
			matrix(choice)  # call matrix function
		elif choice == 2:
			scalar_multiply()  # call scalar multiplication
		elif choice == 3:
			matrix(choice)  # call matrix function
		elif choice == 4:
			transpose()  # call transpose function
		elif choice == 5:
			determinant()  # call determinant function
		elif choice == 6:
			inverse()  # call inverse function
		else:
			flag = 0
	exit()  # else exit program


main()  # calling main function
