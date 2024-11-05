from flask import Flask
from flask_restful import Resource
from datetime import datetime, timedelta
import csv
from io import StringIO


class Csv(Resource):
    def get(self) -> dict:
        """CSVデータを作って返却する

        Returns:
            Response -- レスポンスオブジェクト

        Description:
            CSVファイルの出力は行わず、作成したデータとファイル名を返却する
        """
        # CSVファイル名
        # ファイル名のフォーマットは ${STR}_${STR}_${YYYYMMDD}. とし、${STR} は任意の文字列が入る
        # ${YYYYMMDD} には西暦での年月日が入る
        date_time = datetime.now().strftime("%Y%m%d")
        output_path = "{}_{}_{}.csv".format("好きな", "文字", date_time)

        # CSVデータを返却する
        f = StringIO()
        writer = csv.writer(
            f, quotechar='"', quoting=csv.QUOTE_ALL, lineterminator="\r\n"
        )

        # ヘッダレコードとボディレコードを作る
        header_record = ["名前", "年齢", "住所", "電話番号", "備考"]
        body_record = ["ほげ", "99歳", "ほげ県ほげほげ市", "999-9999-9999", ""]
        writer.writerow(header_record)
        writer.writerow(body_record)

        res: dict = {"fileName": output_path, "csv": f.getvalue()}

        return res
