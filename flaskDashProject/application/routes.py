from application import app 
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpenses
from application import db
import json

@app.route('/')
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    with app.app_context():
        return render_template("index.html", entries=entries)

@app.route('/layout')
def layout():
    with app.app_context():
        return render_template("layout.html", title = 'layout')

@app.route('/add', methods = ['GET','POST'])
def add_expense():
    with app.app_context():
        form = UserInputForm()
        if form.validate_on_submit():
            entry = IncomeExpenses(id=form.id.data, type=form.type.data, category=form.category.data, amount=form.amount.data)
            # entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data)
            db.session.add(entry)
            db.session.commit()
            flash(f"{form.type.data} has been added to {form.type.data}s", "success")
            return redirect(url_for('index'))
        return render_template("add.html", title = 'add', form = form)  
 

@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))