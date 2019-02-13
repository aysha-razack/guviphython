values=input( ).split()
fir=values[0]
sec=values[1]
thi=values[2]
if fir>=sec and fir>=thi:
  print(fir)
elif sec>=fir and sec>=thi:
  print(sec)
else:
  print(thi)
