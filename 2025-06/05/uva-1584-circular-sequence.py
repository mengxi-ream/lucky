import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
  # read n
  # read line by line
  # ans as the first read
  # rotate and compare
  # update ans if necessary
  # print ans
  n = int(input().strip())
  for _ in range(n):
    ans = input().strip()
    current_str = ans
    for _ in range(1, len(ans)):
      current_str = current_str[1:] + current_str[0]
      if current_str < ans:
        ans = current_str
    print(ans)


if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()