from flask_restful import Resource
from server.models.user import UserModel


class AllUsers(Resource):
  """
  全ユーザアカウント管理クラス
    :param Resource: 親クラス。REST-API のリソースクラス
  """

  def get(self):
    """
    user API の GET メソッド。全ユーザアカウントを取得する。
      :param self: AllUsers クラスのインスタンス
    """
    return UserModel.return_all()

  def delete(self):
    """
    user API の DELETE メソッド。全ユーザアカウントを削除する。
      :param self: AllUsers クラスのインスタンス
    """
    return UserModel.delete_all()
