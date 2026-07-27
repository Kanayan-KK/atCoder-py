def main() -> None:
    [m, d] = list(map(int, input().split()))
    s = input()
    sList = list(s)
    count = 0
    for i in range(len(s)):
        if "G" not in sList[max(0, i - d) : min(m, i + d + 1)]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
