#!/bin/bash
# Runtime: 8 ms, faster than 25.01% of Bash online submissions for Valid Phone Numbers.
# Memory Usage: 3.1 MB, less than 75.00% of Bash online submissions for Valid Phone Numbers.
grep -E '^(\([0-9]{3}\)\s|[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt