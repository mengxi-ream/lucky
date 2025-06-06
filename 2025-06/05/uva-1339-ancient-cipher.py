from collections import Counter
import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def get_sorted_freq(s): 
  return sorted(Counter(s).values())

def main():
  while True:
    try:
      print("YES" if get_sorted_freq(input().strip()) == get_sorted_freq(input().strip()) else "NO")
    except EOFError:
      break

if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()