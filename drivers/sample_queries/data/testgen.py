import random
NUMMAX = 5000000

fop=open('opk', 'w')
fpc=open('pck', 'w')
fopr=open('oprk', 'w')

order=range(NUMMAX)
random.shuffle(order)
pkey=range(NUMMAX)
random.shuffle(pkey)

for i in range(NUMMAX):
	fop.write(str(order[i]+1))
	fop.write('|')
	fop.write(str(pkey[i]+1))
	fop.write('\n')

order=range(NUMMAX)
random.shuffle(order)
pkey=range(NUMMAX)
random.shuffle(pkey)

for i in range(NUMMAX):
	fpc.write(str(order[i]+1))
	fpc.write('|')
	fpc.write(str(pkey[i]+1))
	fpc.write('\n')

order=range(NUMMAX)
random.shuffle(order)
pkey=range(NUMMAX)
random.shuffle(pkey)

for i in range(NUMMAX):
	fopr.write(str(order[i]+1))
	fopr.write('|')
	fopr.write(str(pkey[i]+1))
	fopr.write('\n')

fop.close()
fpc.close()
fopr.close()
