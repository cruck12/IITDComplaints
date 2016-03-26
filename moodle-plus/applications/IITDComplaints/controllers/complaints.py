# -*- coding: utf-8 -*-
# try something like
def index():
    return dict(message="hello from complaints.py")

def complaint():
    if len(request.args)<1:
		raise HTTP(404)
    id_complaint = str(request.args[0]).lower()
    complaint = db(db.Complaints.id_complaint==id_complaint).select()
    if len(complaint)>0:
        complaint = complaint.first()
    else:
        raise HTTP(404)
    comments = []
    if len(complaint)>0:
        comments=db(db.Comments.id_complaint==id_complaint).select()
    else:
        raise HTTP(404)
    return dict(complaint=complaint, comments=comments)

def get_sent():
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    complaints=[]
    complaints= db((db.Complaints.id_user==id_user)&(db.Complaints.resolved==0)).select()
    return dict(complaints=complaints)

def get_incoming():
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    id_hostel = db(db.users.id_user==id_user).select(db.users.id_hostel)
    complaints=[]
    complaints= db(((db.Complaints.complaintTo==id_user)|(db.Complaints.type==0)|((db.Complaints.id_hostel==id_hostel)&(db.Complaints.type==1)))&(db.Complaints.resolved==0)).select()
    return dict(complaints=complaints)

def get_resolved():
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    id_hostel = db(db.users.id_user==id_user).select(db.users.id_hostel)
    complaints=[]
    complaints= db((((db.Complaints.complaintTo==id_user)|(db.Complaints.type==0)|((db.Complaints.id_hostel==id_hostel)&(db.Complaints.type==1)))|(db.Complaints.id_user==id_user))&(db.Complaints.resolved==1)).select()
    return dict(complaints=complaints)
