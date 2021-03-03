with open("input.txt") as f:
    dat = f.readlines()
    dat = [line.strip() for line in dat]

maxid = 0

for ele in dat:
  hr = 127
  lr = 0
  hc = 7
  lc = 0
  chrs = [ c for c in ele]
  chrsR = chrs[0:7]
  chrsC = chrs[7:]
  for c in chrsR:
    if(c == 'F'):
      hr = hr - ( hr - lr ) // 2 - 1 
    else:
      lr = lr + ( hr - lr ) // 2 + 1
  for c2 in chrsC:
    if(c2 == 'F'):
      hc = hc - ( hc - lc ) // 2 - 1 
    else:
      lc = lc + ( hc - lc ) // 2 + 1

  sid = hr * 8 + hc
  print('[',lr,hr,']')
  print('[',lc,hc,']')
  print(sid)
  if(sid > maxid):
    maxid = sid

print(maxid)
  
