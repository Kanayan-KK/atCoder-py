s = input()
n = len(s)
answer = 0

for is_even in range(2):
    for center_right in range(n):
        left = center_right - is_even
        right = center_right
        mismatch_count = 0

        while 0 <= left and right < n:
            a = s[left]
            b = s[right]
            if a != b:
                mismatch_count += 1

            if mismatch_count == 2:
                break

            answer += 1
            left -= 1
            right += 1

print(answer)
