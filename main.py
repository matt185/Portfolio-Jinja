from flask import Flask,redirect,url_for,render_template,request
from flask_bootstrap import Bootstrap
from projectsList import all_projects 
from logosList import logo_list
from datetime import date
app=Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    home_project = [project for project in all_projects if project["home"] ==True]  
    year=date.today().year
    print(year)
    return render_template('index.html',  projects=home_project, year=year)

@app.route('/skills')
def skills():
    languages = [ele for ele in logo_list if ele["type"] == "language"]
    backend_skills=[ele for ele in logo_list if ele["type"] == "backend"]
    frontend_skills=[ele for ele in logo_list if ele["type"] =="frontend"]
    other_skills=[ele for ele in logo_list if ele["type"]=="other" or ele["type"]=="testing"]
    
    return render_template('skills.html',languages=languages, backend_skills=backend_skills,frontend_skills=frontend_skills, other_skills=other_skills)
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)