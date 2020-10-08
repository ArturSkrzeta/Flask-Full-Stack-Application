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
    > set1 = ExerciseSet('Bench Press', 80, 6)<br>
    > set2 = ExerciseSet('Bench Press', 90, 5)<br>
    > set3 = ExerciseSet('Bench Press', 100, 3)<br>
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
</ul>

