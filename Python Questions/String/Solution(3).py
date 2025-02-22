str="P@#yn2^at6&i5ve"
char=0
digit=0
symbol=0
for i in str:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        char=char+1
    else:
        symbol=symbol+1

print(f"In the given String -: \nChars= {char} \nDigits= {digit} \nSymbol= {symbol}")