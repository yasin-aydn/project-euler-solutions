from itertools import permutations

def find_permutation(num):
    liste = (list(permutations(range(10),10)))
    result = "".join(map(str,liste[num-1]))
    print(result)

find_permutation(1000000)
