# Generated by Django 3.2.15 on 2022-08-17 21:50

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_Request',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('verified', models.BooleanField(default=False)),
                ('delivery_status', models.CharField(choices=[('0', 'Accepted'), ('1', 'Transit'), ('2', 'Delivered'), ('3', 'Failed Attempt'), ('4', 'Expired'), ('5', 'Waiting')], default='5', max_length=255)),
                ('certificate_status', models.CharField(choices=[('0', 'Semester Certificate'), ('1', 'Migration Certificate'), ('2', 'Domicile Certificate'), ('3', 'Affadavit'), ('4', 'Character Certificate')], default='1', max_length=255)),
                ('payment_amount', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('delivery_done', models.BooleanField(default=False)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('added', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('mail', models.EmailField(max_length=255)),
                ('logo', models.URLField(default='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Fdeflogo.png?alt=media&token=d99783e2-c80c-4e4f-9300-f85f6aacac50')),
                ('signature', models.URLField(default='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Fdefsignature.png?alt=media&token=a53e5c47-51e3-46cd-b415-4ca6e053e969')),
                ('contact', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.institute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('roll', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('dob', models.CharField(blank=True, max_length=10)),
                ('graduating_year', models.IntegerField()),
                ('degree', models.CharField(choices=[('0', 'B.E/B.Tech in Computer Science Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering'), ('17', 'B.E/B.Tech in Production Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('30', 'B.E/B.Tech in Marine Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('16', 'B.E/B.Tech in Power Engineering'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('7', 'B.E/B.Tech in Information Technology'), ('15', 'B.E/B.Tech in Mining Engineering'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering')], default='0', max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('wallet', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('batch', models.CharField(blank=True, max_length=255)),
                ('father_name', models.CharField(blank=True, max_length=255)),
                ('mother_name', models.CharField(blank=True, max_length=255)),
                ('current_semester', models.IntegerField(default=1, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.institute')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Semester_Subject_Registration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('credits', models.FloatField(default=0)),
                ('subject', models.CharField(max_length=255)),
                ('subject_code', models.CharField(max_length=255)),
                ('semester', models.IntegerField()),
                ('graduating_year', models.IntegerField()),
                ('degree', models.CharField(choices=[('0', 'B.E/B.Tech in Computer Science Engineering'), ('33', 'B.E/B.Tech in Petrochemical Engineering'), ('36', 'B.E / B.Tech in Nuclear Engineering'), ('17', 'B.E/B.Tech in Production Engineering'), ('21', 'B.E/B.Tech in Food Processing and Technology'), ('12', 'B.E/B.Tech in Aeronautical Engineering'), ('30', 'B.E/B.Tech in Marine Engineering'), ('32', 'B.E/B.Tech in Geoinformatics'), ('22', 'B.E/B.Tech in Agricultural Engineering'), ('27', 'B.E/B.Tech in Motorsport Engineering'), ('28', 'B.E/B.Tech in Metallurgy Engineering'), ('9', 'B.E/B.Tech in Electronics Engineering'), ('25', 'B.E/B.Tech in Agricultural Information Technology'), ('11', 'B.E/B.Tech in Petroleum Engineering'), ('24', 'B.E/B.Tech in Dairy Technology and Engineering'), ('18', 'B.E/B.Tech in Biotechnology Engineering'), ('4', 'B.E/B.Tech in Electrical and Electronics Engineering'), ('10', 'B.E/B.Tech in Electronics and Telecommunication Engineering'), ('26', 'B.E/B.Tech in Infrastructure Engineering'), ('3', 'B.E/B.Tech in Electrical Engineering'), ('14', 'B.E/B.Tech in Automobile Engineering'), ('20', 'B.E/B.Tech in Plastics Engineering'), ('6', 'B.E/B.Tech in Chemical Engineering'), ('8', 'B.E/B.Tech in Instrumentation and Control Engineering'), ('5', 'B.E/B.Tech in Civil Engineering'), ('19', 'B.E/B.Tech in Genetic Engineering'), ('23', 'B.E/B.Tech in Environmental Engineering'), ('1', 'B.E/B.Tech in Mechanical Engineering'), ('31', 'B.E/B.Tech in Naval Architecture'), ('16', 'B.E/B.Tech in Power Engineering'), ('13', 'B.E/B.Tech in Aerospace Engineering'), ('29', 'B.E/B.Tech in Textile Engineering'), ('34', 'B.E/B.Tech in Polymer Engineering'), ('7', 'B.E/B.Tech in Information Technology'), ('15', 'B.E/B.Tech in Mining Engineering'), ('35', 'B.E/B.Tech in Geotechnical Engineering'), ('2', 'B.E/B.Tech in Electronics and Communication Engineering')], default='0', max_length=255)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.institute')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Receipt',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('paymentid', models.CharField(max_length=255)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.certificate_request')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.student')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('location', models.CharField(max_length=255, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InstituteEvent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('host_name', models.CharField(blank=True, max_length=255)),
                ('host_contact', models.CharField(blank=True, max_length=255)),
                ('event_overview', models.CharField(default='No Information', max_length=255)),
                ('event_description', models.TextField(default='No Information')),
                ('event_ended', models.BooleanField(default=False)),
                ('start_date', models.CharField(max_length=255, null=True)),
                ('end_date', models.CharField(max_length=255, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.institute')),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('winner', models.BooleanField(null=True)),
                ('prize', models.CharField(blank=True, choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Participant'), ('5', 'Special Prize')], default='4', max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.instituteevent')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.student')),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.manager')),
            ],
        ),
        migrations.AddField(
            model_name='certificate_request',
            name='delivery_man',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.delivery'),
        ),
        migrations.AddField(
            model_name='certificate_request',
            name='delivery_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.manager'),
        ),
        migrations.AddField(
            model_name='certificate_request',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.student'),
        ),
        migrations.CreateModel(
            name='Academic_Record_File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('url', models.URLField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Academic_Record',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('subject_code', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=2)),
                ('marks', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('credits', models.FloatField(default=0)),
                ('graduating_year', models.IntegerField()),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.institute')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.student')),
            ],
        ),
    ]
