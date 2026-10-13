# Time O(N) | Space O(N)
# TODO: refactor to be less complex
def twoSum(nums: list[int], target: int) -> list[int]:
        result = []
        num_index_map = {}
        for i in range(0, len(nums)):
            if i == 0:
                num_index_map[nums[i]] = i 
            if num_index_map.get(target - nums[i], -1) > -1 and num_index_map[target - nums[i]] != i:
                  result.append(num_index_map[target - nums[i]])
                  result.append(i)
                  break
            else:
                num_index_map[nums[i]] = i 
        print(num_index_map)
        return result
            

                  
             
                       
                        

if __name__ == '__main__':
        nums = [3,4,5,6]
        target = 7
        print(twoSum(nums, target))