from flask import Blueprint

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

users = [
    {
        'id': 1,
        'name': 'Sushant Pandey',
        'designation': 'Software Engineer'
    },
    {
        'id': 2,
        'name': 'Arjun  Pandey',
        'designation': 'Full Stack Engineer'
    },
    {
        'id': 3,
        'name': 'Pasoori Pandey',
        'designation': 'Software Engineer'
    },
]

@users_blueprint.route('/')
def get_users():
    return users


@users_blueprint.route('/<int:id>', methods=['GET'])
def get_user_by_id(id: int):
    user = next((user for user in users if user['id'] == id), None)
    
    return user if user else { 'message': 'User not found' }, 404