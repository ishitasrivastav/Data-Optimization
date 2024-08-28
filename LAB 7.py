{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6d201fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#conjugate direction algorithim "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1a4ff27a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "g 0 =\n",
      " [[ 1]\n",
      " [-1]]\n",
      "alpha 0 = -0.16666666666666666\n",
      "x 1 =\n",
      " [[-0.16666667]\n",
      " [ 0.        ]]\n",
      "function value at x 1 = -0.08333333333333333\n",
      "g 1 =\n",
      " [[ 0. ]\n",
      " [-1.5]]\n",
      "alpha 1 = -1.5\n",
      "x 2 =\n",
      " [[-1.66666667]\n",
      " [ 3.        ]]\n",
      "function value at x 2 = -2.3333333333333335\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "def g(q,x0,b):\n",
    "    G=np.dot(q,x0)-b\n",
    "    return G\n",
    "def alpha(g,d,q):\n",
    "    gt=np.transpose(g)\n",
    "    dt=np.transpose(d)\n",
    "    a=(np.dot(gt,d)/np.dot(np.dot(dt,q),d))*-1\n",
    "    return a[0]\n",
    "def xnext(x,a,d):\n",
    "    d=d.reshape((2,1))\n",
    "    xn=x+a*d\n",
    "    return xn\n",
    "def func(x,q,b):\n",
    "    f=.5*(np.dot(np.dot(np.transpose(x),q),x))-np.dot(np.transpose(x),b)\n",
    "    return f[0][0]\n",
    "q=[[6,3],\n",
    "   [3,2]]\n",
    "x=[[0],\n",
    "   [0]]\n",
    "b=[[-1],\n",
    "   [1]]\n",
    "d=[[1,0],\n",
    "   [1,-2]]\n",
    "d=np.array(d)\n",
    "n=len(q)   \n",
    "for i in range(n):\n",
    "    g0=g(q,x,b)\n",
    "    print(\"g\",i,\"=\\n\",g0)\n",
    "    a=alpha(g0,d[i],q)\n",
    "    print(\"alpha\",i,\"=\",a)\n",
    "    x=xnext(x,a,d[i])\n",
    "    print(\"x\",i+1,\"=\\n\",x)\n",
    "    print(\"function value at x\",i+1,\"=\",func(x,q,b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1cb71736",
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
