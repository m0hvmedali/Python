# use split to split any by type of your pattern: we use a function called split()
# ──────────────────────────────────────────────────────────────────────────────
# IMPORTANT: to know  all about split: [pattern: str | Pattern[str], string: str, maxsplit: int = 0, flags: _FlagsType = 0]
# ──────────────────────────────────────────────────────────────────────────────
# SYNTAX: re.split(pattern, string)# the function will take two args first one is your pattern and the second one is the string you want to split
# ──────────────────────────────────────────────────────────────────────────────
# NOTE: the pattern in this function is optional we can use any pattern as we want 
# FUNCTION: re.split(pattern, string, maxsplit, flags).1
# ╭──────────────╮
# │    how       │
# │    to        │=>  use split : let's take an example:
# │    split     │
# ╰──────────────╯ 
# ──────────────────────────────────────────────────────────────────────────────
import re
string_one = "i love python"
search_one = re.split(r"\s", string_one, maxsplit=1)
print(search_one)

# the Output: ['i', 'love python']
# ────────────────────────────────────────────────────────────────────────────── 
# FUNCTION: re.sub(pattern, repl, string, count=0, flags=0).2
# ──────────────────────────────────────────────────────────────────────────────
print(re.sub(r"\s", "-", string_one))

# the Output: i-love-python
print(re.sub(r"\s", "-", string_one, count=1))
# ------------------------------------------------------------------------------
# the Output: i-love python
# TODO: use any pattern you want to split the string
print(re.split(r"\s", string_one, maxsplit=1))
print(re.sub(r"\s", "-", string_one, count=1))
# ══════════════════════════════════════════════════════════════════════════════
# ******************************************************************************
# the Output: i-love python
