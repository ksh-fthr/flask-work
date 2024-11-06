from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource


class TokenRefresh(Resource):
    """
    トークン更新クラス
      :param Resource: 親クラス。REST-API のリソースクラス
    """

    @jwt_required(refresh=True)
    def post(self):
        """
        token/refresh API の POST メソッド。更新トークンを使用してアクセストークンを再発行する。
          :param self: TokenRefresh クラスのインスタンス
        """
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {"access_token": access_token}
