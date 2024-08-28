{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5cbe09d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Cost VEctor is:  [3, 2, 0, 0]\n",
      "Matrix A in Standard Form is: \n",
      "[2, 1, 1, 0]\n",
      "[-4, 5, 0, 1]\n"
     ]
    }
   ],
   "source": [
    "# 4A: WAP for Standard Form of LPP - 1\n",
    "\n",
    "#Given LPP\n",
    "#Max z = CX\n",
    "#AX <= b\n",
    "#X >= 0\n",
    "\n",
    "#Add slack variables and convert into the standard form\n",
    "c = [3, 2]\n",
    "a = [[2, 1],\n",
    "   [-4, 5]]\n",
    "bt = [20, 10]\n",
    "\n",
    "n = 2 #Number of Variables\n",
    "m = 2 #Number of COnstraints\n",
    "\n",
    "for i in range(n,n+m):\n",
    "    c.append(0)\n",
    "    \n",
    "print(\"The Cost VEctor is: \",c)\n",
    "\n",
    "for i in range(m):\n",
    "    for j in range(n,n+m):\n",
    "        if i == (j-n):\n",
    "            a[i].append(1)\n",
    "        else:\n",
    "            a[i].append(0)\n",
    "    \n",
    "print(\"Matrix A in Standard Form is: \")\n",
    "for i in range(m):\n",
    "    print(a[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "acfb42d6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Cost Vector in STD Form:  [3, 2]\n",
      "Matrix A in STD Form: \n",
      "[2, 1, 1, 0]\n",
      "[-4, 5, 0, 1]\n",
      "RHS Vector in STD Form:  [20, 10]\n"
     ]
    }
   ],
   "source": [
    "# 4B: Write a Python Function to convert a given LPP into standard Form\n",
    "\n",
    "#Given LPP Max Z = CX, AX <=B, X >= 0\n",
    "#Function Def for COnverting into Standard FOrm\n",
    "#Input: C, A, BT\n",
    "#Output: C, A, BT\n",
    "\n",
    "def LPP_STD_FORM(c, a, bt):\n",
    "    n = len(c) #Number of Variables\n",
    "    m = len(bt) #Number of COnstraint\n",
    "    \n",
    "    for i in range(n,n+m):\n",
    "        c.append(0)\n",
    "    \n",
    "    for i in range(m):\n",
    "        for j in range(n,n+m):\n",
    "            if i==(j-n):\n",
    "                a[i].append(1)\n",
    "            else:\n",
    "                a[i].append(0)\n",
    "    return(c, a, bt)\n",
    "\n",
    "c = [3, 2]\n",
    "a = [[2, 1],\n",
    "     [-4, 5]]\n",
    "bt = [20, 10]\n",
    "\n",
    "cstd, astd, bstd = LPP_STD_FORM(c, a, bt)\n",
    "print(\"The Cost Vector in STD Form: \",c)\n",
    "print(\"Matrix A in STD Form: \")\n",
    "m = len(bt)\n",
    "for i in range(m):\n",
    "    print(astd[i])\n",
    "\n",
    "print(\"RHS Vector in STD Form: \",bstd)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e6fc07f",
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
