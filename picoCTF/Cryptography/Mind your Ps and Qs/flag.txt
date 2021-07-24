Flag: picoCTF{sma11_N_n0_g0od_00264570}

Note: 
- Với bài này bạn dùng RSA để giải mã
- Cái khó của bài là tìm p, q sao cho: (p, q) = 1 và p.q = n. Tuy nhiên, từ số n ta dùng http://factordb.com/ để dễ dàng tìm p và q. Bài toán sẽ được giải quyết. 

Solve in python:

- from Crypto.Util.number import long_to_bytes, inverse

- n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
- e = 65537
- c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667

- p =  2159947535959146091116171018558446546179
- q =  658558036833541874645521278345168572231473

- phi = (p-1)*(q-1)

- d = inverse(e, phi)

- flag = pow(c,d,n)

- print(long_to_bytes(flag).decode())
