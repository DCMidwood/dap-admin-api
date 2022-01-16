import folium
from flask import Flask, render_template, request, redirect, url_for, g, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import (
    DataRequired
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password123@localhost/dapadmin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "secretkey"
db = SQLAlchemy(app)

class dap_user(db.Model):
    __tablename__= 'dap_user'
    uid = db.Column(db.Integer, primary_key =True)
    user_name = db.Column(db.String(50), unique = True)
    user_email = db.Column(db.String(50), unique = True)

    def __init__(self, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email


class dap_project(db.Model):
    __tablename__ = 'dap_project'
    uid = db.Column(db.Integer, primary_key =True)
    project_name = db.Column(db.String(50), unique = True)
    project_db = db.Column(db.String(50), unique = True)

    def __init__(self, project_name, project_db):
        self.project_name = project_name
        self.project_db = project_db


class dap_role(db.Model):
    __tablename__ = 'dap_role'
    uid = db.Column(db.Integer, primary_key =True)
    role_name = db.Column(db.String(50), unique = True)
    role_level = db.Column(db.Integer, unique = False)

    def __init__(self,role_name, role_level):
        self.role_name = role_name
        self.role_level= role_level


class dap_workpack(db.Model):
    __tablename__ = 'dap_workpack'
    uid = db.Column(db.Integer, primary_key =True)
    workpack_name = db.Column(db.String(50), unique = True)
    project_id = db.Column(db.Integer, unique = False)
    workpack_extent = db.Column(db.String(100))

    def __init__(self, workpack_name, project_id, workpack_extent):
        self.workpack_name = workpack_name
        self.project_id = project_id
        self.workpack_extent = workpack_extent


class dap_workpack_user_role(db.Model):
    __tablename__ = 'workpack_user_role'
    uid = db.Column(db.Integer, primary_key =True)
    workpack_id = db.Column(db.Integer, unique = False)
    user_id = db.Column(db.Integer, unique = False)
    role_id = db.Column(db.Integer, unique = False)

    def __init__(self, workpack_id, user_id, role_id):
        self.workpack_id = workpack_id
        self.user_id = user_id
        self.role_id = role_id


class vdap_workpack_project(db.Model):
    __tablename__ = 'vdap_project_workpack'
    uid = db.Column(db.Integer, primary_key =True)
    workpack_id = db.Column(db.Integer, unique = False)
    workpack_name = db.Column(db.String(50), unique = True)
    workpack_extent = db.Column(db.String(100))    
    project_id = db.Column(db.Integer, unique = False)
    project_name = db.Column(db.String(100))   
    project_db = db.Column(db.String(100))

    def __init__(self, workpack_id, workpack_name, workpack_extent,
                        project_id, project_name, project_db):
        self.workpack_id = workpack_id
        self.workpack_name = workpack_name
        self.workpack_extent = workpack_extent   
        self.project_id = project_id
        self.project_name = project_name 
        self.project_db = project_db


class vdap_workpack_detais(db.Model):
    __tablename__ = 'vdap_workpack_detail'
    uid = db.Column(db.Integer, primary_key =True)
    workpack_id = db.Column(db.Integer, unique = False)
    workpack_name = db.Column(db.String(50), unique = True)
    workpack_extent = db.Column(db.String(50), unique = True)

    project_id = db.Column(db.Integer, unique = False)
    project_name = db.Column(db.String(50), unique = True)
    project_db = db.Column(db.String(50), unique = True)

    user_id = db.Column(db.Integer, unique = False)
    user_name = db.Column(db.String(50), unique = True)
    user_email = db.Column(db.String(50), unique = True)

    role_id = db.Column(db.Integer, unique = False)
    role_name = db.Column(db.String(50), unique = True)
    role_level = db.Column(db.String(50), unique = True)

    def __init__(self, workpack_id, workpack_name, workpack_extent,
                        project_id, project_name, project_db,
                        user_id, user_name, user_email,
                        role_id, role_name, role_level):
        self.workpack_id = workpack_id
        self.workpack_name = workpack_name
        self.workpack_extent = workpack_extent                     

        self.project_id = project_id
        self.project_name = project_name
        self.project_db = project_db        

        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email               

        self.role_id = role_id
        self.role_name = role_name
        self.role_level = role_level             


class NewWorkpackForm(FlaskForm):
    workpack_name = StringField("workpackname")
    project_id = SelectField('projectid', choices=[])
    workpack_extent = StringField("Workpack_extent")
    submit = SubmitField("Submit")


class NewWorkpackUserForm(FlaskForm):
    workpack_id = SelectField("Workpack", choices=[])
    user_id = SelectField("User", choices=[])
    role_id = SelectField("Role", choices=[])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    workpacks = vdap_workpack_project.query.all()
    projects = dap_project.query.all()
    return render_template("home.html",
                           workpacks=workpacks,
                           projects=projects
                           )


@app.route("/user/new", methods=["GET", "POST"])
def new_user():

    if request.method == 'POST':
        user_name = request.form['user_name']
        user_email = request.form['user_email']

        user = dap_user(user_name, user_email)
        db.session.add(user)
        db.session.commit()

        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("user_name")), "success")
        return redirect(url_for('user_overview'))

    return render_template("new_user.html")#, form=new_user_form)


