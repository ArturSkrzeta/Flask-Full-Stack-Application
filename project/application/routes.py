from flask import render_template, url_for, redirect
from application import app, db
from application.models import Set
from application.forms import InsertionForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InsertionForm()
    last_week = Set.query.filter_by(name='Deadlift').all()[-1].week

    if form.week.data and form.deadlift.data and form.squat.data and form.bench_press.data:

        s1 = Set(week=form.week.data, name='Deadlift', w=form.deadlift.data, r=1)
        s2 = Set(week=form.week.data, name='Squat', w=form.squat.data, r=1)
        s3 = Set(week=form.week.data, name='Bench Press', w=form.bench_press.data, r=1)

        db.session.add(s1)
        db.session.add(s2)
        db.session.add(s3)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('index.html', set = Set, form=form, last_week=last_week)
