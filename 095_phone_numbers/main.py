import phonenumbers

from phonenumbers import timezone, geocoder, carrier
number = input('Enter your number with +__: ')

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
carrier_is = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")
print(phone)
print(time)
print(carrier_is)
print(reg)
