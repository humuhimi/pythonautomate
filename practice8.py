#! /usr/bin/env python3
# practice8 クリップボードのテキストを保存・復元する
# Usage:
# save <keyword> : クリップボードをキーワードに紐ずけて保存する。
# <keyword> : キーワードに紐ずけられたテキストをクリップボードにコピー
# list : 全キーワードをクリップボードに表示

import shelve, pyperclip, sys

prac8_shelf = shelve.open('practice8')

# うクリップボードの内容を保存

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    prac8_shelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# キーワード一覧　or 読み込み
    if sys.argv[1].lower == 'list':
        pyperclip.copy(str(list(prac8_shelf.keys())))
    elif sys.argv[1] in prac8_shelf:
        pyperclip.copy(prac8_shelf[sys.argv[1]])
else:
    print(
    '''
        # Usage:
        # save <keyword> : クリップボードをキーワードに紐ずけて保存する。
        # <keyword> : キーワードに紐ずけられたテキストをクリップボードにコピー
        # list : 全キーワードをクリップボードに表示
        
    '''
        )

prac8_shelf.close()




