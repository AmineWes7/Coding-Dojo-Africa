@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
   

    if valid_login:
    
        session["user_id"] = user_id
        return redirect(url_for("success"))
    return render_template("index.html", error="Invalid login credentials")