from itertools import permutations


def main() -> None:
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    count = 0
    for a in permutations([i + 1 for i in range(N)]):
        count += P < list(a) < Q

    print(count)

if __name__ == "__main__":
    main()
