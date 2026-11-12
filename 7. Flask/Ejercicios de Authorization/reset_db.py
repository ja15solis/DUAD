from db import engine, metadata_obj
from user_repository import user_repository

metadata_obj.drop_all(engine)
metadata_obj.create_all(engine, checkfirst=True)
user_repository.create(username="Javier", password="admin_password", admin_user=True)

print("""Database reset and initial admin user created.
Username: Javier, Password: admin_password, Admin: True""")