@app.route("/project/new", methods=["GET", "POST"])
def new_project():
    if request.method == 'POST':
        project_name = request.form['project_name']
        project_db = request.form['project_db']

        project = dap_project(project_name, project_db)
        db.session.add(project)
        db.session.commit()
        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("project_name")), "success")
        return redirect(url_for('home'))

    return render_template("new_project.html")


@app.route("/workpack/new", methods=["GET", "POST"])
def new_workpack():
    form = NewWorkpackForm()

    projects = dap_project.query.all()
    project_list = []
    for row in projects:
        id=row.uid
        name=row.project_name
        project_list.append((id, name))
    form.project_id.choices = project_list

    if request.method == 'POST':
        workpack_name = request.form['workpack_name']
        project_id = request.form['project_id']
        workpack_extent = request.form['workpack_extent']

        workpack = dap_workpack(workpack_name, project_id, workpack_extent)
        db.session.add(workpack)
        db.session.commit()

        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("workpack_name")), "success")
        return redirect(url_for('home'))

    return render_template("new_workpack.html", form=form)


@app.route("/workpack_user/new", methods=["GET", "POST"])
def new_workpackuser():
    form = NewWorkpackUserForm()

    workpack_list = []
    workpacks = users = dap_workpack.query.all()
    for row in workpacks:
        id=row.uid
        name=row.workpack_name
        workpack_list.append((id, name))
    form.workpack_id.choices = workpack_list

    users = dap_user.query.all()
    user_list = []
    for row in users:
        id=row.uid
        name=row.user_name
        user_list.append((id, name))
    form.user_id.choices = user_list

    roles = dap_role.query.all()
    role_list = []
    for row in roles:
        id=row.uid
        name=row.role_name
        role_list.append((id, name))

    form.role_id.choices = role_list

    if request.method == "POST":
        workpack_id = request.form['workpack_id']
        user_id = request.form['user_id']
        role_id = request.form['role_id']

        workpack_user_role = dap_workpack_user_role(workpack_id, user_id, role_id)
        db.session.add(workpack_user_role)
        db.session.commit()

        # redirect to some page
        flash("Item has been successfully submitted", "success")
        return redirect(url_for('home'))

    return render_template("new_workpackuser.html", form = form)


@app.route('/map')
def map_func():
	return render_template('map_drawextent.html')

@app.route("/workpack/<int:index>")
def workpack_view(index):
    try:
        workpack = vdap_workpack_project.query.filter_by(workpack_id = index).first()
        workpack_details = vdap_workpack_detais.query.filter_by(workpack_id = index).all()

        wkp_headings = ("User Name", "User Email", "Role")
        wkp_data = []
        for row in workpack_details:
            wkp_data.append(
                            (row.user_name,
                            row.user_email,
                            row.role_name)
                            )

        # create the map
        coords = workpack.workpack_extent
        lat = float(coords.split(",")[0])
        lon = float(coords.split(",")[1])
        coords_formatted = (lat,lon
                            )
        coord_dict = {"lat": lat,
                      "lon": lon
                      }
        print (coord_dict)

        return render_template("workpack.html",
                               index=index,
                               workpack=workpack,
                               workpack_details=workpack_details,
                               headings=wkp_headings,
                               data=wkp_data,
                               coords=coord_dict
        )
    except IndexError:
        abort(404)


@app.route('/user/overview')
def user_overview():

    users = dap_user.query.all()
    print (users)

    user_headings = ("User_Name", "User_Email")
    user_data = []
    
    for row in users:
        user_data.append((row.user_name,
                        row.user_email))
                        
    return render_template('user_overview.html',
                            headings=user_headings,
                            data=user_data,
                            users= users)


@app.route('/user/<index>')
def user(index):
    return render_template('user.html')


@app.route('/map/folium')
def map_folium():
    return render_template("map_folium.html")


@app.route('/map/esrimap')
def map_esrimap():
    return render_template("esri_map.html")


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    app.run(debug=True)