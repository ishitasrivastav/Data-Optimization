{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7df6362c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Given a nXn matrix and two vectors di and dj Find out if di and dj are Q-Conjugate Vectors\n",
    "\n",
    "# Def:  Two vectors di and dj are Q-Conjugate  if diT*Q*dj = 0   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "db4f4962",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "value of diQdj :  6.32\n",
      "Q-Conjugate:  False\n"
     ]
    }
   ],
   "source": [
    "def scalarMul (a,b):\n",
    "    result = 0\n",
    "    for i in range (len(a)):\n",
    "        result = result + a[i]*b[i]\n",
    "    return(result)\n",
    "\n",
    "def conjugateMul (di, Q, dj):    \n",
    "    vec = []\n",
    "    for j in range (len(Q)):\n",
    "        vj = 0\n",
    "        for i in range (len(Q)):\n",
    "            vj = vj + di[i] * Q[i][j]\n",
    "        vec.append(vj)\n",
    "    \n",
    "    diQdj = scalarMul(vec,dj)\n",
    "    return (diQdj)\n",
    "\n",
    "Q = [[3, 0, 1],\n",
    "    [0, 4, 2],\n",
    "    [1, 2, 3]]\n",
    "d1= [3, 0, 1]\n",
    "d2 = [0.5, -0.444, 0.368]\n",
    "\n",
    "value = round(conjugateMul(d1, Q, d2), 4)\n",
    "print(\"value of diQdj : \", value)\n",
    "qconj = True if value == 0 else False \n",
    "print(\"Q-Conjugate: \", qconj)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a160b3fa",
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
