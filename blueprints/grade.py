from flask import Blueprint, render_template

blue = Blueprint('grade', __name__, static_folder='static', template_folder='templates')


@blue.route('/<schedule_id>')
def grade(schedule_id: str) -> str:
    return render_template('grade.html', schedule_id=schedule_id)
