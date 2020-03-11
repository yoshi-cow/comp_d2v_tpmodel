#----------------------------------------------------------------------------------------------
# 青空文庫からダウンロードしたzip書籍ファイルを解凍して、pandasのDFに入れ、pickleで吐き出す。
#----------------------------------------------------------------------------------------------

import glob
import zipfile
import pathlib
import pandas as pd
import re
import pickle

# zipファイルを解凍
aut_zip = ['kajii', 'nagai', 'nakajima', 'natume']
for aut in aut_zip:
    # 著者毎にzipfile取得して解凍
    zip_path = str(pathlib.Path('./get_novel/novels').resolve()) + '/' + aut + '/*' # 絶対パス取得
    res_path =str(pathlib.Path('./get_novel/novels').resolve()) + '/' + aut + '_list'
    for zipf in glob.glob(zip_path):
        # zip解凍して別ディレクトリへ保存
        with zipfile.ZipFile(zipf) as zipf:
            zipf.extractall(res_path)

# textファイルの文字コードがShift_JISのため、utf-8に変換
# ターミナルで、コマンドで一括変換
# $ find . -name "*.txt" -exec iconv -f SHIFT-JIS -t UTF-8 {} -o {} \;

# テキストファイルからタイトルと本文を抽出してpandasDFに保存
cols = ['title', 'content', 'author'] # author入力値 : 0-梶井、1-永井、2-中島、3-夏目
author_df = pd.DataFrame(index=[], columns=cols)
aut_zip = ['kajii_list', 'nagai_list', 'nakajima_list', 'natume_list']
for aut in aut_zip:
    # 著者ごとに作品ファイル取り出し
    work_path = str(pathlib.Path('./get_novel/novels').resolve()) + '/' + aut + '/*.txt'
    for work_fi in glob.glob(work_path):
        with open(work_fi, 'r') as f:
            # タイトルと本文を抽出
            all_d = f.read()
            find_s = re.search(r'-------------------------------------------------------', all_d)
            if find_s:
                all_l = all_d.split('-------------------------------------------------------')
                title = all_l[0].split('\n')[0] # タイトル抽出
                # 本文抽出
                text = all_l[2]
                find_t = re.search(r'底本：.*',text)
                if find_t:
                    content = text[0:find_t.start()]
                else:
                    content = text # 文字コード置換エラーで、'底本：'の部分が無い場合の対応
            else:
                # '-------------'でわけられていないデータの場合
                all_d = all_d.strip() # 念の為、前後の空白とる
                tit_p = re.search('\n', all_d)
                title = all_d[:tit_p.start()] # タイトル抽出
                # 本文抽出
                if aut == 'kajii_list':
                    auth = '梶井基次郎'
                elif aut == 'nagai_list':
                    auth = '永井荷風'
                elif aut == 'nakajima_list':
                    auth = '中島敦'
                else:
                    auth = '夏目漱石'
                auth_p = re.search(auth, all_d)
                teihen_p = re.search('底本：', all_d)
                if teihen_p:
                    content = all_d[auth_p.end()+1:teihen_p.start()] # 本文抽出
                else:
                    # '底本：'の部分が無い場合の対応
                    content = all_d[auth_p.end()+1:]
            # author の設定
            if aut == 'kajii_list':
                author = 0
            elif aut == 'nagai_list':
                author = 1
            elif aut == 'nakajima_list':
                author = 2
            else:
                author = 3
            # dfに挿入
            author_df = author_df.append(pd.Series([title, content, author], index=author_df.columns), ignore_index=True)

# pickleでauthor_dfを保存
pic_f = str(pathlib.Path('./get_novel/novels').resolve()) + '/novel_list.pickle'
with open(pic_f, 'wb') as f:
    pickle.dump(author_df, f)
