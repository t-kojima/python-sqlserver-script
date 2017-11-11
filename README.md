# python-sqlserver-script

## これは何ですか？
SQLServerに対し何らかの処理を施したSQLを発行するPythonスクリプトのテンプレートです。

### どういう使い方をしますか？
1. ファイルだったりSQLだったりから入力データを作成する。
1. 何らかの処理を施したり、施さなかったりする。
1. 処理したデータをUPDATEしたりINSERTしたりする。

### ストアドで良くないですか？
ファイルの取込が面倒なので…

## 環境
- Linuxの場合FreeTDSが必要です。


## 使い方
- pyodbcインストール  
`pip install pyodbc`
- `database.json`を修正
- `script.py`を修正
- `# python script.py`で実行
