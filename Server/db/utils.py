from warnings import catch_warnings
import pandas as pd
from .models import Academic_Record, Institute, Student


def UploadPDF(url=None, subject=None, semester=None, batch=None, institute_id=None):
    if url == None or subject == None or semester == None or batch == None or institute_id == None:
        return False
    df = pd.read_csv(url)
    print(df)
    # Add try catch
    institute = Institute.objects.get(id=institute_id)

    # df = df.dropna()
    # df = df.drop_duplicates('Roll')

    for i, row in df.iterrows():
        try:
            print(row)
            student = Student.objects.get(roll=row.Roll)
            obj = Academic_Record.objects.create(
                semester=semester, institute=institute, student=student, grade=row.Grade, marks=row.Marks, subject=subject)
            obj.save()
        except:
            continue
    return True


# UploadPDF(url='https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Ftest.csv?alt=media&token=25adb90b-5266-4304-89a8-66c501c9733a', subject='Data Science')
