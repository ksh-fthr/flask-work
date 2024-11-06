import base64
import csv
import os
import zipfile
from datetime import datetime, timedelta
from io import StringIO

from flask import Flask
from flask_restful import Resource

TMP_PATH = "./tmp"


class Zip(Resource):
    def get(self) -> dict:
        """CSVファイルを複数作ってZIPに固めて返却する

        Returns:
          Response -- レスポンスオブジェクト

        Description:
          CSVファイルの出力を行った上でZIPに固めて返却する
          ZIPは base64エンコードした上で文字列化する
        """
        # CSVファイル出力のための準備
        os.makedirs(TMP_PATH, exist_ok=True)

        res: dict = self.__create_zip_file()

        # 後始末. 作成した CSV ファイルや ZIP ファイルを削除する
        # CSV生成処理である `create_csv_monthly` の中でやると zip ファイルが掴まれたままで
        # `PermissionError` が発生するので、仕方なくメソッドを抜けたあとに後始末を行う
        self.__delete_files(TMP_PATH)

        return res

    def __create_zip_file(self) -> dict:
        """[summary]

        Returns:
          dict -- ファイル名と base64文字列化したZIPファイルのデータをセットした dict
        """
        #
        #  サンプルコードなのでヘッダもデータも各ファイルで使いまわす
        #

        # ヘッダレコードとボディレコードを作る
        header_record = ["名前", "年齢", "住所", "電話番号", "備考"]
        body_record = ["ほげ", "99歳", "ほげ県ほげほげ市", "999-9999-9999", ""]

        # CSVファイル名
        # ファイル名のフォーマットは ${STR}_${STR}_${YYYYMMDD}. とし、${STR} は任意の文字列が入る
        # ${YYYYMMDD} には西暦での年月日が入る
        date_time = datetime.now().strftime("%Y%m%d")
        output_path1 = "{}_{}_{}.csv".format("好きな", "文字1", date_time)
        output_path2 = "{}_{}_{}.csv".format("好きな", "文字2", date_time)
        output_path3 = "{}_{}_{}.csv".format("好きな", "文字3", date_time)

        # CSVファイルを作成する
        with open(self.__make_file_path(TMP_PATH, output_path1), "w") as f1:
            writer = csv.writer(
                f1, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n"
            )
            writer.writerow(header_record)
            writer.writerow(body_record)

        with open(self.__make_file_path(TMP_PATH, output_path2), "w") as f2:
            writer = csv.writer(
                f2, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n"
            )
            writer.writerow(header_record)
            writer.writerow(body_record)

        with open(self.__make_file_path(TMP_PATH, output_path3), "w") as f3:
            writer = csv.writer(
                f3, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\n"
            )
            writer.writerow(header_record)
            writer.writerow(body_record)

        # ZIPファイル名の例
        # テスト店_月次集計_20190520.zip
        file_name_zip = "{}_{}_{}.zip".format("ZIP", "ファイル", date_time)

        # ZIP ファイルを生成
        with zipfile.ZipFile(
            self.__make_file_path(TMP_PATH, file_name_zip),
            "w",
            compression=zipfile.ZIP_DEFLATED,
        ) as new_zip:
            new_zip.write(
                self.__make_file_path(TMP_PATH, output_path1), arcname=output_path1
            )
            new_zip.write(
                self.__make_file_path(TMP_PATH, output_path2), arcname=output_path2
            )
            new_zip.write(
                self.__make_file_path(TMP_PATH, output_path3), arcname=output_path3
            )

        # ZIP ファイルを base64 エンコード
        # ただしそのままだとバイナリなので JSON 形式でレスポンスを返せない
        # -> decode することで文字列として扱うことで JSON 形式に対応させる
        #
        # つまり
        #   binary ファイル読み込み -> base64encode -> decode で文字列化
        # している
        fzip = open(self.__make_file_path(TMP_PATH, file_name_zip), "br")
        fzip_64encoded = base64.b64encode(fzip.read())
        res: dict = {"fileName": file_name_zip, "zip": fzip_64encoded.decode("utf-8")}

        return res

    def __make_file_path(self, dir_path: str, file_name: str) -> str:
        """ファイルパスを作成する

        Arguments:
          dir_path {str} -- ディレクトリパス
          file_name {str} -- ファイル名

        Returns:
          str -- ファイル名まで含めたパス
        """
        return "{}/{}".format(dir_path, file_name)

    def __delete_files(self, dir_path: str) -> None:
        """CSVファイル出力後にできたファイルを削除する

        Arguments:
          dir_path {str} -- ディレクトリパス

        Returns:
          None -- なし
        """
        files: list = os.listdir(dir_path)
        for file in files:
            try:
                # tmp ファイルの下は zip と csv しかないのでディレクトリのケアは必要ない
                target = self.__make_file_path(dir_path, file)
                os.remove(target)
            except:
                # 本来こないハズのルート
                # os.remove() ではディレクトリの削除で例外(`PermissionError`)が発生するが
                # まあ発生しても 数kb 程度のゴミが残るだけなので放っておく
                continue

        return None
