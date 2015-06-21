import prime

pl=prime.primeList(82500)

for i in range(5*10**4,6*10**4):
    old_phi=prime.phi(i,pl)
    med_phi_n, med_phi_d = prime.fast_phi(prime.fast_pfact(i,pl),pl)
    med_phi=i/med_phi_d*med_phi_n
    new_phi=prime.faster_phi(i,pl)
    if old_phi != new_phi:
        print i, old_phi, med_phi, new_phi