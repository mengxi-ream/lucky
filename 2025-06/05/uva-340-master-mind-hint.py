import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
    idx = 0
    while True:
        n = int(input().strip())
        if n == 0:
            break
        secret = list(map(int, input().strip().split()))
        secret_count = [0] * 10
        for num in secret:
            secret_count[num] += 1
        
        idx += 1
        print("Game {}:".format(idx))
        
        for line in sys.stdin:
            numbers = list(map(int, line.strip().split()))
            if sum(numbers) == 0:
                break
                
            count = [0] * 10
            strong_count = sum(1 for i, num in enumerate(numbers) if num == secret[i])
            
            for num in numbers:
                count[num] += 1
                
            weak_count = sum(min(secret_count[i], count[i]) for i in range(1, 10))
            print("    ({},{})".format(strong_count, weak_count - strong_count))

if __name__ == "__main__":
    if LOCAL:
        if not os.path.exists("input.txt"):
            with open("input.txt", "w") as f:
                pass
        sys.stdin = open("input.txt", "r")
        sys.stdout = open("output.txt", "w")
    main()