from App.models import Competition,User, UserCompetition
from App.database import db

def create_Competition(name, creator_id):
    Here= Competition.query.filter_by(name=name).first()
    if Here:
        print(f'{name} already exists!')
        return Here
    newComp = Competition(name=name, creator_id=creator_id)
    try:
      db.session.add(newComp)
      db.session.commit()
      print(f'{name} created!')
    except Exception as e:
      db.session.rollback()
      print(f'Something went wrong creating {name}')
    return newComp

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competition = Competition.query.all()

    if not competition:
        return []
    else:
        return [comp.toDict() for comp in competition]


def get_competition_by_id(id):
    competition = Competition.query.get(id)
    return competition


def add_results(user_id, comp_id, rank):
    Comp = Competition.query.get(comp_id)
    user = User.query.get(user_id)     
            
    if user and Comp:
        compParticipant = UserCompetition(user_id = user.id, comp_id = Comp.id, rank=rank)


        try:
            db.session.add(compParticipant)
            db.session.commit 
            print("successfully added user to comp")
            return True
        except Exception as e:
            db.session.rollback()
            print("error adding to comp")
            return False
        return False



def get_competition_users(comp_id):
    Comp = get_competition_by_id(comp_id)
    

    if Comp:
        compUsers = Comp.participants
        Participants = [User.query.get(part.user_id) for part in compUsers]
        print(Participants)
