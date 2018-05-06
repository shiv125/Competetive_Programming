limit=14
mod=10**6+2
r=[1]*limit
#r[i] = 1

for i in range(2,limit)
r[i] = ( mod - (mod/i)*r[mod%i]%mod )%mod;
print r[1],r[2]
