from collections import defaultdict
import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

dic = {}

def main():
  for num in range(1, 100_000):
    cum = num
    alteredNumber = num
    while alteredNumber > 0:
      cum += alteredNumber % 10
      alteredNumber //= 10
    if cum not in dic:
      dic[cum] = num
  n = int(input().strip())
  for _ in range(n):
    cum = int(input().strip())
    print(dic[cum] if cum in dic else 0)


if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()