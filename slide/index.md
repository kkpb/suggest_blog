title: 機械学習を使ってブログの分類をした話
author:
profile: 

# 自己紹介
* 小久保翔平
* 琉球大学
* 修士2年
* 並列処理とか GPGPU やってます

# 取り組んだテーマ
* 機械学習
  * 人工知能における研究課題の一つで、人間が自然に行っている学習能力と同様の機能をコンピュータで実現しようとする技術・手法のことである

# 理由
* Deep Learning って最近良く聞くけど、なにができるかわからない
* waifu2x すごい

# 開発環境(1/2)
* OS
  * OS X version 10.10.3
* CPU
  * 2.3 GHz Intel Core i7
* Language
  * Python 2.7.9

# 開発環境(2/2)
* Library
  * Scrapy
  * mecab
  * scikit-learn
  * Flask

# Scrapy
* Crawling & Scraping Framework
* install
  * pip install scrapy
* scrapy_project/spiders/spider.py
  * start_urls : クローリングを始める url を指定
  * rules : 任意の url('entry'を含むなど) に対する操作(再帰的に辿る、コールバック)を指定
* 他のスクレイピングツールとして Beautiful Soup 

# mecab
* 形態素解析エンジン
* 特徴語の抽出に利用
  * 辞書が古いのでそのまま使うと精度に影響が…
* ChaSen, Yahoo 日本語形態素解析

# Flask
* Micro Web Framework
* 必要最低限な機能のみ提供
* Python でちょっとした web アプリを作るならこれ

# scikit-learn
* 機械学習ライブラリ
* 特徴ベクトルへの変換
* ブログの分類
* 豊富な分類器
  * ほぼ同じ API で利用可能

# 機械学習を始める上で
* 必要十分なデータ量
  * < 10k samples
* アルゴリズムの選択
  * 特徴ベクトル
    * BoW, tf*idf
  * 分類器
    * Naive Bayes, SVM, etc...
  * scikit-learn に [Cheat-Sheet](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) あります

# 分類器のチューニング
* 交差検定
  * ある学習用データと検証用データでたまたま良い(悪い)結果になるのを防ぐ
  * 学習データを学習用と検証用に分割し、計算
* グリッドサーチ
  * パラメータの範囲を指定して総当りで検証
  * 並列実行化
    * データ量\*パラメータの種類\*パラメータ範囲

# 成果物の概要
* はてなブログの新着記事を取得
* 文書の特徴を示す単語を抽出
* 単語を特徴ベクトルに変換
* 特徴ベクトルを分類器にかけて WEB で表示

# 成果物の特徴
* 分類された記事に対するフィードバック
  * フィードバックを元に再学習
  * 使えば使うほど精度が上がっていく(はず)

# 改善点
* 特徴語の抽出
  * 辞書をそのまま使ったので上手く特徴語を抽出できていない
  * 次元量の増大
* 他の分類器の検証

# 感想
* データ集めがとにかく大変
* ライブラリが揃っているので機械学習を始めるのに Python は良い
* 今回はとりあえず動くものを優先したので、各アルゴリズムの実装を読みたい