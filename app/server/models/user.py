from server import db
from passlib.hash import pbkdf2_sha256 as sha256


class UserModel(db.Model):
  """
  ユーザアカウントモデル
    :param db.Model: DBモデル
  """
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def save_to_db(self):
    """
    アカウントをDBに登録する
      :param self: UserModel のインスタンス
    """
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_username(cls, username):
    """
    登録されているユーザアカウントを検索する
      :param cls: UserModel クラス( インスタンスに非ず )
      :param username: ユーザ名
    """
    return cls.query.filter_by(username=username).first()

  @classmethod
  def return_all(cls):
    """
    登録されているユーザアカウント全てをリストで返却する
      :param cls: UserModel クラス( インスタンスに非ず )
    """
    def to_json(x):
      return {
          'username': x.username,
          'password': x.password
      }
    return {'users': list(map(lambda x: to_json(x), UserModel.query.all()))}

  @classmethod
  def delete_all(cls):
    """
    登録されているユーザアカウントを全て削除する
      :param cls: UserModel クラス( インスタンスに非ず )
    """
    try:
      num_rows_deleted = db.session.query(cls).delete()
      db.session.commit()
      return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
    except:
      return {'message': 'Something went wrong'}

  @staticmethod
  def generate_hash(password):
    """
    パスワードをハッシュ化する
      :param password: ハッシュ化するパスワード
    """
    return sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    """
    パスワードをハッシュ化して既存のものと一致するかチェックする
      :param password: チェック対象のパスワード
      :param hash: ハッシュ化されたパスワード
    """
    return sha256.verify(password, hash)
