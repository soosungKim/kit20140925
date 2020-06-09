import sqlite3

def dbcon():
    return sqlite3.connect('mydb.db')

def create_table():
    try:
        query = '''
            CREATE TABLE "user" (
                "id" varchar(50),
                "pw" varchar(50),
                "name" varchar(50),
                PRIMARY KEY ("id")
            )
        '''
        db = dbcon()
        c = db.cursor()
        c.execute(query)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()


def insert_data(num, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num, name)
        c.execute("insert into student VALUES (?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('select * from student')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def select_num(num):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num, )
        c.execute('select * from student WHERE num = ?', setdata)
        ret = c.fetchone()
    except Exception as e :
        print('db error:', e)
    finally:
        db.close()
        return ret
    
#create_table
#insert_data('20140925', '디비')
#ret = select_all()
#print(ret)