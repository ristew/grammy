import grammy
import sys

gen_len = 500
if len(sys.argv) > 1:
    grammy.read_file(sys.argv[1])
else:
    grammy.read_file('austen-emma.txt')
if '-l' in sys.argv:
    gen_len = int(sys.argv[sys.argv.index('-l') + 1])


if '-c' in sys.argv:
    print grammy.slow_gen()
else:
    print grammy.gen(gen_len)
