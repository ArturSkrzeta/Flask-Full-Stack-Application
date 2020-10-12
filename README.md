<h2>Flask Full Stack Application</h2>

<h3>Intro</h3>
<ul>
  <li>With SQLAlchemy we can represent database structure as classes called models.=</li>
  <li>Each class represents data schema, so it is a sinle table in a database.</li>
</ul>


<h3>Installation</h3>
<ul>
  <li>In terminal:
    <br>
    - pip install flask<br>
    - pip install flask-sqlalchemy
  </li>
  <li>In main.py:
    <br>
    > app = Flask(__name__)<br>
    > from flask_sqlalchemy import SQLAlchemy<br>
    > app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// indicates relative path of a project - db will be created in main directory<br> 
    > db = SQLAlchemy(app)<br>
  </li>
  <li>In Python interpreter (project directory):
    <br>
    > from main import db<br>
    > db.create_all()<br>
    > from main import ExerciseSet<br>
    > set1 = ExerciseSet(name='Bench Press', weight=80, reps=6)<br>
    > set2 = ExerciseSet(name='Bench Press', weight=90, reps=5)<br>
    > set3 = ExerciseSet(name='Bench Press', weight=100, reps=3)<br>
    > db.session.add(set1)<br>
    > db.session.add(set2)<br>
    > db.session.add(set3)<br>
    > db.session.commit()<br>
    > ExerciseSet.query.all()<br>
    > ExerciseSet.query.first()<br>
    > ExerciseSet.query.filter_by(name='Bench Press').all()<br>
    > bench = ExerciseSet.query.filter_by(name='Bench Press').first()<br>
    > ex1 = ExerciseSet.query.get(1)<br>
    > bench.weight<br>
    > db.drop_all() # drops all db's tables
  </li>
  <li>Quering db with filters:
    <br>
    > e = ExerciseSet.query.filter_by(name='B').all()<br>
    > e = ExerciseSet.query.filter_by(name='B').all()[-1] # getting last item<br>
  </li>
</ul>

<h3>Package Structure</h3>
<ul>
  <li>Directory 'application' with __init__.py defined becomes python package.</li>
  <li>In __init__.py, I create app instance.</li>
  <li>I can import from it then: <b>from application import app</b> as if <b>from application.__init__.py import app</b>.</li>
  <li>Any other modules from 'application' package can be iumported according to: <b>from package.module import class</b> -> <b>from application.models import MyModel</b>.</li>
  <br>
  <img src="images/init_app.JPG">
  <br>
  <br>
  <li>Project structre:</li>
  <br>
  <img src="images/tree.JPG">
  <br>
  <br>
  <li>Running Flask server with <b>python run.py</b></li>
</ul>

<h3>SQLALchemy</h3>
<ul>
  <li>Creating model instance = table row, we need to provide <b>keyword arguments</b>:</li>
  <br>
  <img src="images/interpreter.JPG">
  <br>
  <br>
  <li>filter_by with multiple criterias:
    <br>
    - set.query.filter_by(week=1, name="Squat").first().w
  </li>
  <li>Taking last item:
    <br>
    - set.query.filter_by(name='Bench Press').all()[-1].w
  </li>
</ul>

<h3>Forms</h3>
<ul>
  <li>Library installation: pip install flask-wtf.</li>
  <li>Python import: from flask_wtf import FlaskForm.</li>
  <li>Python classes are representative of forms. They will be automatically converted into HTML forms within a template.</li>
  <li>Form fileds are imported from wtforms:
    <br>
    - from wtforms import StringField<br>
    - username = StringField()
  </li>
  <li>Validators for validation are imported from wtforms.validators:
    <br>
    - from wtforms.validators import DataRequired, Length<br>
    - username = StringField('Username', validators=[DataRequired(), Length(min=2,max=20)])<br>
    - first argument is the html label
  </li>
  <li>Submit button:
    <br>
    - from wtforms import SubmitField<br>
    - submit = SubmitField('Submit')
  </li>
  <li>Bolean field:
    <br>
    - from wtforms import BooleanField<br>
    - remember = BooleanField('Remember Me')
  </li>
  <li>Dropdown field:
    <br>
    - from wtforms import SelectField
    - name = SelectField('Exercise Name', choices=['Bench Press','Deadlift','Squat'])
  </li>
  <li>Importing form into routes
    <br>
    <img src="images/forms_in_routes.JPG">
  </li>
</ul>
