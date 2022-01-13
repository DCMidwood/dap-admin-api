import sqlite3

import folium
from flask import Flask, render_template, request, redirect, url_for, g, flash, abort
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import (
    DataRequired
)



from model import (get_db, get_workpacks, get_specific_workpack,
                    get_specific_workpack_details, get_projects,
                    get_project_list)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "secretkey"


class NewProjectForm(FlaskForm):
    name = StringField("ProjectName")
    database = StringField("database")
    submit = SubmitField("Submit")


class NewWorkpackForm(FlaskForm):

    workpack_name = StringField("workpackname")
    project_id = SelectField('projectid', choices=[])
    workpack_extent = StringField("workpack_extent")
    submit = SubmitField("Submit")


class NewUserForm(FlaskForm):
    user_name = StringField("User Name")
    user_email = StringField("Email")
    submit = SubmitField("Submit")


class NewWorkpackUserForm(FlaskForm):
    workpackid = StringField("Workpack")
    userid = StringField("User")
    roleid = StringField("Role")
    submit = SubmitField("Submit")


@app.route("/")
def home():
    workpacks = get_workpacks()

    return render_template("home.html",
                           workpacks=workpacks)


@app.route("/workpack/<int:index>")
def workpack_view(index):
    try:
        workpack = get_specific_workpack(index)
        workpack_details = get_specific_workpack_details(index)

        wkp_headings = ("User Name", "User Email", "Role")
        wkp_data = []
        for row in workpack_details:
            wkp_data.append((row.get('user'),
                            row.get('user_email'),
                            row.get('role'))
                            )

        #wkp_data = ( #workpack_details.user_email, workpack_details.role)

        # create the map
        coords = workpack.get("extent")
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

@app.route("/user/new", methods=["GET", "POST"])
def new_user():
    new_user_form = NewUserForm()
    if request.method == "POST":
        conn = get_db()
        c = conn.cursor()

        c.execute("""INSERT INTO dap_user
                        (user_name,user_email)
                        VALUES(?,?)""",
                  (
                      new_user_form.user_name.data,
                      new_user_form.user_email.data
                  )
                  )
        conn.commit()
        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("user_name")), "success")

    return render_template("new_user.html", form=new_user_form)


@app.route("/project/new", methods=["GET", "POST"])
def new_project():
    new_project_form = NewProjectForm()
    if request.method == "POST":

        conn = get_db()
        c = conn.cursor()

        c.execute("""INSERT INTO dap_project
                        (project_name,project_db)
                        VALUES(?,?)""",
                  (
                      new_project_form.name.data,
                      new_project_form.database.data
                  )
                  )
        conn.commit()
        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("name")), "success")

    return render_template("new_project.html", form=new_project_form)


@app.route("/workpack/new", methods=["GET", "POST"])
def new_workpack():
    form = NewWorkpackForm()
    project_list = get_project_list()
    form.project_id.choices = project_list
    if request.method == "POST":
        #print("Form Data:")
        #print("Workpack Name: {}, Project Id: {}".format(
        #    request.form.get("name"),
        #    request.form.get("project_id")
        #))
        conn = get_db()
        c = conn.cursor()

        c.execute("""INSERT INTO dap_workpack
                        (workpack_name, project_id, workpack_extent)
                        VALUES(?,?,?)""",
                  (
                      form.workpack_name.data,
                      form.project_id.data,
                      form.workpack_extent.data,
                  )
                  )
        conn.commit()


        # redirect to some page
        flash("Item {} has been successfully submitted".format(request.form.get("workpack_name")), "success")

    return render_template("new_workpack.html", form=form)


@app.route("/workpack/new_user", methods=["GET", "POST"])
def new_workpackuser():
    form = NewWorkpackUserForm()
    if request.method == "POST":
        conn = get_db()
        c = conn.cursor()
        c.execute("""INSERT INTO workpack_user_role
                        (workpack_id, user_id, role_id)
                        VALUES(?,?,?)""",
                  (
                      form.workpackid.data,
                      form.userid.data,
                      form.roleid.data,
                  )
                  )
        conn.commit()

        # redirect to some page
        flash("Item has been successfully submitted", "success")

    return render_template("new_workpackuser.html", form=form)


@app.route('/map')
def map_func():
	return render_template('map_drawextent.html')


@app.route('/user/<index>')
def user(index):
    return render_template('user.html')


@app.route('/map/folim')
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