import phonenumbers
from phonenumbers import carrier, timezone, geocoder

my_number = phonenumbers.parse("+9323434545", "GB")

print(phonenumbers.is_valid_number(my_number))
print(carrier.name_for_number(my_number, "en"))
print(timezone.time_zones_for_number(my_number))
print(geocoder.description_for_number(my_number, 'en'))


