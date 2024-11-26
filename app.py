from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (use a database in production)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append({'id': len(tasks) + 1, 'name': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
