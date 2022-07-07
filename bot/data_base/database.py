import sqlite3

def sql_start():
    global base, cur, base_adm, cur_adm
    base = sqlite3.connect("data_base/user1.db")
    cur = base.cursor()
    if base:
        print("Databese connected OK")
    base.execute('CREATE TABLE IF NOT EXISTS data(user_id TEXT PRIMARY KEY, user_city TEXT)')
    base.commit()

async def new_user_db(user_id, user_city):
    cur.execute('INSERT INTO data VALUES(?, ?)', (user_id, user_city))
    base.commit()

async def user_check(user_id):
    r = cur.execute("SELECT user_city FROM data WHERE user_id == ?", (user_id,)).fetchone()
    base.commit()
    return r

async def user_update(user_id, user_city):
    r = cur.execute("UPDATE data SET user_city = ? WHERE user_id == ?", (user_city, user_id))
    base.commit()
    return r
