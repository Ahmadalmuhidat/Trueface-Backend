from django.db import connection

class Database:
  @staticmethod
  def execute_get_query(query, data=None):
    try:
      with connection.cursor() as cursor:
        cursor.execute(query, data)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
    except Exception as e:
      print("Database error:", str(e))
      return []

  @staticmethod
  def execute_post_query(query, data=None):
    try:
      with connection.cursor() as cursor:
        cursor.execute(query, data)
      return True
    except Exception as e:
      print("Database error (POST):", str(e))
      return False