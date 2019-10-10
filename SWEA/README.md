# SWEA

- [Difficulty 1](d1)
- [Difficulty 2](d2)
- [Difficulty 3](d3)
- [Difficulty 4](d4)
- [Difficulty 5](d5)
- [Difficulty 6](d6)

## used snippet

```json
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
			"ans = \"\"",
			"",
			"for tc in range(1, int(input())+1):",
			"    n = int(input())",
      "    nums = list(map(int, input().split()))",
      "res = \"\""",
			"",
			"    ans += \"#{} {}\\n\".format(tc, res)",
			"",
			"print(ans)"
		],
		"description": "swea ps starting snippet"
	}
```

