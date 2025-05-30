import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
  pass

if __name__ == "__main__":
  if LOCAL:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()