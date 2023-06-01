IP = '192.168.3.1'
res = ''.join([f'{x:10}' for x in IP.split('.')])+'\n'+ ' '.join(bin(int(x,16))[2:].zfill(9) for x in IP.split('.'))
print(res)
