#core/models.py

from core import db

class Transaction(db.Model):

    __tablename__="modele"

    id=db.Column(db.Integer, primary_key=True,unique=True,autoincrement=True,nullable=False)
    modele_attribut1=db.Column(db.Integer)
    modele_attribut2=db.Column(db.String(64),nullable=False)

    def __init__(self,attribut1,attribut2):
        self.modele_attribut1=attribut1
        self.modele_attribut2=attribut2