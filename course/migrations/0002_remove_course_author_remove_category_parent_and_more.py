# Generated by Django 5.1.4 on 2025-02-05 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='author',
        ),
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='course',
            name='category',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursevideo',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursesection',
            name='course',
        ),
        migrations.RemoveField(
            model_name='userproductreview',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursevideo',
            name='section',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userproductreview',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseSection',
        ),
        migrations.DeleteModel(
            name='CourseVideo',
        ),
        migrations.DeleteModel(
            name='SearchHistory',
        ),
        migrations.DeleteModel(
            name='UserProductReview',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
