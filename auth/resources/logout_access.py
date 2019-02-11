from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt
)
from auth.models.revoked_token import RevokedTokenModel


class UserLogoutAccess(Resource):
  """
  ログアウトアクセスクラス
    :param Resource: 親クラス。REST-API のリソースクラス
  """

  @jwt_required
  def post(self):
    """
    logout/access API の POST メソッド。認証トークンを失効する。
      :param self: UserLogoutAccess クラスのインスタンス
    """
    jti = get_raw_jwt()['jti']
    try:
      revoked_token = RevokedTokenModel(jti=jti)
      revoked_token.add()
      return {'message': 'Access token has been revoked'}
    except:
      return {'message': 'Something went wrong'}, 500
