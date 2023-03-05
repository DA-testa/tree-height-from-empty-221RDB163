import sys
import threading

def CalculateHeight(parents_count, node):

    children = []
    for i in range(parents_count):
        children.append([])

    for i in range(parents_count):
        if node[i] != -1:
            children[node[i]].append(i)
            continue
        branche = i

    def CalculateDepth(branche):
        lowest_branch = 0
        
        for child in children[branche]:
            depth = CalculateDepth(child)
            lowest_branch = lowest_branch if lowest_branch > depth else depth
        lowest_branch += 1

        return lowest_branch

    return CalculateDepth(branche)

def main():
    input_type = input()

    if "I" in input_type:
        parents_count = int(input())

        input_branches = input().split(" ")
        branches = []

        for i in range( len(input_branches) ):
            branches.append(int(input_branches[i]))

        tree_height = CalculateHeight(parents_count, branches)
        print(tree_height)

    elif "F" in input_type:
        file_name = input()

        with open( f"test/{file_name}", "r" ) as file:
            parents_count = int(file.readline())

            input_branches = file.readline().split()
            branches = []
            for i in range( len(input_branches) ):
                branches.append(int(input_branches[i]))

            tree_height = CalculateHeight(parents_count, branches)

            print(tree_height)
    else:
        exit()

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
