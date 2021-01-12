# flask-work
Python のマイクロフレームワークである [Flask](https://palletsprojects.com/p/flask/) の学習用リポジトリです。

# ブランチについて
基本的にそのとき確認した内容ごとにブランチを切ります。
現在は次のブランチがあります。

* [feat/csv](https://github.com/ksh-fthr/flask-work/tree/feat/csv)
  * CSV データを返却する API 実装を試すブランチ
  * Qiita の [[Angular] CSV ファイルを出力したときにやったこと](https://qiita.com/ksh-fthr/items/29db7c5c7268ee1802c5) でバックエンドの実装として扱った

# バージョン
次のバージョンで確認を行っています。

|        | バージョン |
| ------ | ---------- |
| Python | 3.7.x      |
| Flask  | 1.0.2      |

# ライブラリのインストール
`requirements.txt` で管理しています。
本リポジトリを利用する際は、事前に下記を実行してライブラリのインストールを行い、依存関係を解決しておいてください。

```bash
$ pip install -r requirements.txt
```

# 起動
次のコマンドでアプリケーションが起動します。

```bash
$ python3 app/run.py
```
