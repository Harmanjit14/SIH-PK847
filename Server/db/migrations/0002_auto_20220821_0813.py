# Generated by Django 3.2.15 on 2022-08-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester_subject_registration',
            name='degree',
            field=models.CharField(choices=[('17', 'B.E/B.Tech in Production Engineering'), ('7', 'B.E/B.Tech in Information Technology'), ('30', 'B.E/B.Tech in Marine Engineering'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('0', 'B.E/B.Tech in Computer Science Engineering'), ('15', 'B.E/B.Tech in Mining Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('16', 'B.E/B.Tech in Power Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering')], default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(choices=[('17', 'B.E/B.Tech in Production Engineering'), ('7', 'B.E/B.Tech in Information Technology'), ('30', 'B.E/B.Tech in Marine Engineering'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('0', 'B.E/B.Tech in Computer Science Engineering'), ('15', 'B.E/B.Tech in Mining Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('16', 'B.E/B.Tech in Power Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering')], default='0', max_length=255),
        ),
    ]
