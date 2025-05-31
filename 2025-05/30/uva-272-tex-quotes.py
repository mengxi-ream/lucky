import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
    left = True
    for line in sys.stdin:
        line = line.rstrip('\n')  # 去掉行末的换行符
        parsedLine = ""
        for c in line:
          if c == '"':
            parsedLine += '``' if left else '\'\''
            left = not left
          else:
            parsedLine += c
        print(parsedLine)
              

if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()