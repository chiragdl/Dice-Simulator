{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d89bb3f5",
   "metadata": {},
   "source": [
    "### Dice Simulator!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2017390c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----------\n",
      "|        |\n",
      "|    6   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    3   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    6   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    3   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    6   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    5   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    1   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!y\n",
      "----------\n",
      "|        |\n",
      "|    2   |\n",
      "|        |\n",
      "----------\n",
      " y to cointinue to roll the dice..!n\n"
     ]
    }
   ],
   "source": [
    "import random \n",
    "x = \"y\"\n",
    "while x == \"y\":\n",
    "    num = random.randint(1,6)\n",
    "    if num == 1:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    1   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "    elif num == 2:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    2   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "    elif num == 3:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    3   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "    elif num == 4:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    4   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "    elif num == 5:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    5   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "    elif num == 6:\n",
    "        print(\"----------\")\n",
    "        print(\"|        |\")\n",
    "        print(\"|    6   |\")\n",
    "        print(\"|        |\")\n",
    "        print(\"----------\")\n",
    "        \n",
    "    x = input(\" y to cointinue to roll the dice..!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c8d565e8",
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
