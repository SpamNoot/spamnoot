def can_user_login(username, password, users_dict):

    if username in users_dict:
        if users_dict[username] == password:
            return True

    return False
