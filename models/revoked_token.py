from manage import db


class RevokedTokenModel(db.Model):
  """
  失効トークンモデル
    :param db.Model: DBモデル
  """

  __tablename__ = 'revoked_tokens'
  id = db.Column(db.Integer, primary_key=True)
  jti = db.Column(db.String(120))

  def add(self):
    """
    失効されたトークンを追加する
      :param self: RevokedTokenModel のインスタンス
    """
    db.session.add(self)
    db.session.commit()

  @classmethod
  def is_jti_blacklisted(cls, jti):
    """
    トークンが失効しているか否かをチェックスする
      :param cls: RevokedTokenModel クラス( インスタンスに非ず )
      :param jti: チェック対象のトークン
    """
    query = cls.query.filter_by(jti=jti).first()
    return bool(query)
