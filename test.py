import random
pxx = []
nxx = []
if False:
    for i in ['adjectives', 'nouns']:
        with open('2syllable'+i+'.txt', 'r') as f:
            pxx.extend(x.lower()[:-1] for x in f if x.lower().startswith('p') and 
                not (i is 'nouns' and x[-2] is 's'))
    with open('3syllablenouns.txt', 'r') as f:
        nxx.extend(x.lower()[:-1] for x in f if x.lower().startswith('n'))
else:
    for i in ['adjectives', 'nouns']:
        with open(i+'.txt', 'r') as f:
            pxx.extend(x.lower()[:-1] for x in f if x.lower().startswith('p') and 
                not (i is 'nouns' and x[-2] is 's'))
    with open('nouns.txt', 'r') as f:
        nxx.extend(x.lower()[:-1] for x in f if x.lower().startswith('n'))
print(random.choice(pxx) + " " + random.choice(nxx))