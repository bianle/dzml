# -*- coding: cp936 -*-
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import web
def getDb():
    host = 'localhost'
    db = 'test'
    port = 3306
    user = 'root'
    pw = 'toor'
    try:
        import sae.const

        db = sae.const.MYSQL_DB      # ���ݿ���
        user = sae.const.MYSQL_USER    # �û���
        pw = sae.const.MYSQL_PASS    # ����
        host = sae.const.MYSQL_HOST    # �����������ɶ�д��
        port = int(sae.const.MYSQL_PORT)    # �˿ڣ�����Ϊ<type 'str'>������ݿ��Ҫ������ת��Ϊint
        #sae.const.MYSQL_HOST_S  # �ӿ�������ֻ����
    except ImportError:
        pass
    return web.database(dbn='mysql',host=host,port=port, db=db, user=user, pw = pw);
def test():
    msg = ''
    db = getDb()
    db.insert('test',id=1,name='testestestestsetest')
    li = db.query('select id,name from test ')
    for rcd in li:
        msg+= '|'+bytes(rcd.id) +'|'+ bytes(rcd.name)+'|\n'
    id = 1
    db.update('test', name='test' ,where='id=$id' ,vars=locals())
    li = db.select('test',what='id,name,id as idd')
    for rcd in li:
        msg+= '|'+bytes(rcd.id) +'|'+ rcd.name+'|'+bytes(rcd.idd)+'|\n'
    db.delete('test', where = 'id = $id', vars = locals())
    return msg;
if __name__ == "__main__":
    db = getDb()
    db.insert('test',id=1,name='testestestestsetest')
    li = db.query('select id,name from test ')
    for rcd in li:
        print '|'+bytes(rcd.id) +'|'+ rcd.name+'|'
    id = 1
    db.update('test', name='test' ,where='id=$id' ,vars=locals())
    li = db.select('test',what='id,name,id as idd')
    for rcd in li:
        print '|'+bytes(rcd.id) +'|'+ rcd.name+'|'+bytes(rcd.idd)
    db.delete('test', where = 'id = $id', vars = locals())
