class Solution:
    def twoSum(nums: list[int], target: int) -> list[int]:

        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

    def MYtwoSum(nums: list[int], target: int) -> list[int]:

        for num_index in range(len(nums)):

            for num2_index in range(num_index, len(nums)):

                if num2_index == num_index:
                    continue

                if nums[num_index] + nums[num2_index] == target:
                    return [num_index, num2_index]

if __name__ == "__main__":
    print(Solution.twoSum([2, 3, 4, 5, 6, 7, 11, 15], 9))