# Generated by Django 4.2.5 on 2024-01-25 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("physics", "Physics"),
                            ("chemistry", "Chemistry"),
                            ("math", "Math"),
                        ],
                        max_length=100,
                    ),
                ),
                ("image", models.ImageField(upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="BookQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(unique=True)),
                ("answer", models.TextField(default=None)),
                (
                    "difficulty_level",
                    models.CharField(
                        choices=[
                            ("easy", "Easy"),
                            ("medium", "Medium"),
                            ("hard", "Hard"),
                        ],
                        default="medium",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookQuestionOption",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Chapter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chapters",
                        to="main.book",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                ("year", models.IntegerField()),
            ],
            options={
                "ordering": ["name", "year"],
            },
        ),
        migrations.CreateModel(
            name="ExamQuestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("body", models.TextField(unique=True)),
                ("answer", models.TextField(default=None)),
                (
                    "subject",
                    models.CharField(
                        choices=[
                            ("physics", "Physics"),
                            ("chemistry", "Chemistry"),
                            ("math", "Math"),
                        ],
                        default="physics",
                        max_length=25,
                    ),
                ),
                (
                    "difficulty_level",
                    models.CharField(
                        choices=[
                            ("easy", "Easy"),
                            ("medium", "Medium"),
                            ("hard", "Hard"),
                        ],
                        default="medium",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExamQuestionOptions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exercises",
                        to="main.chapter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExerciseQuestionIntermidiate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_order", models.PositiveIntegerField()),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.exercise"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.bookquestion",
                    ),
                ),
            ],
            options={
                "ordering": ["question_order"],
            },
        ),
        migrations.AddField(
            model_name="exercise",
            name="questions",
            field=models.ManyToManyField(
                blank=True,
                related_name="Exercises",
                through="main.ExerciseQuestionIntermidiate",
                to="main.bookquestion",
            ),
        ),
        migrations.CreateModel(
            name="ExamQuestionIntermidiate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_order", models.PositiveIntegerField()),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.exam"
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.examquestion",
                    ),
                ),
            ],
            options={
                "ordering": ["question_order"],
            },
        ),
        migrations.AddField(
            model_name="examquestion",
            name="correct_options",
            field=models.ManyToManyField(
                related_name="correct_options", to="main.examquestionoptions"
            ),
        ),
        migrations.AddField(
            model_name="examquestion",
            name="options",
            field=models.ManyToManyField(
                related_name="options", to="main.examquestionoptions"
            ),
        ),
        migrations.AddField(
            model_name="exam",
            name="questions",
            field=models.ManyToManyField(
                blank=True,
                related_name="Exams",
                through="main.ExamQuestionIntermidiate",
                to="main.examquestion",
            ),
        ),
        migrations.AddField(
            model_name="bookquestion",
            name="correct_options",
            field=models.ManyToManyField(
                related_name="correct_options", to="main.bookquestionoption"
            ),
        ),
        migrations.AddField(
            model_name="bookquestion",
            name="options",
            field=models.ManyToManyField(
                related_name="options", to="main.bookquestionoption"
            ),
        ),
    ]
