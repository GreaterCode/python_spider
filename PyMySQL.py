import pymysql

def close_database(db):
    db.close()

def create_database(db):
    cursor = db.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print('Database version:', data)
    cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8')

def build_connect():
    db = pymysql.connect(host='localhost', user='root', password='renwoxing', port=3306, db='spiders')
    return db
def create_table(db):
    cursor = db.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
    cursor.execute(sql)

def insert_data(db):
    data = {
        'id': '2001',
        'name': 'renwoxing',
        'age': '23'
    }
    cursor = db.cursor()
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table} ({keys}) VALUES  ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('successful')
            db.commit()
    except Exception as e:
        db.rollback()


def main():
    db = build_connect()
    create_table(db)
    close_database()

if __name__ == '__main__':
    main()