load("../framework/instance_gen.sage")

verbosity = 2

print("=============  SMAUGT-512")
# KS SMAUG-T1 and TiMER
n = 512
m = 512
q = 1024
h = 140

secret_table = [n-h, h//2]
error_table = [384, 247, 66, 7]
D_s = get_distribution_from_table(secret_table, n)
D_e = get_distribution_from_table(error_table, 1024)

"""
_, _, inst = initialize_from_LWE_instance(DBDD_predict_diag, n, q,
                                          m, D_e, D_s, verbosity=verbosity)

inst.integrate_q_vectors(q, report_every=20)
print(" Attack Estimation via GSA + Interesect model ")
inst.estimate_attack()
print(" Attack Estimation via simulation + probabilistic model ")
inst.estimate_attack(probabilistic=True, lift_union_bound=True, silent=False)
"""

print("=============  SMAUGT-768")
# KS SMAUG-T3
n = 768
m = 768
q = 2048
h = 264

secret_table = [n-h, h//2]
D_s = get_distribution_from_table(secret_table, n)

_, _, inst = initialize_from_LWE_instance(DBDD_predict_diag, n, q,
                                          m, D_e, D_s, verbosity=verbosity)

inst.integrate_q_vectors(q, report_every=20)
print(" Attack Estimation via GSA + Interesect model ")
inst.estimate_attack()
print(" Attack Estimation via simulation + probabilistic model ")
inst.estimate_attack(probabilistic=True, lift_union_bound=True, silent=False)


print("=============  SMAUGT-1024")
# KS SMAUG-T5
n = 1024
m = 1024
q = 2048
h = 348

secret_table = [n-h, h//2]
D_s = get_distribution_from_table(secret_table, n)

_, _, inst = initialize_from_LWE_instance(DBDD_predict_diag, n, q,
                                          m, D_e, D_s, verbosity=verbosity)

inst.integrate_q_vectors(q, report_every=20)
print(" Attack Estimation via GSA + Interesect model ")
inst.estimate_attack()
print(" Attack Estimation via simulation + probabilistic model ")
inst.estimate_attack(probabilistic=True, lift_union_bound=True, silent=False)
