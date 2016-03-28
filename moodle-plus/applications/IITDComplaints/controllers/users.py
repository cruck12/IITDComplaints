# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from users.py")

def getAll():
    users=[]
    users=db((db.users.id>0)&(db.users.verified==1)).select(db.users.id,db.users.first_name,db.users.type)
    return dict(users=users)

def getUser():
    if len(request.args)<1:
        raise HTTP(404)
    user_id = str(request.args[0]).lower()
    users=db((db.users.id==user_id)&(db.users.verified==1)).select(db.users.id,db.users.first_name,db.users.type)
    return dict(users=users)
