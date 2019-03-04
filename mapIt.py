
#! /usr/bin/env python3
# mapIt.pyではコマンドラインやクリップボードに指定した住所の地図を開く
# https://www.google.com/maps/place/~/で開く

import webbrowser ,sys,pyperclip

if len(sys.argv) > 1:
    # コマンドから住所を取得する
    address = ' '.join(sys.argv[1:])
else:
    #クリップボードから住所を取得する
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

