from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from server.models.revoked_token import RevokedTokenModel


class UserLogoutRefresh(Resource):
    """
    ログアウトリフレッシュクラス
      :param Resource: 親クラス。REST-API のリソースクラス
    """

    @jwt_required(refresh=True)
    def post(self):
        """
        logout/refresh API の POST メソッド。認証トークンを再発行する。
          :param self: UserLogoutRefresh クラスのインスタンス
        """
        jti = get_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {"message": "Refresh token has been revoked"}
        except:
            return {"message": "Something went wrong"}, 500
