def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False

    set_nums = set()

    for num in nums:
        if type(num) == str or num < 0:
            return False
        elif num in set_nums:
            return num
        else:
            set_nums.add(num)

    return False
