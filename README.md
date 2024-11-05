# flask-work

Python のマイクロフレームワークである [Flask](https://palletsprojects.com/p/flask/) の学習用リポジトリです。

# ブランチについて

基本的にそのとき確認した内容ごとにブランチを切ります。
現在は次のブランチがあります。

* [feat/csv](https://github.com/ksh-fthr/flask-work/tree/feat/csv)
  * CSV データを返却する API 実装を試すブランチ
  * Qiita の [[Angular] CSV ファイルを出力したときにやったこと](https://qiita.com/ksh-fthr/items/29db7c5c7268ee1802c5) でバックエンドの実装として扱った
* [feat/zip](https://github.com/ksh-fthr/flask-work/tree/feat/zip)
  * base64 文字列化した ZIP ファイルを返却する API 実装を試すブランチ
  * Qiita の [[Flask] CSV ファイルを ZIP に固める](https://qiita.com/ksh-fthr/items/df875613d7e36f94a679) で扱った
  * また同じく Qiita の [[Angular] base64 文字列をバイナリに戻してダウンロードする](https://qiita.com/ksh-fthr/items/b3e3afb7f8e51759a1ed) でバックエンドの実装として扱った

# Python や フレームワーク等のバージョン

[pyenv](https://github.com/pyenv/pyenv) でバージョン管理を行っています。
次のバージョンで確認を行っています。

|        | バージョン | 備考 |
| ------ | ---------- | ---- |
| Python | 3.13.0     | [.python-version](.python-version) |
| Flask  | 3.0.3      | [poetry.lock](poetry.lock) |

# パッケージのインストール

[poetry](https://python-poetry.org/) で管理しています。
本リポジトリを利用する際は、事前に下記を実行してパッケージのインストールを行い、依存関係を解決しておいてください。

```bash
$ poetry install
```

# 起動

次のコマンドでアプリケーションが起動します。

```bash
# 仮想環境内でのコマンドの実行
$ poetry run python app/run.py
```

# フォーマッター

## 事前準備
Git フックを利用して commit 時にフォーマッターを実行するようにしています。
お手元の環境で試される場合は事前に

```bash
% pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

で `pre-commit` をインストールしておいてください。

## 手動で実行

手動で実行したい場合は下記で実行できます。

```bash
pre-commit run --all-files
```
