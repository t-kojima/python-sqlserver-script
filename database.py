# !/usr/bin/env python3
# coding: utf-8
"database.py"

import json
import pyodbc


class Database:
    """common database class"""

    def __init__(self):
        """ database open """
        params = load_params()
        self.con = pyodbc.connect(
            "DRIVER={{SQL Server}};PORT=1433;SERVER={0};UID={1};PWD={2};DATABASE={3}".
            format(params['server'], params['user'], params['password'],
                   params['dbname']))
        self.cursor = self.con.cursor()

    def close(self):
        """ database close """
        self.cursor.close()
        self.con.close()

    def commit(self):
        """ database transaction commit """
        self.con.commit()

    def rollback(self):
        """ database transaction rollback """
        self.con.rollback()

    def execute(self, sql):
        """ query execute without results """
        self.cursor.execute(sql)

    def select(self, sql):
        """ query execute with results """
        self.cursor.execute(sql)
        return [record for record in self.cursor.fetchall()]


def load_params():
    """ load params from json """
    with open('./database.json', 'r', encoding='utf-8') as f:
        return json.load(f)
