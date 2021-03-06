# Generated by Django 2.0.7 on 2018-07-29 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizMania', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionString', models.CharField(max_length=2000)),
                ('questionType', models.CharField(max_length=20)),
                ('questionImage', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('option1', models.CharField(max_length=20, null=True)),
                ('option2', models.CharField(max_length=20, null=True)),
                ('option3', models.CharField(max_length=20, null=True)),
                ('option4', models.CharField(max_length=20, null=True)),
                ('answer', models.CharField(max_length=20)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruleDisplay', models.BooleanField(default=True)),
                ('completed', models.BooleanField(default=False)),
                ('answeredQuestions', models.CharField(max_length=2000)),
                ('points', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizMania.Users')),
            ],
        ),
    ]
