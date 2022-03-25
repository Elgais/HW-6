def get_list() -> list:
    return list(range(0, 900_000))

class Solution:

    def binary_search(self, list, target):
        lower_b = 0
        upper_b = len(list)
        attemps = 0
        while lower_b <= upper_b:
            mid = (lower_b + upper_b) // 2
            attemps += 1

            if list[mid] == target:
                return f'Lost attemps :{attemps}' 

            elif list[mid] > target:
                upper_b = mid -1

            elif list[mid] < target:
                lower_b = mid +1
        return -1
        
p = Solution().binary_search(get_list(), 500_000)
print(p)