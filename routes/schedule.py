from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, current_user, login_user

from model import schedule_dao

blue = Blueprint('schedule', __name__, static_folder='static', template_folder='templates')


@blue.route('/schedule')
def schedule():
    schedules = []
    for row in schedule_dao.find_all():
        schedules.append({
            'id': row.id,
            'name': row.name
        })
    return render_template('schedules.html', schedules=schedules, titulo='Grades')


@blue.route('/my_schedule', methods=['POST'])
@login_required
def my_schedule():
    if request.method == 'POST':
        id = request.form.get('id_schedule')
        current_user.schedule = schedule_dao.find_by_id(id)
        current_user.save()
        return redirect('/my_schedule')


@blue.route('/schedule/<id_schedule>')
def grade(id_schedule: str):
    returned_schedule = schedule_dao.find_by_id(id_schedule)
    if returned_schedule is None:
        return redirect('/')
    return render_template('schedule.html', schedule=returned_schedule, title=returned_schedule.name)


@blue.route('/api/<id_schedule>')
def api_grade(id_schedule: str):
    id_schedule = int(id_schedule)
    returned_schedule = schedule_dao.find_one({'id': id_schedule})
    if returned_schedule is None:
        return redirect('/')
    return returned_schedule.__dict__
