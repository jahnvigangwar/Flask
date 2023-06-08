from application import db
from datetime import datetime

class IncomeExpenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), default='income', nullable=False)
    category = db.Column(db.String(30), nullable=False, default='rent')
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False)
    
    def __str__(self):
        return f"IncomeExpenses {self.id}: {self.category}"




# entry1 = IncomeExpenses(id = 1, type = "income", amount=4000, category="salary")
# entry2 = IncomeExpenses(id = 2, type = "expense", amount=3000, category="rent")
# entry3 = IncomeExpenses(id = 3, type = "expense", amount=2000, category="feeding")

# with app.app_context():
#      db.session.add(entry3)

# with app.app_context():
#      db.session.commit()

#with app.app_context():
#   entries = IncomeExpenses.query.all()

# with app.app_context():
#      for entry in entries: 
#             print(f"{entry.type},{entry.category},{entry.date},{entry.amount} ")


# IncomeExpenses.query.get(1).type

