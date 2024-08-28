{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7eeb3b16",
   "metadata": {},
   "outputs": [],
   "source": [
    "#conjugate gradient algorithim"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a62af20f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "g 0 =\n",
      " [[ 1]\n",
      " [-1]]\n",
      "initial direction\n",
      " [[-1]\n",
      " [ 1]]\n",
      "next direction [[-1]\n",
      " [ 1]]\n",
      "alpha 0 = [0.25]\n",
      "x 1 =\n",
      " [[-0.25]\n",
      " [ 0.25]]\n",
      "function value at x 1 = [[-0.25]]\n",
      "g 1 =\n",
      " [[-0.25]\n",
      " [-0.25]]\n",
      "next direction [[0.1875]\n",
      " [0.3125]]\n",
      "alpha 1 = [0.12903226]\n",
      "x 2 =\n",
      " [[-0.22580645]\n",
      " [ 0.29032258]]\n",
      "function value at x 2 = [[-0.25806452]]\n"
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
    "    d=d.reshape((n,1))\n",
    "    xn=x+a*d\n",
    "    return xn\n",
    "def directon(g,q,d0):\n",
    "    bk=np.dot(np.dot(np.transpose(g),q),d0)/np.dot(np.dot(np.transpose(d0),q),d0)\n",
    "    dnext=-g+bk*d0\n",
    "    return dnext\n",
    "\n",
    "def func(x,q,b):\n",
    "    f=.5*(np.dot(np.dot(np.transpose(x),q),x))-np.dot(np.transpose(x),b)\n",
    "    return f\n",
    "q=[[7,2],\n",
    "   [2,5]]\n",
    "x=[[0],\n",
    "   [0]]\n",
    "b=[[-1],\n",
    "   [1]]\n",
    "d=0\n",
    "n=len(q)\n",
    "for i in range(n):\n",
    "    g0=g(q,x,b)\n",
    "    print(\"g\",i,\"=\\n\",g0)\n",
    "    if np.all(g0==0):\n",
    "        print(\"optimality reached\")\n",
    "        break\n",
    "    if i==0:\n",
    "        d=-1*g0\n",
    "        print(\"initial direction\\n\",d)\n",
    "    else:\n",
    "        d=directon(g0,q,d)\n",
    "      \n",
    "    print(\"next direction\",d)\n",
    "    a=alpha(g0,d,q)\n",
    "    print(\"alpha\",i,\"=\",a)\n",
    "    x=xnext(x,a,d)\n",
    "    print(\"x\",i+1,\"=\\n\",x)\n",
    "    print(\"function value at x\", i+1, \"=\", func(x, q, b))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e90d1b8",
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
