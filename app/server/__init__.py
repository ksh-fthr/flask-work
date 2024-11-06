"""
server ディレクトリ配下をモジュールとして扱うための初期処理
"""

from flask import jsonify  # response に JSON を返すの楽にしてくれる
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager  # JSON Web Token
from flask_restful import Api  # HTTPメソッドと python コードのメソッドを対応させてくれる
from flask_sqlalchemy import SQLAlchemy  # ORM

app = Flask(__name__)
app.config.from_object("server.conf.config")

CORS(app)
api = Api(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


from server.models import revoked_token
from server.resources import router

# REST-API Routing
api.add_resource(router.UserRegistration, "/registration")
api.add_resource(router.UserLogin, "/login")
api.add_resource(router.UserLogoutAccess, "/logout/access")
api.add_resource(router.UserLogoutRefresh, "/logout/refresh")
api.add_resource(router.TokenRefresh, "/token/refresh")
api.add_resource(router.AllUsers, "/users")
api.add_resource(router.Csv, "/csv")
api.add_resource(router.Zip, "/zip")


@app.before_request
def create_tables():
    """
    DB、テーブルを生成する
    """
    db.create_all()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """
    トークンがブラックリストにあるか否かをチェックする
      :param decrypted_token: チェック対象のトークン
    """
    jti = decrypted_token["jti"]
    return revoked_token.RevokedTokenModel.is_jti_blacklisted(jti)
