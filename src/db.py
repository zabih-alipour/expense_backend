import sqlite3

db_path = "./HomeExpenses.db"


def add_subject(subject):
    sql = ''' INSERT INTO item ("name") VALUES (?) '''

    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql, subject)
        conn.commit()
        return cur.lastrowid


def get_subjects():
    sql = ''' SELECT * FROM item '''
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


def add_invoice(invoice):
    sql = ''' INSERT INTO factore ("factor_date", "item_id", "description", "price", "quality") 
                VALUES (?, ?, ?, ?, ?) '''
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql, invoice)
        conn.commit()
        return cur.lastrowid


def get_invoices(subject):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        if subject is None:
            sql = ''' SELECT * FROM factore '''
            cur.execute(sql)
        else:
            sql = ''' SELECT * FROM factore f WHERE f.item_id=?'''
            cur.execute(sql, subject)

        return cur.fetchall()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
