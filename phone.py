import phonenumbers
from phonenumbers import geocode

phone_number1 = phonenumbers.parse("+8011552509")

print("\nPhone Number Location\n")
print(geocode.description_for_number(phone_number1, "en"))