from init import db, ma
from marshmallow import fields

class Card(db.Model):
    __tablename__ = "cards"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    date = db.Column(db.Date) # Date created
    status = db.Column(db.String)
    priority = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="cards")

class CardSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name", "email"]) # nested defines the relationship

    class Meta: # where we define the sfields of the Meta
        fields = ("id", "title", "description", "date", "status", "priority", "user")
        ordered = True # whatever we return in this field this will respect the order above, instead of dumping in abc order

cards_schema = CardSchema() # creatig our card schema
cards_schema = CardSchema(many=True)
