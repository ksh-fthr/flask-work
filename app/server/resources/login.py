from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, reqparse
from server.models.user import UserModel

parser = reqparse.RequestParser()
parser.add_argument("username", help="This field cannot be blank", required=True)
parser.add_argument("password", help="This field cannot be blank", required=True)


class UserLogin(Resource):
    """
    ログイン認証クラス
      :param Resource: 親クラス。REST-API のリソースクラス
    """

    def post(self):
        """
        login API の POST メソッド。ログイン認証を行う。
          :param self: UserLogin クラスのインスタンス
        """
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data["username"])

        if not current_user:
            return {"message": "User {} doesn't exist".format(data["username"])}

        if UserModel.verify_hash(data["password"], current_user.password):
            access_token = create_access_token(identity=data["username"])
            refresh_token = create_refresh_token(identity=data["username"])
            return {
                "message": "Logged in as {}".format(current_user.username),
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
        else:
            return {"message": "Wrong credentials"}
