# generator delegation
def countup(stop):
    n = 1
    while n <= stop:
        yield n
        n += 1

def countdown(start):
    n = start        # ✅ Start from `start`
    while n >= 1:    # ✅ Count down until we reach 1
        yield n
        n -= 1

def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)

for x in up_and_down(5):
    print(x, end=" ")
    
# Enhanced Generator and yeild expressions
def reciever():
  print("Ready to recieve")
  while True:
    n = yield
    print("Got", n)
r = reciever()
print(r.send(None))
print(r.send(1))
print(r.send(2))
print(r.send(3))