import random

cache = {}
text = ""

def read_file(filename):
    global text
    f = open(filename, 'r')
    text = f.read()
    f.close()
    parse_text()

def parse_text():
    for i, c in enumerate(text):
        if i > 2:
            key = (text[i - 3], text[i - 2], text[i - 1])
            key2 = (text[i - 2], text[i - 1])
            if key in cache:
                cache[key].append(c)
            else:
                cache[key] = [c]
            if key2 in cache:
                cache[key2].append(c)
            else:
                cache[key2] = [c]

def gen(size=100):
    seed = random.randint(0, len(text) - 3)
    c1, c2, c3 = text[seed], text[seed + 1], text[seed + 2]
    gen_ = []
    for i in xrange(size):
        gen_.append(c1)
        try:
            c1, c2, c3 = c2, c3, random.choice(cache[(c1, c2, c3)])
        except:
            try:
                c1, c2, c3 = c2, c3, random.choice(cache[(c2, c3)])
            except:
                c1, c2, c3 = c2, c3, random.choice(text)

    gen_.append(c2)
    return ''.join(gen_)
