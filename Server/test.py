import pandas as pd
url = "https://firebasestorage.googleapis.com/v0/b/stately-pulsar-343510.appspot.com/o/static%2Ftest.csv?alt=media&token=25adb90b-5266-4304-89a8-66c501c9733a"

df = pd.read_csv(url)
print(df)