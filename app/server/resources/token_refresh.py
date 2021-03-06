
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_refresh_token_required,
    get_jwt_identity
)


class TokenRefresh(Resource):
  """
  トークン更新クラス
    :param Resource: 親クラス。REST-API のリソースクラス
  """
  @jwt_refresh_token_required
  def post(self):
    """
    token/refresh API の POST メソッド。更新トークンを使用してアクセストークンを再発行する。
      :param self: TokenRefresh クラスのインスタンス
    """
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return {'access_token': access_token}
