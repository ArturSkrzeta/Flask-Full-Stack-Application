<h2>?Flask Full Stack Application</h2>

<h3>Intro</h3>
<ul>
  <li></li>
  <li></li>
</ul>


<h3>Installation</h3>
<ul>
  <li>In terminal:
    <br>
    - pip install flask<br>
    - pip install flask-sqlalchemy
  </li>
  <li>In app:
    <br>
    > app = Flask(__name__)
    > from flask_sqlalchemy import SQLAlchemy
    > app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # /// indicates relative path of a project - db will be created in main directory 
    > db = SQLAlchemy(app)
  </li>
</ul>

