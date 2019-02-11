"""
auth ディレクトリ配下をモジュールとして扱うための初期処理
"""

from flask import Flask
from flask import jsonify                 # response に JSON を返すの楽にしてくれる
from flask_restful import Api             # HTTPメソッドと python コードのメソッドを対応させてくれる
from flask_sqlalchemy import SQLAlchemy   # ORM
from flask_jwt_extended import JWTManager  # JSON Web Token

app = Flask(__name__)
app.config.from_object('auth.conf.config')

api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


import auth.models.user
import auth.models.revoked_token
import auth.resources.router


# REST-API Routing
api.add_resource(auth.resources.router.UserRegistration, '/registration')
api.add_resource(auth.resources.router.UserLogin, '/login')
api.add_resource(auth.resources.router.UserLogoutAccess, '/logout/access')
api.add_resource(auth.resources.router.UserLogoutRefresh, '/logout/refresh')
api.add_resource(auth.resources.router.TokenRefresh, '/token/refresh')
api.add_resource(auth.resources.router.AllUsers, '/users')

# DB
@app.before_first_request
def create_tables():
  """
  DB、テーブルを生成する
  """
  db.create_all()


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
  """
  トークンがブラックリストにあるか否かをチェックする
    :param decrypted_token: チェック対象のトークン
  """
  jti = decrypted_token['jti']
  return auth.models.revoked_token.RevokedTokenModel.is_jti_blacklisted(jti)
