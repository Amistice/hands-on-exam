def steps_to_the_right(nums: list, k: int) -> list:
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    return nums[-k:] + nums[:-k]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(steps_to_the_right(nums, 3))# Q8: Rotate array right by k positions
