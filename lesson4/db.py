import json


USERS_FILE_PATH = 'users.json'


def users_all(active: bool):
    with open(USERS_FILE_PATH, mode='r', encoding='utf-8') as f:
        users = json.load(f)
    if active:
        return [u for u in users if u.get('active', False)]
    return users


def save_users(users):
    with open(USERS_FILE_PATH, mode='w', encoding='utf-8') as f:
        json.dump(users, f, indent=4, ensure_ascii=False)


def add_user(user_data):
    users = users_all(False)
    user_dict = user_data.dict()
    user_dict.pop('action', None)
    users.append(user_dict)
    save_users(users)


def update_user(user_id, updates):
    users = users_all(False)
    for u in users:
        if u['id'] == user_id:
            u.update(updates)
            break
    save_users(users)


def delete_param(user_id, 
                 ):
    users = users_all(False)
    for u in users:
        if u['id'] == user_id:
            if param in u:
                del u[param]
            break
    save_users(users)