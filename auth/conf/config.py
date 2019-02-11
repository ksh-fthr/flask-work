# DB への PATH
SQLALCHEMY_DATABASE_URI = 'sqlite:///db/auth.sqlite3'

# データベースの設定と、セッション情報を暗号化するためのキー
import os
SECRET_KEY = os.urandom(24)

# アプリ起動時の warning を抑止する
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Json Web Token の設定
# HS *などの対称ベースの署名アルゴリズムに必要な秘密鍵
JWT_SECRET_KEY = os.urandom(24)
# トークンの無効化を有効または無効にする。デフォルトはFalse(無効)
JWT_BLACKLIST_ENABLED = True
# ブラックリストと照合するトークンの種類で、オプションは 'refresh'または 'access'
# シーケンスやセットを渡して、複数の種類をチェックする。デフォルトは（ 'access'、 'refresh'）
# ブラックリストが有効になっている場合にのみ使用される
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
