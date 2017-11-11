# !/usr/bin/env python3
# coding: utf-8
"script.py"

from database import Database
db = Database()

# read file
with open('hoge.txt') as f:
    targets = [line.strip() for line in f.readlines()]

# read records
targets = db.select("SELECT * FROM <TABLENAME>")

for target in targets:
    # execute
    sql = "UPDATE <TABLENAME> SET Column1 = {0} WHERE Column2 = 'fuga'".format(
        target[0])
    db.execute(sql)
