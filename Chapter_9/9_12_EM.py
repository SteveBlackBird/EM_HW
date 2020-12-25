# Multiple modules
from admin import Admin, Privileges

new_admin = Admin('petr', 'zalskiy', 25, 'siktivkar')
new_admin.privileges.show_privileges()
new_admin.show_user_name()
