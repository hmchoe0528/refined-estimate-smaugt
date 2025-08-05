from cost import *


# Result of the DDGR20 BKZ prediction
#
# =============  SMAUGT-512
# GSA Intersect:                dim=904 	 δ=1.003915 	 β=409.95
# Probabilistic simulation:     dim=904                      β=417.08
# =============  SMAUGT-768
# GSA Intersect:                dim=1360 	 δ=1.002930 	 β=615.80
# Probabilistic simulation:     dim=1969 	 			 	 β=724.78 
# ======= Frodo-1344
# GSA Intersect:                dim=2634 	 δ=1.002152 	 β=933.55  
# Probabilistic simulation:     dim=2634 	 	 	 		 β=957.51  


print("              \t& n   \t&  β \t& β' \t& gates \t& memory ")
print("-"*65)

print("Kyber-1  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1025, 413))
print("Frodo-1  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1297, 496))
print("SMAUG-T1 \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(904 , 417))
print("-"*65)

print("Kyber-3  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1467, 637))
print("Frodo-3  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1969, 724))
print("SMAUG-T3 \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1360, 615))
print("-"*65)

print("Kyber-5  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1918, 894))
print("Frodo-5  \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(2634, 957))
print("SMAUG-T5 \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1360, 615))
print("-"*65)


