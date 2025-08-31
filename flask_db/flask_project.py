from flask import Flask, request, render_template, redirect, url_for, session,flash
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)
app.secret_key = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(), nullable=False, unique=True)

    def __repr__(self):
        return f"<User {self.username}>"
    
@app.route("/")
def home():
    return render_template("base.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        username=request.form["username"]
        email=request.form["email"]
        n_user=User(username=username,email=email)
        try:
            db.session.add(n_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            flash("Email already exists!", "error")
            return render_template("register.html")

        return redirect(url_for("users"))
    return render_template("register.html")

@app.route("/users", methods=["GET","POST"])
def users():
    if "authenticated" not in session:
        if request.method == "POST":
            password = request.form.get("password")
            if password == "admin123":
                session["authenticated"] = True
                return redirect(url_for("users"))
            else:
                flash("Wrong password!", "error")
                return render_template("password.html")
        return render_template("password.html")
    alluser=User.query.all()
    return render_template("users.html",users=alluser)

@app.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("home"))

@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if "authenticated" not in session:
        return redirect(url_for("users"))
    
    user = User.query.get_or_404(user_id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("Error deleting user!", "error")
    
    return redirect(url_for("users"))


if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)