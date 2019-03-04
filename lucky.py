#! /usr/bin/env python3
# google 検索結果をいくつか開く
# ブラウザのアドレスバーは基本http://google.com/search?q=~

import requests, sys, webbrowser, bs4
print('Googling...') # ダウンロード中にテキストを表示
res =  requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する

soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.r a') # rクラスは検索結果のリンクにだけ使われる。

# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems)) # 一番min のものを返す
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))





