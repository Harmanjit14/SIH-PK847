import phonenumbers
from phonenumbers import geocoder

ch_number = phonenumbers.parse("+919878565076","CH")
import opencage
apikey = "43afd243ca7c4087aab4db318ff619ab"
print(geocoder.description_for_number(ch_number,"en"))