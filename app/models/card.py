from app import db
from flask import current_app


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)
    #child
        # lowercase 'board_id' looks at a table in your db
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'), nullable=True)

    def to_json(self): 
        return {  
            "card_id": self.card_id,   
            "message": self.message,
            "likes_count": self.likes_count,
            "board_id": self.board_id
        }
