from Crypto.Util.number import long_to_bytes
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
c = 39207274348578481322317340648475596807303160111338236677373

# sử dụng factordb.com để tách n thành p va q
p = 752708788837165590355094155871
q = 986369682585281993933185289261

phi = (p-1)*(q-1)

d = pow(e, -1, phi)

print(long_to_bytes(pow(c,d,n)))

