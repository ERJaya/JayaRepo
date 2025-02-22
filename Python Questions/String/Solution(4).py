a="Elephant and Horse"
a=a.lower()
vowel=0
cons=0
for i in a:
    if i in "aeiou":
        vowel=vowel+1
    elif i==" ":
        continue
    else:
        cons=cons+1
print(f"Vowel = {vowel} & Consonent = {cons}")