{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ac4ea866",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Legrange’s First Order Necessary Condition – using Eigen Vector\n",
    "\n",
    "# MAXIMIZE : (x**T)*Q*x /  (x**T)*P*x  ; where Q = Q**T >= 0 and P = P**T >0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "abd409f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "P_inverse\n",
      " [[0.5 0. ]\n",
      " [0.  1. ]]\n",
      "P_inverse*q= \n",
      " [[2. 0.]\n",
      " [0. 1.]]\n",
      "Eigenvalues:\n",
      " [2. 1.]\n",
      "\n",
      "Eigenvectors:\n",
      " [[1. 0.]\n",
      " [0. 1.]]\n",
      "funtion at 1st eigen vector 2.0\n",
      "funtion at 2nd eigen vector 1.0\n",
      "function maximum at x0 = [1. 0.] and minimum at x1 = [0. 1.]\n"
     ]
    }
   ],
   "source": [
    "##b ISHITA   2367406\n",
    "\n",
    "import numpy as np\n",
    "p=[[2,0],\n",
    "   [0,1]]\n",
    "q=[[4,0],\n",
    "   [0,1]]\n",
    "p=np.array(p)\n",
    "q=np.array(q)\n",
    "pinverse=np.linalg.inv(p)\n",
    "print(\"P_inverse\\n\",pinverse)\n",
    "pq=np.dot(pinverse,q)\n",
    "print(\"P_inverse*q= \\n\",pq)\n",
    "eigenvalues, eigenvectors = np.linalg.eig(pq)\n",
    "print(\"Eigenvalues:\\n\",eigenvalues)\n",
    "print(\"\\nEigenvectors:\\n\",eigenvectors)\n",
    "def func(x):\n",
    "    xqx=np.dot(np.dot(x,q),np.transpose(x))\n",
    "    xpx=np.dot(np.dot(x,p),np.transpose(x))\n",
    "    return xqx/xpx\n",
    "f1=func(eigenvectors[0])\n",
    "f2=func(eigenvectors[1])\n",
    "print(\"funtion at 1st eigen vector\",f1)\n",
    "print(\"funtion at 2nd eigen vector\",f2)\n",
    "if f1>f2:\n",
    "    print(f\"function maximum at x0 = {eigenvectors[0]} and minimum at x1 = {eigenvectors[1]}\")\n",
    "else:\n",
    "    print(f\"function maximum at x1 = {eigenvectors[1]} and minimum at x0 = {eigenvectors[0]}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "697b1d47",
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
