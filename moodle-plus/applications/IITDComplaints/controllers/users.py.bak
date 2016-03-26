# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from users.py")

def getAll():
    users=[]
    users=db((db.users.id>0)&(db.users.verified==1)).select(db.users.id,db.users.first_name,db.users.type)
    return dict(users=users)
