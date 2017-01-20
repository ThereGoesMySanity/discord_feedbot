import random
pxx = []
nxx = []
if True:
    for i in ['adjectives', 'nouns', 'adverbs']:
        with open('2syllable'+i+'.txt', 'r') as f:
            pxx.extend(x for x in f if x.startswith('p'))
    with open('3syllablenouns.txt', 'r') as f:
        nxx.extend(x for x in f if x.startswith('n'))
else:
    for i in ['adjectives', 'nouns', 'adverbs']:
        with open(i+'.txt', 'r') as f:
            pxx.extend(x for x in f if x.startswith('p'))
            if i is 'nouns':
                nxx.extend(x for x in f if x.startswith('n'))
print(random.choice(pxx) + " " + random.choice(nxx))