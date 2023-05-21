from main.entities.core.base import db

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))
    role = db.Column(db.String(64))

    movie = db.relationship('Movie', back_populates='actors_association')
    actor = db.relationship('Actor', back_populates='movies_association')

    def __init__(self, movie_id, actor_id, role):
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.role = role

    def __str__(self):
        return f'Role(id={self.id})'

    def __repr__(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "actor_id": self.actor_id,
            "role": self.role
        }