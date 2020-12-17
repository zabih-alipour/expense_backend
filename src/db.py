import sqlite3

db_path = "./HomeExpenses.db"


def add_subject(subject):
    sql = ''' INSERT INTO item ("name") VALUES (?) '''
    print(subject)
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql, (subject.get('name'),))
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
    item_id = 0
    subject_name = invoice.get("item").get("name")
    for p in get_subject_by_name(subject_name):
        item_id = p.get("id")

    if item_id == 0:
        item_id = add_subject({"name": subject_name})

    obj = (invoice.get("factor_date"),
           item_id,
           invoice.get("description"),
           invoice.get("price"),
           invoice.get("quantity"))

    sql = ''' INSERT INTO factore ("factor_date", "item_id", "description", "price", "quality") 
                VALUES (?, ?, ?, ?, ?) '''
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute(sql, obj)
        conn.commit()
        return cur.lastrowid


def get_invoices(subject):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        if subject is None or subject == 0:
            sql = ''' SELECT f.id, f.factor_date, f.item_id, f.description, f.price, f.quality, i.name as item_name  
                      FROM factore f 
                      join item i on f.item_id = i.id order by f.factor_date desc'''
            cur.execute(sql)
        else:
            sql = ''' SELECT f.id, f.factor_date, f.item_id, f.description, f.price, f.quality, i.name  as item_name
                      FROM factore f 
                      join item i on f.item_id = i.id 
                      WHERE i.id= ? order by f.factor_date desc '''
            cur.execute(sql, (subject,))

        return cur.fetchall()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_daily_expense():
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = ''' SELECT * FROM vw_daily_summary '''
        cur.execute(sql)
        return cur.fetchall()


def get_subject_expense():
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = ''' SELECT * FROM vw_item_summary '''
        cur.execute(sql)
        return cur.fetchall()


def get_subject_by_name(name):
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        sql = ''' SELECT * FROM item i where i.name like ? '''
        cur.execute(sql, (name + '%',))
        return cur.fetchall()
