from threading import Thread
import math

# add the numbers from 1 through N
N = int(input("Enter N: "))

# make a list of 16 partial sums
sum = [0] * 16

# function to sum a range into a partial sum
def sumFrom(a, b, i):
  global sum
  while a <= b:
    sum[i] = sum[i] + a
    a = a + 1


# start 16 threads
threads = []
for i in range(16):
  a = i * math.floor(N / 16) + 1
  b = (i + 1) * math.floor(N / 16)
  if i == 15:
    b = N
  t = Thread(target = sumFrom, args = (a, b, i))
  t.start( )
  threads.append(t)

# wait for them all
for t in threads:
  t.join( )


# add partial sums
total = 0
for s in sum:
  total = total + s

print("Sum from 1 to N =", total)
