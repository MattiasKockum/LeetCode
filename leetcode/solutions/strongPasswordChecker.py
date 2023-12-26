class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        print(password)
        cond_digit = False
        cond_upper = False
        cond_lower = False
        last_char = None
        combo = 1
        groups_len = []
        for index, char in enumerate(password):
            if not cond_digit and char in "0123456789":
                cond_digit = True
            if not cond_upper and char.isupper():
                cond_upper = True
            if not cond_lower and char.islower():
                cond_lower = True
            if char == last_char:
                combo += 1
                if combo == 3:
                    groups_len.append(combo)
                elif combo > 3:
                    groups_len[-1] += 1
            else:
                combo = 1
            last_char = char
        steps = 0
        groups_len = sorted(groups_len)
        length = len(password)
        # adding essentials if not (replace = one step, adding = one step)
        groups_len.sort(key=lambda x: x % 3)
        print(f"{groups_len=}")
        print(f"{cond_digit=}, {cond_upper=}, {cond_lower=}, {combo=}")
        print(f"Init : {steps=}, {length=}, {groups_len=}")
        if not cond_digit:
            steps += 1
            len_cond = 4
            if length < 6:
                length += 1
                len_cond = 5
            if groups_len != []:
                if groups_len[-1] <= len_cond:
                    groups_len.pop()
                else:
                    groups_len[-1] -= 3
        groups_len.sort(key=lambda x: x % 3)
        print(f"After cond_digit : {steps=}, {length=}, {groups_len=}")
        if not cond_upper:
            steps += 1
            len_cond = 4
            if length < 6:
                length += 1
                len_cond = 5
            if groups_len != []:
                if groups_len[-1] <= len_cond:
                    groups_len.pop()
                else:
                    groups_len[-1] -= 3
        groups_len.sort(key=lambda x: x % 3)
        print(f"After cond_upper : {steps=}, {length=}, {groups_len=}")
        if not cond_lower:
            steps += 1
            len_cond = 4
            if length < 6:
                length += 1
                len_cond = 5
            if groups_len != []:
                if groups_len[-1] <= len_cond:
                    groups_len.pop()
                else:
                    groups_len[-1] -= 3
        groups_len.sort(key=lambda x: x % 3)
        print(f"After cond_lower : {steps=}, {length=}, {groups_len=}")
        # removing if too long, adding if too short
        if length > 20:
            diff = length - 20
            steps += diff
            length = 20
            # prioritize multiples of 3
            groups_len.sort(key=lambda x: x % 3)
            print(groups_len)
            for _ in range(diff):  
                if groups_len != []:
                    groups_len[0] -= 1
                    groups_len.sort(key=lambda x: x % 3)
                    while groups_len[0] == 5 and groups_len != len(groups_len) * [5]:
                        groups_len = groups_len[1:] + groups_len[:1]
                    if groups_len[-1] == 2:
                        groups_len.pop()
                print(groups_len)
        elif length < 6:
            diff = 6 - length
            steps += diff
            length = 6
            for _ in range(diff):
                if groups_len != []:
                    if groups_len[-1] <= 4:
                        groups_len.pop()
                    else:
                        groups_len[-1] -= 2
        print(f"After cond_len: {steps=}, {length=}, {groups_len=}")
        # removing three consecutives (removing = one step)
        steps += sum([i // 3 for i in groups_len])
        print(f"After breaking : {steps=}, {length=}, {groups_len=}")
        return steps

