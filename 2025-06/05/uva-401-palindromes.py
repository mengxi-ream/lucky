import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

dic = {
  "A": "A",
  "E": "3",
  "H": "H",
  "I": "I",
  "J": "L",
  "L": "J",
  "M": "M",
  "O": "O",
  "S": "2",
  "T": "T",
  "U": "U",
  "V": "V",
  "W": "W",
  "X": "X",
  "Y": "Y",
  "Z": "5",
  "1": "1",
  "2": "S",
  "3": "E",
  "5": "Z",
  "8": "8"
}

def main():
  for line in sys.stdin:
    palindrome = True
    mirrored = True
    cleanLine = line.strip()
    for i in range(len(cleanLine) // 2 + 1):
      left = cleanLine[i]
      right = cleanLine[len(cleanLine) - 1 - i]
      if left != right:
        palindrome = False
      if left not in dic or dic[left] != right:
        mirrored = False
      if not palindrome and not mirrored:
        break
    if not palindrome and not mirrored:
      print("{} -- is not a palindrome.\n".format(cleanLine))
    elif palindrome and mirrored:
      print("{} -- is a mirrored palindrome.\n".format(cleanLine))
    elif palindrome:
      print("{} -- is a regular palindrome.\n".format(cleanLine))
    else:
      print("{} -- is a mirrored string.\n".format(cleanLine))



if __name__ == "__main__":
  if LOCAL:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()