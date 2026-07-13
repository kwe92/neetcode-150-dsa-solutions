# maybe working worst case time is O(N^2) and the best time possible is O(N)
def removeElement(nums: list[int], val: int) -> int:
    index_state = []
    for i in range(0, len(nums)):
        if nums[i] == val:
            index_state.append(i)
    
    for i, prev_i in enumerate(index_state):
        idx_to_remove = prev_i - i
        nums.pop(idx_to_remove)

# TODO: figure out a O(N) algo
def removeElement(nums: list[int], val: int) -> int:
    pass

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]

    val = 2

    removeElement(nums, val)
    
    print(f'external nums: {nums}')