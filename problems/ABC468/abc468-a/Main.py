def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n - 2):
        ans += a[i] < a[i + 1] > a[i + 2]
    print(ans)


if __name__ == "__main__":
    main()
