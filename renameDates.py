#! /usr/bin/env python3
# renameDates.py 米国式日ずけMM-DD-YYYYをお欧州式DD-MM-YYYYに書き換える。

import shutil, os, re


date_pattern = re.compile(r"""^(.*?) # 日ずけの前の全テキスト
    ((1|2)?\d)- # 月を表す1,2桁の数字
    ((0|1|2|3)?\d)- # 日を表す1,2桁の数字
    ((19|20)\d\d) # 年を表す4桁の数字
    (.*?)$ # 日ずけの後の全テキスト
    """,re.VERBOSE)


for amer_filename in os.listdir('.'): # カレントディレクトリの全ファイルをループする
    mo = date_pattern.search(amer_filename)

# 日ずけのないファイルをスキップする
    if mo == None:
        continue

# ファイル名を分割する mo.groupは()の数で番号がつくことに注意する。

before_part = mo.group(1)
month_part = mo.group(2)
day_part = mo.group(4)
year_part = mo.group(6)
after_part = mo.group(8)

# 欧式の日ずけのファイル名を作る。

euro_filename = before_part + day_part + '-' + month_part + '-' + \ year_part + after_part

# ファイル名を変更する

print('Renameing "{}" to "{}" ....'.format(amer_filename,euro_filename))
#shutil.move(amer_filename,euro_filename)



