import random
import copy
import time
import matplotlib.pyplot as plt


# debug
def printDict(tag, dict):
    print(f"Debug: {tag}")

    for key in dict.keys():

        value = dict[key]
        try:
            value = '\t'.join(dict[key])
        except:
            pass
        print(f"\t{key}: {value}")


# debug
def printDicts(tag, savePropositionalPositions, pickRandomPropositional):
    print(f"-----------------------------------{tag}---------------------------------------------")
    printDict("propositional ", propositional)
    printDict("savePropositionalPositions", savePropositionalPositions)
    printDict("pickRandomPropositional", pickRandomPropositional)
    print("--------------------------------------------------------------------------------")


def isSatisfied(clauses, m):
    correctPropositional = 0
    for value in clauses.values():
        for check in value:
            if check:
                correctPropositional += 1
                break
    return m - correctPropositional


# clausesHaveToChange is always equals to True except one time. This happens because we want to make
# refusalNumber-savePropositionalPositions-printSavePropositionalPositions only one time and don't change
# them because they are used to create clauses and sign of the numbers
def clausesMaker(m, k, propositional, clausesHaveToChange, n):
    global clauses, savePropositionalPositions, pickRandomPropositional, refusalNumber, printSavePropositionalPositions
    clauses = {}
    pickRandomPropositional = {}
    if not clausesHaveToChange:
        refusalNumber = {}
        savePropositionalPositions = {}
        printSavePropositionalPositions = {}
    for j in range(m):
        if not clausesHaveToChange:
            savePropositionalPositions[j] = []
            printSavePropositionalPositions[j] = []
        pickRandomPropositional[j] = []
        for number in range(k):
            if not clausesHaveToChange:
                # save propositional positions by choosing random propositions
                savePropositionalPositions[j].append(random.choice(list(propositional.keys())))
                printSavePropositionalPositions[j].append(random.choice(list(propositional.keys())))

            pickRandomPropositional[j].append(propositional[savePropositionalPositions[j][number]])
        # pick random True False. If for example we have [True, False, True] and C = [P2, P1, P4] then P
        # changes where refusalNumber is true C = [-P2, P1, -P4]
        if not clausesHaveToChange:
            refusalNumber[j] = [bool(random.getrandbits(1)) for _ in range(k)]
        clauses[j] = []

    # only used to print problem in "Hill_climbing.txt" (print it in console)
    if not clausesHaveToChange:
        print("n=", n, "m=", m, "k=", k)
        for j in range(m):
            for i in range(k):
                if refusalNumber[j][i]:
                    printSavePropositionalPositions[j][i] = "-" + printSavePropositionalPositions[j][i]
        printDict("Clauses", printSavePropositionalPositions)

    initializeClauses(k, m)


# make clauses
def initializeClauses(k, m):
    global clauses, refusalNumber, pickRandomPropositional
    # we use refusalNumber and pickRandomPropositional to give values to every clause
    for j in range(m):
        for i in range(k):
            if refusalNumber[j][i]:
                clauses[j].append(not pickRandomPropositional[j][i])
            else:
                clauses[j].append(pickRandomPropositional[j][i])


def hill_climbing(n, m, k, firstStep, clausesNotMade, clausesHaveToChange):
    """step 1"""
    global prevP
    global propositional
    if firstStep:
        propositional = {}
        # set random boolean values inside propositional
        for i in range(n):
            propositional[f"P{i}"] = bool(random.getrandbits(1))
    if clausesNotMade:
        clausesMaker(m, k, propositional, clausesHaveToChange, n)
    """step 2"""
    T = isSatisfied(clauses, m)
    if T == 0:
        return propositional
    """step 3"""
    newT = T
    x = 0
    count = False
    changedClauses = copy.deepcopy(clauses)
    """step 4"""
    for p in propositional.keys():
        if count:
            propositional[prevP] = not propositional[prevP]
        count = True
        prevP = p
        propositional[p] = not propositional[p]
        for position in savePropositionalPositions.keys():
            for ip, position2 in enumerate(savePropositionalPositions[position]):
                if position2 == p:
                    changedClauses[position][ip] = not changedClauses[position][ip]
        R = isSatisfied(changedClauses, m)
        changedClauses = copy.deepcopy(clauses)
        if R < newT:
            newT = R
            x = p

    propositional[prevP] = not propositional[prevP]
    """step 5"""
    if newT < T:
        propositional[x] = not propositional[x]
        if x != 0:
            for position in savePropositionalPositions.keys():
                for ip, position2 in enumerate(savePropositionalPositions[position]):
                    if position2 == x:
                        clauses[position][ip] = not clauses[position][ip]
        if newT == 0:
            printDict("propositional ", propositional)
            return propositional
        else:
            return hill_climbing(n, m, k, False, True, True)
    else:
        """step 6"""
        return hill_climbing(n, m, k, True, True, True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    y = []
    x = []
    for j in range(1, 9):
        start = time.time()
        for i in range(0, 5):
            hill_climbing(10, 10 * j, 4, True, True, False)
        end = time.time()
        x.append(j)
        y.append(end - start)
    plt.plot(x, y)

    # naming the x-axis
    plt.xlabel('m/n')

    # naming the y-axis
    plt.ylabel('Time')

    # giving a title to my graph
    plt.title('Hill_climbing')

    # function to show the plot
    plt.show()
