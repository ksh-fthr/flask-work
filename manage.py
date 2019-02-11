# __pycache__ ディレクトリを生成させない
import sys
sys.dont_write_bytecode = True

# auth 配下のモジュールをアプリケーションとして起動する
from auth import app
if __name__ == "__main__":
  app.run(host='127.0.0.1', port=5000, debug=True)
