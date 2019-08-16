# SWEA

- [Difficulty 1](d1)
- [Difficulty 2](d2)
- [Difficulty 3](d3)
- [Difficulty 4](d4)

## used snippet

```python
 "swea": {
    "prefix": "swea",
    "body": [
      "'''",
      "problem_description",
      "'''",
      "",
      "import sys",
      "sys.stdin = open(\"SWEA/inputs/${TM_FILENAME/[\\D]//gi}_in.txt\", \"r\")",
      "",
      "t = int(input())",
      "for i in range(t):",
      "    n = int(input())",
      "    nums = list(map(int, input().split()))",
      "",
      "    print(\"#{} {}\".format(i+1, result))"
    ],
    "description": "swea ps starting snippet"
  }
}
```
