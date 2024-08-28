{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9acbd35b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[9, -1, 3]\n"
     ]
    }
   ],
   "source": [
    "# Addition of 2 vectors\n",
    "\n",
    "vector1 = [5, -2, 3]     #taking 2 vecctors\n",
    "\n",
    "vector2 = [4, 1, 0]\n",
    "\n",
    "vector_sum = []     # Initializing  a new vector to store sum\n",
    "\n",
    "for i in range(len(vector1)):\n",
    "    vector_sum.append(vector1[i] + vector2[i])\n",
    "\n",
    "print(vector_sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "97447392",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the size of vector:4\n",
      "enter the values for the vector:\n",
      "enter the element:-1\n",
      "enter the element:0\n",
      "enter the element:3\n",
      "enter the element:5\n",
      "enter the scalar value:4\n",
      "The resultant vector: [-4.0, 0.0, 12.0, 20.0]\n"
     ]
    }
   ],
   "source": [
    "#Python code for vector scalar multiplication\n",
    "\n",
    "def vector_scaler_multiplication():\n",
    "    size = int(input(\"enter the size of vector:\"))\n",
    "    vector=[]\n",
    "    print(\"enter the values for the vector:\")\n",
    "    \n",
    "    for i in range(size):\n",
    "        value=float(input(\"enter the element:\"))\n",
    "        vector.append(value)\n",
    "    \n",
    "    scalar=float(input(\"enter the scalar value:\"))\n",
    "    result=[scalar * v for v in vector]\n",
    "    print(\"The resultant vector:\",result)\n",
    "vector_scaler_multiplication()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c83e6e21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of elements in vector: 3\n",
      "Enter the elements of vector a: \n",
      "2\n",
      "3\n",
      "4\n",
      "Enter the number of elements in vector: 3\n",
      "Enter the elements of vector b: \n",
      "4\n",
      "-5\n",
      "6\n",
      "Inner product =  17.0\n"
     ]
    }
   ],
   "source": [
    "#python code for inner product of 2 vectors\n",
    "\n",
    "a = []\n",
    "n = int(input(\"Enter the number of elements in vector: \"))\n",
    "print(\"Enter the elements of vector a: \")\n",
    "\n",
    "for i in range (0,n):\n",
    "    l = float(input())\n",
    "    a.append(l)\n",
    "    \n",
    "b = []\n",
    "n = int(input(\"Enter the number of elements in vector: \"))\n",
    "print(\"Enter the elements of vector b: \")\n",
    "\n",
    "for i in range (0,n):\n",
    "    m = float(input())\n",
    "    b.append(m)\n",
    "    \n",
    "c = 0\n",
    "for i in range (0,n):\n",
    "    c = c+(a[i]*b[i])\n",
    "    \n",
    "print(\"Inner product = \", c)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b75ae2e",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'col2' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-bd227bec3336>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     35\u001b[0m \u001b[1;31m# Multiply matrices\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 36\u001b[1;33m \u001b[0mresult_matrix\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmatrix_multiply\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmatrix_A\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mmatrix_B\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     38\u001b[0m \u001b[1;31m# Print the result\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m<ipython-input-1-bd227bec3336>\u001b[0m in \u001b[0;36mmatrix_multiply\u001b[1;34m(A, B)\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m     \u001b[1;31m# Initializing the result matrix with zeros\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m     \u001b[0mresult\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mcol2\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mrange\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mrow1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m     \u001b[1;31m# loops for matrix multiplication\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'col2' is not defined"
     ]
    }
   ],
   "source": [
    "# Python code for Matrix Multiplication\n",
    "\n",
    "def matrix_multiply(A, B):\n",
    "    rows_A, cols_A = len(A), len(A[0])\n",
    "    rows_B, cols_B = len(B), len(B[0])\n",
    "\n",
    "    # Checking if matrices can be multiplied\n",
    "    if cols_A != rows_B:\n",
    "        raise ValueError(\"Number of columns in A matrix must be equal to the number of rows in B matrix.\")\n",
    "\n",
    "    # Initializing the result matrix with zeros\n",
    "    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]\n",
    "    \n",
    "    # loops for matrix multiplication\n",
    "    for i in range(rows_A):\n",
    "        for j in range(cols_B):\n",
    "            for k in range(cols_A):\n",
    "                result[i][j] += A[i][k] * B[k][j]\n",
    "\n",
    "    return result\n",
    "\n",
    "# Example matrices\n",
    "matrix_A = [\n",
    "    [1, 2, 0, -1],\n",
    "    [4, 3, 1, 7],\n",
    "]\n",
    "\n",
    "matrix_B = [\n",
    "    [7, 0],\n",
    "    [5, 11],\n",
    "    [1, 7],\n",
    "    [2, 5]\n",
    "]\n",
    "\n",
    "# Multiply matrices\n",
    "result_matrix = matrix_multiply(matrix_A, matrix_B)\n",
    "\n",
    "# Print the result\n",
    "for row in result_matrix:\n",
    "    print(row)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "90f418f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[4, 2, 3]\n",
      "[9, 8, 9]\n",
      "[-1, 8, 8]\n"
     ]
    }
   ],
   "source": [
    "# Python code for addition of 2 matrices\n",
    "\n",
    "\n",
    "A = [[3, 0, 2],\n",
    "    [1 , 5, 2],\n",
    "    [-3 , 4, 7]]\n",
    " \n",
    "B = [[1, 2, 1],\n",
    "    [8, 3, 7],\n",
    "    [2, 4, 1]]\n",
    " \n",
    " \n",
    "result = [[0,0,0],\n",
    "        [0,0,0],\n",
    "        [0,0,0]]\n",
    " \n",
    "# iterate through rows\n",
    "for i in range(len(A)):   \n",
    "# iterate through columns\n",
    "    for j in range(len(A[0])):\n",
    "        result[i][j] = A[i][j] + B[i][j]\n",
    " \n",
    "for r in result:\n",
    "    print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4b49e9e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Rank of the matrix:\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "## Rank of a Matrix\n",
    "\n",
    "def find_matrix_rank(matrix):\n",
    "    num_rows, num_cols = len(matrix), len(matrix[0]) if matrix else 0\n",
    "    rank = 0\n",
    "    row, col = 0, 0\n",
    "\n",
    "    while row < num_rows and col < num_cols:\n",
    "        # Find the pivot in the current column\n",
    "        pivot_row = row\n",
    "        while pivot_row < num_rows and matrix[pivot_row][col] == 0:\n",
    "            pivot_row += 1\n",
    "\n",
    "        if pivot_row < num_rows:\n",
    "            # Swap rows to move the pivot to the current row\n",
    "            matrix[row], matrix[pivot_row] = matrix[pivot_row], matrix[row]\n",
    "\n",
    "            # Scale the current row so that the pivot becomes 1\n",
    "            pivot_element = matrix[row][col]\n",
    "            matrix[row] = [elem / pivot_element for elem in matrix[row]]\n",
    "\n",
    "            # Eliminate other entries below the leading 1\n",
    "            for i in range(row + 1, num_rows):\n",
    "                factor = matrix[i][col]\n",
    "                matrix[i] = [elem - factor * matrix[row][j] for j, elem in enumerate(matrix[i])]\n",
    "\n",
    "            # Increment rank and move to the next column and row\n",
    "            rank += 1\n",
    "            row += 1\n",
    "            col += 1\n",
    "        else:\n",
    "            # If no pivot is found in the current column, move to the next column\n",
    "            col += 1\n",
    "\n",
    "    return rank\n",
    "\n",
    "# Example usage:\n",
    "matrix = [[0,0,0],\n",
    "          [0,0,0],\n",
    "          [0,0,0]]\n",
    "\n",
    "rank = find_matrix_rank(matrix)\n",
    "print(\"Rank of the matrix:\")\n",
    "print(rank)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d647080b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "Diagonal entries made to 1 iteration Number k= 0\n",
      "[1.0, -0.8888888888888888, 0.3333333333333333, 0.0]\n",
      "[1, 2, 3, -4]\n",
      "[6, 7, 0, -1]\n",
      "\n",
      "\n",
      "All Non-Diagonal entries made to 1 iteration Number k= 0\n",
      "[1.0, -0.8888888888888888, 0.3333333333333333, 0.0]\n",
      "[0.0, 2.888888888888889, 2.6666666666666665, -4.0]\n",
      "[0.0, 12.333333333333332, -2.0, -1.0]\n",
      "\n",
      "\n",
      "Diagonal entries made to 1 iteration Number k= 1\n",
      "[1.0, -0.8888888888888888, 0.3333333333333333, 0.0]\n",
      "[0.0, 1.0, 0.923076923076923, -1.3846153846153846]\n",
      "[0.0, 12.333333333333332, -2.0, -1.0]\n",
      "\n",
      "\n",
      "All Non-Diagonal entries made to 1 iteration Number k= 1\n",
      "[1.0, 0.0, 1.1538461538461537, -1.2307692307692306]\n",
      "[0.0, 1.0, 0.923076923076923, -1.3846153846153846]\n",
      "[0.0, 0.0, -13.384615384615383, 16.076923076923073]\n",
      "\n",
      "\n",
      "Diagonal entries made to 1 iteration Number k= 2\n",
      "[1.0, 0.0, 1.1538461538461537, -1.2307692307692306]\n",
      "[0.0, 1.0, 0.923076923076923, -1.3846153846153846]\n",
      "[-0.0, -0.0, 1.0, -1.2011494252873562]\n",
      "\n",
      "\n",
      "All Non-Diagonal entries made to 1 iteration Number k= 2\n",
      "[1.0, 0.0, 0.0, 0.15517241379310343]\n",
      "[0.0, 1.0, 0.0, -0.27586206896551735]\n",
      "[-0.0, -0.0, 1.0, -1.2011494252873562]\n"
     ]
    }
   ],
   "source": [
    "##### Simultaneous linear equation\n",
    "\n",
    "n=3\n",
    "ab=[[9, -8, 3, 0],\n",
    "    [1, 2, 3 , -4],\n",
    "    [6, 7, 0, -1]]\n",
    "for k in range(n):\n",
    "    pivot =ab[k][k]\n",
    "    for j in range(n+1):\n",
    "        if pivot!=0:\n",
    "            ab[k][j]=ab[k][j]/pivot\n",
    "    print(\"\\n\\nDiagonal entries made to 1 iteration Number k=\",k)\n",
    "    for i in range(n):\n",
    "        print(ab[i])\n",
    "        if i!=k:\n",
    "            pivot =ab[i][k]\n",
    "            for j in range(n+1):\n",
    "                ab[i][j]=ab[i][j] - pivot*ab[k][j]\n",
    "    print(\"\\n\\nAll Non-Diagonal entries made to 1 iteration Number k=\",k)\n",
    "    for i in range(n):\n",
    "        print(ab[i])\n",
    "                    \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "daeee7ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "Diagonal entries made to 1 iteration Number k= 0\n",
      "[1.0, 1.0, 0.5, 0.0]\n",
      "[3, 4, 0, 1]\n",
      "\n",
      "\n",
      "All Non-Diagonal entries made to 1 iteration Number k= 0\n",
      "[1.0, 1.0, 0.5, 0.0]\n",
      "[0.0, 1.0, -1.5, 1.0]\n",
      "\n",
      "\n",
      "Diagonal entries made to 1 iteration Number k= 1\n",
      "[1.0, 1.0, 0.5, 0.0]\n",
      "[0.0, 1.0, -1.5, 1.0]\n",
      "\n",
      "\n",
      "All Non-Diagonal entries made to 1 iteration Number k= 1\n",
      "[1.0, 0.0, 2.0, -1.0]\n",
      "[0.0, 1.0, -1.5, 1.0]\n",
      "\n",
      "\n",
      "The inverse matrix is\n",
      "[2.0, -1.0]\n",
      "[-1.5, 1.0]\n"
     ]
    }
   ],
   "source": [
    "#Inverse of a Matrix\n",
    "\n",
    "n=2\n",
    "ai =[[2, 2, 1, 0],\n",
    "     [3, 4, 0, 1]]\n",
    "for k in range(n):\n",
    "    pivot =ai[k][k]\n",
    "    for j in range(2*n):\n",
    "        ai[k][j]=ai[k][j]/pivot\n",
    "    print(\"\\n\\nDiagonal entries made to 1 iteration Number k=\",k)\n",
    "    for i in range(n):\n",
    "        print(ai[i])\n",
    "    for i in range(n):    \n",
    "        if i!=k:\n",
    "            pivot =ai[i][k]\n",
    "            for j in range(2*n):\n",
    "                ai[i][j]=ai[i][j] - pivot*ai[k][j]\n",
    "    print(\"\\n\\nAll Non-Diagonal entries made to 1 iteration Number k=\",k)\n",
    "    for i in range(n):\n",
    "        print(ai[i])\n",
    "        \n",
    "print(\"\\n\\nThe inverse matrix is\")\n",
    "for i in range(n):\n",
    "    print(ai[i][n:2*n])            \n",
    "             "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bef3209b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
