from App.models import Admin
from App.database import db

def create_Admin(username, password, website):
    Here = Admin.query.filter_by(username=username).first()
    if Here:
        print(f'{username} already exists!')
        return Here  
    newA = Admin(username=username, password=password, website=website)
    try:
      db.session.add(newA)
      db.session.commit()
      print(f'New Admin: {username} created!')
    except Exception as e:
      db.session.rollback()
      print(f'Something went wrong creating {username}')
    return newA  


def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def get_admin(id):
    return Admin.query.get(id)

def get_all_admins():
    return Admin.query.all()

def get_all_admins_json():
    admins = Admin.query.all()
    if not admins:
        return []
    admins = [admin.get_json() for admin in admins]
    return admins

def update_admin(id, username):
    admin = get_admin(id)
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None
    