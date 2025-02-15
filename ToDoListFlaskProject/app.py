
from datetime import datetime
from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), unique=False,nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_completed = db.Column(db.DateTime)
    is_deleted = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return '<Task %r>' % self.id
    
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding the task.'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()  # fetch all tasks in descending order by creation date
        return render_template('index.html', tasks=tasks)


@app.route('/complete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    print("task_to_delete ",task_to_delete)
    task_to_delete.is_deleted = True
    task_to_delete.date_completed = datetime.utcnow()
    print("after")
    print("task_to_delete.is_deleted ",task_to_delete.is_deleted)
    print("task_to_delete.date_completed ",task_to_delete.date_completed)
    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the task.'
    
@app.route('/deletePermanent/<int:id>')
def deletePermanent(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the task permanently.'


@app.route('/update/<int:id>', methods=['POST','GET'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'POST':
        newContent = request.form['content']
        task_to_update.content = newContent
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error updating the task.'
    else:
        return render_template('update.html',task=task_to_update)


@app.route('/review/<int:id>', methods=['GET'])
def reviewTask(id):
    task_to_review = Todo.query.get_or_404(id)
    task_to_review.is_deleted = False
    task_to_review.date_completed = None  # reset the completion date to None when reviewing the task again
    print("task_to_review.date_completed",task_to_review.date_completed)
    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error updating the task.'

if __name__ == "__main__":
    app.run(debug=True)