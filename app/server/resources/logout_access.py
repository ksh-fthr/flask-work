from flask_jwt_extended import get_jwt, jwt_required
from flask_restful import Resource
from server.models.revoked_token import RevokedTokenModel


class UserLogoutAccess(Resource):
    """
    ログアウトアクセスクラス
      :param Resource: 親クラス。REST-API のリソースクラス
    """

    @jwt_required(refresh=True)
    def post(self):
        """
        logout/access API の POST メソッド。認証トークンを失効する。
          :param self: UserLogoutAccess クラスのインスタンス
        """
        jti = get_jwt()["jti"]
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {"message": "Access token has been revoked"}
        except:
            return {"message": "Something went wrong"}, 500
