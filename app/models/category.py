from database import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    tasks = db.relationship('Task', back_populates='category')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }
