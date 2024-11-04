# __pycache__ ディレクトリを生成させない
import sys
sys.dont_write_bytecode = True

# server 配下のモジュールをアプリケーションとして起動する
from server import app
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
