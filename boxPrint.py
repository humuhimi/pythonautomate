
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbolは１文字以上でなければいけません')
    if width <= 2:
        raise Exception('widthは2より大きくなければならない')
    if height <= 2:
        raise Exception('heightは2より大きくなければならん')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym,w, h in (('*' ,4,4),('0',20,5),('x',1,3),('22',3,3)):
    try:
        box_print(sym,w,h)
    except Exception as err:
        print('例外が起こりました:' + str(err))

