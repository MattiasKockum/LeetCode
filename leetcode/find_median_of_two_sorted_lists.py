def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    total_len = len(nums1) + len(nums2)
    goal_pos = (total_len - 1) / 2

    if nums1 == []:
        if goal_pos % 1 == 0:
            return nums2[int(goal_pos)]
        else:
            return (nums2[int(goal_pos)] + nums2[int(goal_pos) + 1]) / 2

    if nums2 == []:
        if goal_pos % 1 == 0:
            return nums1[int(goal_pos)]
        else:
            return (nums1[int(goal_pos)] + nums1[int(goal_pos) + 1]) / 2

    if nums1[-1] <= nums2[0]:
        if goal_pos % 1 == 0:
            return (nums1 + nums2)[int(goal_pos)]
        else:
            return sum((nums1 + nums2)[int(goal_pos) : int(goal_pos + 1.5)]) / 2

    if nums2[-1] <= nums1[0]:
        if goal_pos % 1 == 0:
            return (nums2 + nums1)[int(goal_pos)]
        else:
            return sum((nums2 + nums1)[int(goal_pos) : int(goal_pos + 1.5)]) / 2

    
    n_2 = None
    n_1 = None
    pos = -1

    while pos < goal_pos and nums1 != [] and nums2 != []:
        n_2 = n_1
        if nums1[0] < nums2[0]:
            n_1 = nums1.pop(0)
        else:
            n_1 = nums2.pop(0)
        pos += 1

    if pos == goal_pos:
        return n_1
    elif pos > goal_pos:
        if goal_pos % 1 == 0:
            return n_1
        else:
            return (n_1 + n_2) / 2
    elif pos == goal_pos - 0.5:
        if nums1 == []:
            return (n_1 + nums2[0]) / 2
        else:
            return (n_1 + nums1[0]) / 2
    else:
        if nums1 == []:
            if goal_pos % 1 == 0:
                return nums2[int(goal_pos) - pos - 1]
            else:
                return sum(nums2[int(goal_pos) - pos - 1 : int(goal_pos) - pos + 1]) / 2
        else:
            if goal_pos % 1 == 0:
                return nums1[int(goal_pos) - pos - 1]
            else:
                return sum(nums1[int(goal_pos) - pos - 1 : int(goal_pos) - pos + 1]) / 2

    print(f"{n_2=}, {n_1=}, {pos=}, {goal_pos=}, {nums1=}, {nums2=}")

    return -200
