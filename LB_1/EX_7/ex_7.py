MAC = 'AAAA:BBBB:CCCC'
MAC = ''.join(bin(int(x,16))[2:].zfill(8) for x in MAC.split(':'))
print(MAC)
