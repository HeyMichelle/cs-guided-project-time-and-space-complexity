"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:
- No negative numbers and no zero
- Return none if no answer
#  edge cases listed above during lecture not originally included in notes
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""

def two_sum(nums, target):
    # dictionary solution
    num_dict = {}
    # O(n)
    for i in range(len(nums)): 
        num_dict[nums[i]] = i
    
    for i in range(len(nums)): # range generates all of the indices 
        current_num = nums[i] # O(1)
        # check if the compliment is in the dict
        compliment = target - current_num # O(1)

        if compliment in num_dict and i != num_dict[compliment]: # searching a hash table is O(1)
            return [i, num_dict[compliment]]

            # compliment exists! return its index

    # Runtime: everything inside the loop is O(1), we have two loops that are not nested, therefor is O(n) + O(n) which is just O(n) not O(2n) and not O(n^2) because constants get deleted
        # O(n) time complexity
    # Space complexity: creating a dictionary, we will always have an 'n' # of items. Better to take up space than reduce speed.
        # O(n) space


    # brute force solution
    # for i in range(len(nums)): # do we always want to use range(len()) in for loops?
    #     for j in range(i+1, len(nums)):
    #         num1 = nums[i]
    #         num2 = nums[j]
    #         if num1 + num2 == target:
    #             return [i, j]
    # 
    # return None
    # 
    # # the above code is a bad brute force solution
    # # after creating, go through each line on the inside of the loop and see the runtime
    # # it has O(n) linear runtime for each loop with O(1) constant time for items inside the loop (variables). Altogether is O(n^2) quadratic due to O(n) * O(n) for the nested loops
    # # nested loops does not always mean O(n^2), if were 10 instead of len(nums) 'n' then would not be quadratic



# Understand
    # input: nums and target
    # output: indices of the two numbers used to add up to target
    # given array in integers 'nums' and integer 'target'
    # return [i] of the two numbers that add up to target
# Plan
    # We now have BIG O as a tool in determining best steps
    # Make it work first via "brute force" solution, then modify to improve time and space     complexity 
        # possibly use two loops or a nested loop, generate possible pairs
        # try a number, add it to each of the other numbers, does it equal target? If not, go to the next number, and add to each number again
    # brute force option:
        # two loops to generate all pairs
        # loop for each num_1 in nums:
            # loop num_2 in nums starting at index +1
            # num_1 + num_2
    # find a better algorithm better than O(n^2)
        # linear is out of picture because does not allow nested loops, can only run once
        # is there a data structure I could build to build this out in an easier faster way?
    # Optimization for time and space complexity:
        # asking myself, is there a 5? And where is it? (for example provided above problem) 2 + 5 == 7
        # iterate through until you find 5
        # what if you had a dictionary, what would it store? The 5, the id(location)
            # the key's are numbers and the values are the index
            # dictionary is O(1)
    # Build a dictionary
        # loop
            # each num : index, insert into dictionary
        # find the two numbers 
            # for each num, is there a matching num or (compliment)
            # if there is, where is it? (meaining what is the index)
