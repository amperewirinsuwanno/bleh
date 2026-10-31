bleh_value = 10
def bleh():
  global bleh_value
  for i in range(bleh_value):
    print("bleh")
    bleh_value += 1

while True:
  bleh()
