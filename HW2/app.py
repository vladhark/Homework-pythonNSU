from flask import Flask, jsonify, request, render_template
import read_data
import json

app = Flask(__name__)

data = read_data.DataTable()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/names')
def give_names():
    return jsonify(data.student_names)


@app.route('/<hw_name>/mean_score')
def give_mean_score(hw_name):
    if (hw_name == 'hw-01'):
        return str(data.mean_HW1())
    if (hw_name == 'hw-02'):
        return str(data.mean_HW2())
    return {'status': 'vse upalo', 'message': 'potomu chto plohoy zapros'}, 400


@app.route('/<hw_name>/<group_id>/mean_score')
def give_mean_score_group(hw_name, group_id):
    if (hw_name == 'hw-01'):
        return str(data.mean_HW1_group(int(group_id)))
    if (hw_name == 'hw-02'):
        return str(data.mean_HW2_group(int(group_id)))
    return {'status': 'vse upalo', 'message': 'potomu chto plohoy zapros'}, 400


@app.route('/mean_score')
def give_mean_score_args():
    hw_name = request.args.get('hw_name')
    group_id = request.args.get('group_id')
    if (hw_name == 'hw-01'):
        return str(data.mean_HW1_group(int(group_id)))
    if (hw_name == 'hw-02'):
        return str(data.mean_HW2_group(int(group_id)))
    return {'status': 'vse upalo', 'message': 'potomu chto plohoy zapros'}, 400


@app.route('/mark')
def give_mark():
    student_id = request.args.get('student_id')
    return str(data.return_mark(student_id))


@app.route('/course_table')
def return_table():
    hw_name = request.args.get('hw_name')
    group_id = request.args.get('group_id')
    if hw_name is None:
        return {'status': 'vse upalo', 'message': 'potomu chto plohoy zapros'}, 400
    if group_id is None:
        scores = [{'name': student, 'group': data.student_to_group[student], 'scores': data.student_mark(student)}
                  for student in data.student_names['names']]
    else:
        scores = [{'name': student, 'group': data.student_to_group[student], 'scores': data.student_mark(student)}
                  for student in data.groups[group_id]]
    return render_template("course_table.html", scores=scores, hw_name=hw_name)


@app.route('/about')
def about():
    return 'This is the about page'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'


app.run(host='0.0.0.0', port=1337)
