# -*- coding: utf-8 -*-
# try something like
def index():
    return dict(message="hello from complaints.py")

def complaint():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    id_complaint = str(request.args[0]).lower()
    complaint = db(db.Complaints.id==id_complaint).select()
##    if len(complaint)>0:
    complaint = complaint.first()
##    else:
##        raise HTTP(404)
    comments = []
##    if len(complaint)>0:
    comments=db(db.Comments.id==id_complaint).select()
##    else:
##        raise HTTP(404)
    return dict(complaint=complaint, comments=comments)


def get_sent():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    complaints=[]
    complaints= db((db.Complaints.user_id==id_user)&(db.Complaints.resolved==0)).select()
    return dict(complaints=complaints)

def get_incoming():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    id_hostels = db(db.users.id==id_user).select(db.users.hostel_id).first()
    id_hostel = id_hostels.hostel_id
    complaints=[]
    complaints= db(((db.Complaints.complaintTo_id==id_user)|(db.Complaints.Complaint_type==0)|((db.Complaints.hostel_id==id_hostel)&(db.Complaints.Complaint_type==1)))&(db.Complaints.resolved==0)).select()
    return dict(complaints=complaints)

def get_resolved():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    id_user = str(request.args[0]).lower()
    id_hostels = db(db.users.id==id_user).select(db.users.hostel_id).first()
    id_hostel = id_hostels.hostel_id
    complaints=[]
    complaints= db((((db.Complaints.complaintTo_id==id_user)|(db.Complaints.Complaint_type==0)|((db.Complaints.hostel_id==id_hostel)&(db.Complaints.Complaint_type==1)))|(db.Complaints.user_id==id_user))&(db.Complaints.resolved==1)).select()
    return dict(complaints=complaints)