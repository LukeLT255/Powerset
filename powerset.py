
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)

    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

if __name__ == '__main__':
    total = input("Please enter the total amount of numbers you would like to enter." + '\n')
    numList = [input('Enter number ' + str(i + 1) + ': ') for i in range(int(total))]
    print(powerset(numList))



