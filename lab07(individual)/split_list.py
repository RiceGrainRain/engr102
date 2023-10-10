# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Manas Navale
# Section: 577
# Assignment: Lab Topic 7
# Date: 10/9/2023
#
def split_list(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    
    left_sum = 0
    left_list = []
    
    for num in nums:
        left_sum += num
        left_list.append(num)
        
        if left_sum == total_sum - left_sum:
            return left_list, nums[len(left_list):]
    
    return None, None

# Input string
input_str = input("Enter numbers: ")
input_list = [int(num) for num in input_str.split()]

left_portion, right_portion = split_list(input_list)

if left_portion is not None and right_portion is not None:
    print(f"Left: {left_portion}")
    print(f"Right: {right_portion}")
    left_sum = 0
    for num in left_portion:
        left_sum += num
    print("Both sum to", left_sum)
else:
    print(f"Cannot split evenly")
