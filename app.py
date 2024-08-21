from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [
    {
        'id': 1,
        'title': 'Project 1',
        'category': 'Deep Learning',
        'description': 'Master\'s thesis'
    },
    {
        'id': 2,
        'title': 'Project 2',
        'category': 'Engineering',
        'description': 'Work Project'
    },
    {
        'id': 3,
        'title': 'Project 3',
        'category': 'Data Analysis',
        'description': 'Personal Project'
    },
    {
        'id': 4,
        'title': 'Project 4',
        'category': 'Image Processing',
        'description': 'Course Project'
    },
]


@app.route("/")
def hello():
  return render_template('home.html', projects=PROJECTS)


@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
