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

def post_complaint():
    if not auth.is_logged_in():
        raise HTTP(404)
    user_id = request.vars["user_id"]
    hostel_id = request.vars["hostel_id"]
    name = request.vars["name"]
    ComplaintTo_id = request.vars["ComplaintTo_id"]
    Complaint_type = request.vars["Complaint_type"]
    description = request.vars["description"]
    Complaint_id = db.Complaints.validate_and_insert(user_id=user_id, hostel_id=hostel_id, complaintTo_id=ComplaintTo_id, Complaint_type=Complaint_type, name=name, description=description)
    return dict(success=False if not Complaint_id else True)

def upvote():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    complaint_id = str(request.args[0]).lower
    complaint = db(db.Complaints.id==complaint_id).select().first()
    complaint.update_record(upvote=db.Complaints.upvote+1)
    return dict(success=False if not complaint else True, complaint = db(db.Complaints.id==complaint_id).select().first())

def downvote():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    complaint_id = str(request.args[0]).lower
    complaint = db(db.Complaints.id==complaint_id).select().first()
    complaint.update_record(downvote=db.Complaints.downvote+1)
    return dict(success=False if not complaint else True, complaint = db(db.Complaints.id==complaint_id).select().first())

def resolve():
    if not auth.is_logged_in():
        raise HTTP(404)
    if len(request.args)<1:
		raise HTTP(404)
    complaint_id = str(request.args[0]).lower
    complaint = db(db.Complaints.id==complaint_id).select().first()
    user = db(db.users.id==complaint.user_id).select().first()
    if complaint.Complaint_type=="3":
        user.update_record(verified=1)
    complaint.update_record(resolved=1)
    return dict(success=False if not complaint else True, complaint = db(db.Complaints.id==complaint_id).select().first(), user=user)
