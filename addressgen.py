import cryptobaker
from string import ascii_letters, digits, punctuation
from random import sample
import pyperclip
cyrillic_letters="бвгджзклмнпрстфхцчшщйаэыуояеёюиьъ"
germanic_letters="ÄÖÜẞ"
accented_letters="éèâîôñïç"
all = ascii_letters + digits + punctuation + cyrillic_letters + germanic_letters + accented_letters
encoder = cryptobaker.Recipe(
    cryptobaker.toBase64,
    cryptobaker.toMorse,
    cryptobaker.toHex,
    cryptobaker.join(" ")
)
temp = sample(all, 50)
address = cryptobaker.Bake(temp, encoder)
real_address = str(address.apply(cryptobaker.toSHA256))
print(real_address)
pyperclip.copy(real_address)
print("Automatically copied!")