from django.db import models

# Create your models here.

class ExamQuestionOptions(models.Model):
    content= models.TextField(unique=True)
    def __str__(self):
        return self.content
    
    

class ExamQuestion(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    SUBJECT_CHOICES=(
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('math', 'Math'),
    )
    body= models.TextField(unique=True)
    answer= models.TextField(default=None)
    options= models.ManyToManyField(ExamQuestionOptions, related_name="options")
    correct_options = models.ManyToManyField(ExamQuestionOptions, related_name="correct_options")
    subject= models.CharField(max_length=25, choices=SUBJECT_CHOICES, default='physics')
    difficulty_level= models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='medium')

    def __str__(self):
        return self.body
    
class Exam(models.Model):
    
    name= models.CharField(max_length=25)
    year= models.IntegerField()
    questions = models.ManyToManyField(ExamQuestion, related_name='Exams', blank=True, through="ExamQuestionIntermidiate")
    def __str__(self):
        return f"{self.name}-{self.year}"
    class Meta:
        ordering = ['name', 'year']


class ExamQuestionIntermidiate(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestion, on_delete=models.CASCADE)
    question_order = models.PositiveIntegerField()

    class Meta:
        ordering = ["question_order"]

    def save(self, *args, **kwargs):
        if not self.pk:
            # Set the order based on the number of existing questions for the exercise
            self.question_order = self.exam.questions.count() + 1
        super().save(*args, **kwargs)



class BookQuestionOption(models.Model):
    content= models.TextField(unique=True)
    def __str__(self):
        return self.content   

class BookQuestion(models.Model):
    DIFFICULTY_CHOICES = (
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    )
    SUBJECT_CHOICES=(
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('math', 'Math'),
    )
    
    body= models.TextField(unique=True)
    answer= models.TextField(default=None)
    options= models.ManyToManyField(BookQuestionOption, related_name="options")
    correct_options = models.ManyToManyField(BookQuestionOption, related_name="correct_options")
    difficulty_level= models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='medium')
    subject= models.CharField(max_length=25, choices=SUBJECT_CHOICES, default='math')

    def __str__(self):
        return self.body
    


class Book(models.Model):
    name= models.CharField(max_length=250)
    SUBJECT_CHOICES=(
        ('physics', 'Physics'),
        ('chemistry', 'Chemistry'),
        ('math', 'Math'),
    )
    subject= models.CharField(max_length=100, choices=SUBJECT_CHOICES)
    image= models.ImageField(upload_to="images/")

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name= models.CharField(max_length=250)
    book= models.ForeignKey(Book, related_name="chapters", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Exercise(models.Model):
    name= models.CharField(max_length=250)
    questions= models.ManyToManyField(BookQuestion, related_name="Exercises", blank=True, through="ExerciseQuestionIntermidiate")
    chapter= models.ForeignKey(Chapter, related_name="exercises", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExerciseQuestionIntermidiate(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    question = models.ForeignKey(BookQuestion, on_delete=models.CASCADE)
    question_order = models.PositiveIntegerField()

    class Meta:
        ordering = ["question_order"]

    def save(self, *args, **kwargs):
        if not self.pk:
            # Set the order based on the number of existing questions for the exercise
            self.question_order = self.exercise.questions.count() + 1
        super().save(*args, **kwargs)


class UserSubmittedBookAnswer(models.Model):
    answer = models.TextField()
    book = models.CharField(max_length=250)
    chapter = models.CharField(max_length=250)
    exercise = models.CharField(max_length=250)
    no= models.IntegerField()

class BookQuestionFeedback(models.Model):
    feedback = models.TextField()
    book = models.CharField(max_length=250)
    chapter = models.CharField(max_length=250)
    exercise = models.CharField(max_length=250)
    no= models.IntegerField()

    



    


    











