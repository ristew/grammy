import grammy
import sys

gen_len = 500
if len(sys.argv) > 1:
    grammy.read_file(sys.argv[1])
    if len(sys.argv) > 2:
        gen_len = int(sys.argv[2])
else:
    grammy.read_file('austen-emma.txt')
print grammy.gen(gen_len)
