from django.urls import path
from .controllers import users, students, classes, courses

urlpatterns = [
  # users
  path('insert_user', users.insert_user),
  path('get_users', users.get_users),
  path('search_user', users.search_user),
  path('remove_user', users.remove_user),
  path('check_user', users.check_user),

  # students
  path('insert_student', students.insert_student),
  path('remove_student', students.remove_student),
  path('get_all_students', students.get_all_students),
  path('search_student', students.search_student),
  path('get_students_count', students.get_students_count),
  path('check_duplicated_student_id', students.check_duplicated_student_id),

  # classes
  path('get_classes', classes.get_classes),
  path('search_class', classes.search_class),
  path('remove_class', classes.remove_class),
  path('insert_class_student_relation', classes.insert_class_student_relation),
  path('clear_class_student_relation', classes.clear_class_student_relation),
  path('insert_class', classes.insert_class),
  path('get_classes_student_relation', classes.get_classes_student_relation),
  path('remove_class_student_relation', classes.remove_class_student_relation),
  path('get_classes_for_selection', classes.get_classes_for_selection),

  # courses
  path("get_courses", courses.get_courses),
  path("search_courses", courses.search_courses),
  path("remove_course", courses.remove_course),
  path("insert_course", courses.insert_course)
]