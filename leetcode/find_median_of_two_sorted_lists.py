def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    print(nums1, nums2)
    sorted = []
    total_len = len(nums1) + len(nums2)
    goal_pos = (total_len - 1) / 2

    sorted = []

    median = -200

    while len(sorted) < goal_pos + 1 and nums1 != [] and nums2 != []:
        if nums1[0] < nums2[0]:
            sorted.append(nums1.pop(0))
        else:
            sorted.append(nums2.pop(0))

    if len(sorted) == goal_pos + 1:
        median = sorted[-1]
    elif nums1 == []:
        if goal_pos % 1 == 0:
            median = nums2[int(goal_pos) - len(sorted)]
        else:
            median = (
                    (sorted + nums2)[int(goal_pos - 0.5)]
                    + (sorted + nums2)[int(goal_pos + 0.5)]
                    ) / 2
    elif nums2 == []:
        if goal_pos % 1 == 0:
            median = nums1[int(goal_pos) - len(sorted)]
        else:
            median = (
                    (sorted + nums1)[int(goal_pos - 0.5)]
                    + (sorted + nums1)[int(goal_pos + 0.5)]
                    ) / 2
    elif len(sorted) > goal_pos:
        median = (sorted[-1] + sorted[-2]) / 2

    print(goal_pos, total_len, sorted, nums1, nums2, median)

    return median
