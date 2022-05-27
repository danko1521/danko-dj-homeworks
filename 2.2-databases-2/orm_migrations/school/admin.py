from django.contrib import admin

from .models import Student, Teacher, StudentPosition


class ClassroomPositioninline(admin.TabularInline):
    model = StudentPosition


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['group']
    # list_editable = ['group']
    list_per_page = 10
    search_fields = ['name']
    filter_horizontal = ['teacher']


#
#
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
