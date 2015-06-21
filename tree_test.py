import prime

pl=prime.primeList()

for i in range(2,10):
    pf_i=prime.fast_pfact(i,pl)
    old_phi=prime.phi_factor(pf_i,pl)
    new_phi=prime.phi_tree(pf_i,pl)
    print i, pf_i, old_phi, new_phi