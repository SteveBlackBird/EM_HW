# Import Admin Class

from users import Admin, Privileges

new_user = Admin('sergey', 'ivanov', 23, 'california')
new_user.show_user_name()
new_user.privileges.show_privileges()