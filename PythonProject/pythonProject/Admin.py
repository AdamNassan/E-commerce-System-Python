from datetime import datetime
class Admin:
    def __init__(self, user_id, user_name, user_date_of_birth, role, active):
        self.user_id = user_id
        self.user_name = user_name
        self.user_date_of_birth = datetime.strptime(user_date_of_birth, "%d/%m/%Y").date()
        self.role = role
        self.active = bool(int(active))

    def __str__(self):
        return f"User ID: {self.user_id}\nUser Name: {self.user_name}\nDate of Birth: {self.user_date_of_birth}\nRole: {self.role}\nActive: {self.active}"
