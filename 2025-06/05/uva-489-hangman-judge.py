import sys
import os

LOCAL = os.getenv("LOCAL", "false").lower() == "true"

def main():
  data = sys.stdin.read().splitlines()
  idx = 0

  while idx < len(data):
    case = int(data[idx])
    if case == -1:
      break
    print("Round {}".format(case))
    ans = set(data[idx + 1].strip())
    guess = data[idx + 2].strip()
    right_set = set()
    wrong_count = set()
    
    for c in guess:
      if c in ans:
        right_set.add(c)
        if right_set == ans:
          print("You win.")
          break
      else:
        wrong_count.add(c)
        if len(wrong_count) >= 7:
          print("You lose.")
          break
    else:
      if right_set != ans:
        print("You chickened out.")

    idx += 3
    


if __name__ == "__main__":
  if LOCAL:
    if not os.path.exists("input.txt"):
      with open("input.txt", "w") as f:
        pass
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
  main()