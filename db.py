import sqlite3
from flask import g, _app_ctx_stack

DATABASE = 'db.sqlite'

class EnterableCursor(object):
    def __init__(self, conn):
        self.conn = conn

    def __enter__(self):
        self.conn.__enter__()
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.__exit__(type, value, traceback)

class FakeG:
    def in_app_ctx(self):
        return _app_ctx_stack.top is not None

    def __getattr__(self, key):
        if self.in_app_ctx():
            return getattr(g, key, None)
        else:
            return None

    def __setattr__(self, key, value):
        if self.in_app_ctx():
            setattr(g, key, value)
        return self

gg = FakeG()

def get_db():
    db = gg._database
    if db is None:
        db = gg._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return EnterableCursor(db)

def cleanup_db(exception):
    db = gg._database
    if db is not None:
        db.close()
