from django.db import models

# Create your models here.
class Book(models.Model):
    BookName = models.CharField(max_length=256)
    PageVolume = models.IntegerField()
    inputdate = models.DateTimeField()
    Lent = models.DateTimeField()
    authName = models.CharField(max_length=256)

# class Boy(models.Model):
#     Name = models.CharField(max_length=256)
#     Age = models.IntegerField()
#     BirthDay = models.DateField()
#     SelfIntroduction = models.TextField()
#     email = models.EmailField()

# class School(models.Model):
#     SchoolName = models.CharField(max_length=256)
#     Address = models.CharField(max_length=256)
#     StudentNumber = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Notice(models.Model):
    title = models.CharField(max_length=100)
    likeCount = models.IntegerField()
    viewCount = models.IntegerField()
    content = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'제목 : {self.title}, 좋아요 수 : {self.likeCount}, 조회수 : {self.viewCount}'

# class Notice(models.Model):
#     clothesTee = models.IntegerField()
#     clothesPants = models.IntegerField()
#     clothesNit = models.IntegerField()


    # def __str__(self):
    #     return f'제목 : {self.clothesTee}, 거래자명 : {self.clothesPants}, 거래일 : {self.clothesNit}'

    # class Lent(models.Model):
    #     title = models.CharField(max_length=100)
    #     users = models.ManyToManyField(User)

class Students(models.Model):
    Name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    Department = models.CharField(max_length=256)
    content = models.TextField()

    user = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f'제목 : {self.name}, 이름 : {self.email}, 이메일 : {self.department}, 학과'


#     1. ** Student **:
#     - ** `name` **: 학생
#     이름
#     - ** `email` **: 이메일
#     - ** `department` **: 속한
#     학과(**`OneToOneField` ** to ** `Department` **)

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    Name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    department = models.CharField(max_length=256)
    content = models.TextField()

    Instructor = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    Students = models.ManyToManyField('Students', through='Enrollment')
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)
    def __str__(self):
        return f'제목 : {self.title}, 과목명 : {self.code}, 과목 : {self.instructor}, 강사 : {self.department}, 제공 : {self.student}, 수강'
# 2. ** Course **:
# - ** `title` **: 과목명
# - ** `code` **: 과목
# 코드
# - ** `instructor` **: 강사(**`ForeignKey` ** to ** `Instructor` **)
# - ** `department` **: 제공
# 학과(**`ForeignKey` ** to ** `Department` **)
# - ** `students` **: 수강
# 학생들(**`ManyToManyField` ** to ** `Student` **, **`through = 'Enrollment'
# ` **)
#
class Instructor(models.Model):
    Name = models.CharField(max_length=256)
    title = models.CharField(max_length=100)

    content = models.TextField()

    def __str__(self):
        return f'제목 : {self.name}, 강사 : {self.office}, 사무실'
# 3. ** Instructor **:
# - ** `name` **: 강사
# 이름
# - ** `office` **: 사무실
# 위치

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)
    content = models.TextField()

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Students = models.ManyToManyField('Students')
    def __str__(self):
        return f'제목 : {self.name}, 학과명 : {self.head}, 학과장'
# 4. ** Department **:
# - ** `name` **: 학과명
# - ** `head` **: 학과장
class Enrollment(models.Model):
    enrollment = models.CharField(max_length=100)
    enrollment_date = models.IntegerField()
    content = models.TextField()

    Students = models.ForeignKey('Students', on_delete=models.CASCADE)
    Course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'제목 : {self.enrollment}, : {self.students}, 학생 : {self.course}, 과목 : {self.enrollment_date}, 수강'

# 5. ** Enrollment **:
# - ** `student` **: 학생(**`ForeignKey` ** to ** `Student` **)
# - ** `course` **: 과목(**`ForeignKey` ** to ** `Course` **)
# - ** `enrollment_date` **: 수강
# 신청
# 날짜
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    du_date = models.IntegerField()
    content = models.TextField()

    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f'제목 : {self.title}, 과제명 : {self.course}, 과목 : {self.du_date}, 마감'



# 6. ** Assignment **:
# - ** `title` **: 과제명
# - ** `course` **: 해당
# 과목(**`ForeignKey` ** to ** `Course` **)
# - ** `due_date` **: 마감
# 날짜
class Submission(models.Model):
    assignment = models.CharField(max_length=100)
    students = models.CharField(max_length=256)
    submission = models.CharField(max_length=256)
    grade = models.CharField(max_length=256)
    content = models.TextField()

    Assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE)
    Students = models.ForeignKey('Students', on_delete=models.CASCADE)

    def __str__(self):
        return f'제목 : {self.assignment}, 과제 : {self.students}, 제출한 학생 : {self.submission}, 제출한 학생 : : {self.grade}, 평가'

# 7. ** Submission **:
# - ** `assignment` **: 과제(**`ForeignKey` ** to ** `Assignment` **)
# - ** `student` **: 제출한
# 학생(**`ForeignKey` ** to ** `Student` **)
# - ** `submission_date` **: 제출
# 날짜
# - ** `grade` **: 평가
# 점수