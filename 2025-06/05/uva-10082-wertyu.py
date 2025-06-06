import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
  s = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

  dic = dict(zip(s[1:], s))

  while True:
    try:
      print("".join(dic[i] if i in dic else i for i in input()))
    except EOFError:
      break


if __name__ == "__main__":
  if LOCAL:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()