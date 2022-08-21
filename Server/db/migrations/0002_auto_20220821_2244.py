# Generated by Django 3.2.15 on 2022-08-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate_request',
            name='event_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='certificate_request',
            name='certificate_status',
            field=models.CharField(choices=[('0', 'Semester Certificate'), ('1', 'Migration Certificate'), ('2', 'Domicile Certificate'), ('3', 'Affadavit'), ('4', 'Character Certificate'), ('5', 'Event')], default='1', max_length=255),
        ),
        migrations.AlterField(
            model_name='semester_subject_registration',
            name='degree',
            field=models.CharField(choices=[('7', 'B.E/B.Tech in Information Technology'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('16', 'B.E/B.Tech in Power Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('15', 'B.E/B.Tech in Mining Engineering'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('17', 'B.E/B.Tech in Production Engineering'), ('30', 'B.E/B.Tech in Marine Engineering'), ('0', 'B.E/B.Tech in Computer Science Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering')], default='0', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='degree',
            field=models.CharField(choices=[('7', 'B.E/B.Tech in Information Technology'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('16', 'B.E/B.Tech in Power Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('15', 'B.E/B.Tech in Mining Engineering'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('17', 'B.E/B.Tech in Production Engineering'), ('30', 'B.E/B.Tech in Marine Engineering'), ('0', 'B.E/B.Tech in Computer Science Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering')], default='0', max_length=255),
        ),
    ]
