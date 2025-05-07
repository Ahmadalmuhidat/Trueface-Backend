from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from ..utils.database import Database
from ..helper import json_web_token

@csrf_exempt
def insert_user(request):
  if request.method == "POST":
    data = (
      request.POST.get("user_id"),
      request.POST.get("name"),
      request.POST.get("email"),
      request.POST.get("password"),
      request.POST.get("role")
    )
    query = '''
      INSERT INTO
        Users
      VALUES
      (
        %s,
        %s,
        %s,
        %s,
        %s
      )
    '''
    return JsonResponse({
      "status_code": 200,
      "data": Database.execute_post_query(query, data)
    })
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def get_users(request):
  if request.method == "GET":
    query = '''
      SELECT
        ID,
        Name,
        Email,
        Role
      FROM
        Users
    '''
    return JsonResponse({
      "status_code": 200,
      "data": Database.execute_get_query(query)
    })
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def search_user(request):
  if request.method == "GET":
    user_id = request.GET.get("user_id")
    data = [user_id]
    query = '''
      SELECT
        ID,
        Name,
        Email,
        Role
      FROM
        Users
      WHERE
        ID = %s
    '''
    return JsonResponse({
      "status_code": 200,
      "data": Database.execute_get_query(query, data)
    })
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def remove_user(request):
  if request.method == "POST":
    user_id = request.POST.get("user_id")
    data = [user_id]

    delete_user_query = 'DELETE FROM Users WHERE ID = %s'
    remove = Database.execute_post_query(delete_user_query, data)

    if remove:
      delete_classes_query = '''
        DELETE FROM
          Classes
        WHERE
          Instructor = %s
      '''
      Database.execute_post_query(delete_classes_query, data)
      return JsonResponse({
        "status_code": 200,
        "data": True
      })
    else:
      return JsonResponse({
        "status_code": 500,
        "error": "Something went wrong while deleting the student"
      })
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def check_user(request):
  if request.method == "GET":
    email = request.GET.get("email")
    password = request.GET.get("password")
    data = (email,)
    query = '''
      SELECT
        ID,
        Password,
        Role
      FROM
        Users
      WHERE
        Email = %s
    '''
    user = Database.execute_get_query(query, data)

    if len(user) == 1:
      if str(user[0]['Password']) == str(password):
        payload = {
          'user_id': user[0]['ID'],
          'role': user[0]['Role'],
          'exp': datetime.utcnow() + timedelta(hours=24)
        }
        return JsonResponse({
          "status_code": 200,
          "data": json_web_token.create_token(payload)
        })
      else:
        return JsonResponse({
          "status_code": 500,
          "error": "Password incorrect"
        })
    else:
      return JsonResponse({
        "status_code": 500,
        "error": "User was not found"
      })
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)