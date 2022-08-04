from warnings import catch_warnings
import pandas as pd
from .models import Academic_Record, Institute, Student


def UploadPDF(url=None, subject=None, semester=None, batch=None, institute_id=None):
    if url == None or subject == None or semester == None or batch == None or institute_id == None:
        return 'Error'
    df = pd.read_csv(url)
    print(df)
    # Add try catch
    institute = Institute.objects.get(id=institute_id)

    for i, row in df.iterrows():
        try:
            student = Student.objects.get(roll=row.Roll)
            obj = Academic_Record.objects.create(
                semester=semester, institute=institute, student=student, grade=row.Grade, marks=row.Marks, subject=subject, batch=batch)
            obj.save()
        except:
            continue
    return 'Done'


# UploadPDF(url='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Ftest.csv?alt=media&token=25adb90b-5266-4304-89a8-66c501c9733a', subject='Data Science')
