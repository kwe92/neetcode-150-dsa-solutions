# O(NlogN) Log-Linear Time and (N) Linear Space
def removeDuplicates(nums: list[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort() # O(NlogN) log-linear time
        return len(nums)

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]

    k = removeDuplicates(nums)

    print('number of unique elements:', k)
    print('nums:', nums)
