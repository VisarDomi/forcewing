from forcewing import db, bcrypt
from forcewing.models import User 

db.drop_all()
db.create_all()
hashed_pw = bcrypt.generate_password_hash('forcewing').decode('utf-8')
user = User(username='Forcewing', password=hashed_pw)
db.session.add(user)
db.session.commit()
