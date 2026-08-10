import psycopg2
from psycopg_connection import PgManager

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
    )


# def format_user(user_record):
#     return {
#         "id": user_record[0],
#         "full_name": user_record[1],
#         "email": user_record[2],
#         "password": user_record[3],
#     }

# # (...)

# results = cursor.fetchall()
# formatted_results = [format_user(result) for result in results]
# print(formatted_results)