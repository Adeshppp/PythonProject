
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


# setup application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db= SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
   # everytime we create a new element it will return a task and its id
    def __repr__(self):
        return '<Task %r>' % self.id

# create a index route
@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()  # fetch all tasks in descending order by creation date
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your task'
    
@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id);
    if request.method == "POST":
        task.content = request.form['content']
        
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'  # if there's an error in updating, return this message
    else:
        return render_template('update.html', task=task)
    
if __name__ == "__main__":
    app.run(debug=True)

# In this code, we have created a simple Flask application. 
# The app is initialized with the Flask class, 
# and then we define a route ('/') to respond with 'Hello, World!'. 
# Finally, we run the Flask application in debug mode, allowing it to automatically reload changes to the code and display the changes in real-time.