import random
import copy
import time
import matplotlib.pyplot as plt


def isSolution(child):
    global clauseArray
    table = copy.deepcopy(clauseArray)
    sizeOfChild = len(child)
    countTrue = 0
    # get all values in clauseArray and find if they are negative numbers.
    # table saves propositional values regarding randomNumber values
    for i, element in enumerate(clauseArray):
        for id, j in enumerate(element):
            # j<0 negative number
            if j < 0:
                if j >= -sizeOfChild:
                    # change number sign
                    table[i][id] = (not child[-j - 1])
            else:
                if j <= sizeOfChild:
                    table[i][id] = (child[j - 1])
        for id, j in enumerate(element):
            if table[i][id] == True:
                countTrue += 1
                break
    # if countTrue equals clauseArray length then every C is satisfied
    if countTrue == len(clauseArray):
        return True

    return False


# print values we used to find the solution
def makeInputFile(n, m, k):
    global clauseArray
    print("n=", n, "m=", m, "k=", k)
    clauseArray = []
    for _ in range(m):
        tempClauses = []
        for _ in range(k):
            randomNumber = random.randint(-n, n)
            while randomNumber == 0:
                randomNumber = random.randint(-n, n)
            tempClauses.append(randomNumber)
        print(tempClauses)
        clauseArray.append(tempClauses)


def isValid(child):
    global clauseArray
    table = copy.deepcopy(clauseArray)
    sizeOfChild = len(child)
    # get all values in clauseArray and find if they are negative numbers.
    # table saves propositional values regarding randomNumber values
    for i, element in enumerate(clauseArray):
        for id, j in enumerate(element):
            if j < 0:
                if j >= -sizeOfChild:
                    table[i][id] = (not child[-j - 1])
            else:
                if j <= sizeOfChild:
                    table[i][id] = (child[j - 1])
        if not any(table[i]):
            return False

    return True


def DFS(n, m, k):
    """step 1"""
    stack = []
    makeInputFile(n, m, k)
    stack.append([])
    """step 2"""
    while stack:
        """a"""
        vertex = stack.pop()
        """b"""
        while len(vertex) == n:
            if stack:
                vertex = stack.pop()
            else:
                return "Error"
        leftChild = copy.deepcopy(vertex)
        leftChild.append(False)
        rightChild = copy.deepcopy(vertex)
        rightChild.append(True)
        """step i"""
        if isValid(leftChild):
            """1"""
            if isSolution(leftChild):
                return "Solved" + str(leftChild)
            else:
                """step ii"""
                stack.append(leftChild)
        """step i"""
        if isValid(rightChild):
            """1"""
            if isSolution(rightChild):
                return "Solved" + str(leftChild)
            else:
                """step ii"""
                stack.append(rightChild)

    """step 3"""
    return "Impossible"


if __name__ == '__main__':
    x = []
    y = []
    for j in range(1, 9):
        start = time.time()
        print(DFS(10, 10 * j, 4))  # n, m, k
        end = time.time()
        x.append(j)
        y.append(end - start)
    plt.plot(x, y)

    # naming the x-axis
    plt.xlabel('m/n')

    # naming the y-axis
    plt.ylabel('Time')

    # giving a title to my graph
    plt.title('Depth-First-Search')

    # function to show the plot
    plt.show()
