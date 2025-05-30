import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
  print("Hello world", LOCAL)

if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()