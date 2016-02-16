# -*- coding: cp936 -*-
from copy import copy
from mysql import getDb
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
    
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')
        
class ModelMetaclass(type):
    def __new__(cls,name,bases,attrs):
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print ('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s==>%s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        if not attrs.has_key('__table__'):
            attrs['__table__'] = name # 
        attrs['__mappings__'] = mappings # 
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
    
    def modify(self,**kwargs):
        params = copy(self)
        try:
            params['where'] = kwargs['where']
            params['vars'] = kwargs['vars']
        except:
            params['where']='id='+str(self.id)
        getDb().update(self.__table__,**params)
    def remove(self):
        print 'remove'
    
    
    def save(self):
        it = getDb().insert(self.__table__,**self)
        setattr(self, 'id', it)
        return it
    
    @classmethod   
    def find(cls,**kwargs):
        rs = getDb().select(cls.__table__,**kwargs)
        return rs
    
    
    @classmethod
    def execute(cls,sql,**kwargs):
        rs = getDb().query(sql,**kwargs)
        '''
        if(isinstance(rs, long)):
            return rs
        else:
            
            for rcd in rs:
                rcd = dict(rcd)
                lst.append(rcd)
            return lst
        '''
        return rs
    
    '''
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))
    '''

class Url(Model):
    ''
    __table__ = 'su_url'
    id = IntegerField('id')
    url = StringField('url')
    hash = StringField('hash')
    
    
if __name__ == '__main__':
#     r = Room(id = 1,no=2)
#     r.modify()
    lst = Room.find(what='id',where='id=1')
    for rm in lst:
        print rm
    lst = Room.execute('update po_room set no=no+1 where id=$id ',id=1)
    print lst
    
    
    
