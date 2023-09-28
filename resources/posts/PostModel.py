from app import db
from datetime import datetime

# when having a one to many connection, the foreign key always goes on the MANY side

class PostModel(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String, default=datetime.utcnow)
    # table name and column name with . notation (users from UserModel, looking at the id)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Post: {self.body}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
