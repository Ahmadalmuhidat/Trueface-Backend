from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..utils.database import Database

@csrf_exempt
def get_classes(request):
  if request.method == "GET":
    try:
      query = '''
        SELECT
          Classes.*,
          Courses.Title
        FROM
          Classes
        LEFT JOIN
          Courses
        ON
          Courses.ID = Classes.Course
      '''
      data = Database.execute_get_query(query)
      return JsonResponse({
        "status_code": 200,
        "data": data
      })
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def search_class(request):
  if request.method == "GET":
    try:
        class_id = request.GET.get('class_id')
        data = [class_id]
        query = '''
          SELECT
            Classes.*,
            Courses.Title
          FROM
            Classes
          LEFT JOIN
            Courses
          ON
            Courses.ID = Classes.Course
          WHERE
            Classes.ID = %s
        '''
        data = Database.execute_get_query(query, data)
        return JsonResponse({
          "status_code": 200,
          "data": data
        })
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def remove_class(request):
  if request.method == "POST":
    try:
      
      class_id = request.POST.get('class_id')
      query = '''
        DELETE FROM
          Classes
        WHERE
          ID = %s
      '''
      if Database.execute_post_query(query, [class_id]):
        query = '''
          DELETE FROM
            ClassStudentRelation
          WHERE
            Class = %s
        '''
        Database.execute_post_query(query, [class_id])
      return JsonResponse({
        "status_code": 200,
        "data": True
      })
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def insert_class_student_relation(request):
  if request.method == "POST":
    try:
      print(request.POST.get('relation_id'))
      data = (
        request.POST.get('relation_id'),
        request.POST.get('student_id'),
        request.POST.get('class_id'),
        request.POST.get('day')
      )
      query = '''
        INSERT INTO
          ClassStudentRelation
          (
            ID,
            Student,
            Class,
            Day
          )
        VALUES
        (
          %s, 
          %s,
          %s,
          %s
        )
      '''
      Database.execute_post_query(query, data)
      return JsonResponse({"status_code": 200,"data": True})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def clear_class_student_relation(request):
  if request.method == "POST":
    try:
      student_id = request.POST.get('student_id')
      query = '''
        DELETE FROM
          ClassStudentRelation
        WHERE
          Student = %s
      '''
      Database.execute_post_query(query, [student_id])
      return JsonResponse({"status_code": 200, "data": True})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def insert_class(request):
  if request.method == "POST":
    try:
      data = (
        request.POST.get('class_id'),
        request.POST.get('subject'),
        request.POST.get('catalog_nbr'),
        request.POST.get('academic_career'),
        request.POST.get('course'),
        request.POST.get('offering_nbr'),
        request.POST.get('start_time'),
        request.POST.get('end_time'),
        request.POST.get('section'),
        request.POST.get('component'),
        request.POST.get('campus'),
        request.POST.get('instructor_id'),
        request.POST.get('instructor_type'),
      )
      query = '''
        INSERT INTO
        Classes
        (
          ID,
          SubjectArea,
          CatalogNbr,
          AcademicCareer,
          Course,
          OfferingNbr,
          StartTime,
          EndTime,
          Section,
          Component,
          Campus,
          Instructor,
          InstructorType
        )
        VALUES
        (
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s,
          %s
        )
      '''
      Database.execute_post_query(query, data)
      return JsonResponse({"status_code": 200, "data": True})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def get_classes_student_relation(request):
  if request.method == "GET":
    try:
      student_id = request.GET.get('student_id')
      data = [student_id]
      query = '''
        SELECT
          ClassStudentRelation.ID AS Relation,
          Classes.ID AS Class,
          Classes.SubjectArea,
          Classes.StartTime,
          Classes.EndTime,
          ClassStudentRelation.Day
        FROM
          Classes
        JOIN
          ClassStudentRelation
        ON
          Classes.ID = ClassStudentRelation.Class
        WHERE
          ClassStudentRelation.Student = %s
      '''
      data = Database.execute_get_query(query, data)
      return JsonResponse({"status_code": 200,"data": data})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def remove_class_student_relation(request):
  if request.method == "POST":
    try:
      relation_id = request.POST.get('relation_id')
      print(relation_id)
      data = [relation_id]
      query = '''
        DELETE FROM
          ClassStudentRelation
        WHERE
          ID = %s
      '''
      Database.execute_post_query(query, data)
      return JsonResponse({"status_code": 200, "data": True})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)

@csrf_exempt
def get_classes_for_selection(request):
  if request.method == "GET":
    try:
      query = '''
        SELECT
          ID,
          SubjectArea,
          StartTime,
          EndTime
        FROM
          Classes
      '''
      data = Database.execute_get_query(query)
      return JsonResponse({"status_code": 200,"data": data})
    except Exception as e:
      return JsonResponse({"error": str(e)}, status=500)
  return JsonResponse({
    "error": "Method not allowed"
  }, status=405)