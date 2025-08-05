from cost import *


# Result of the DDGR20 BKZ prediction for SMAUG-T LWE parameter
#
# =============  SMAUGT-512 and TiMER
# LWE #
# GSA Intersect:                dim=904     δ=1.003915  β=409.95
# Probabilistic simulation:     dim=904                 β=417.08
# LWR #
# GSA Intersect:                dim=897     δ=1.003917  β=409.66
# Probabilistic simulation:     dim=897                 β=416.72 
# =============  SMAUGT-768
# LWE #
# GSA Intersect:                dim=1360    δ=1.002930  β=615.80
# Probabilistic simulation:     dim=1360                β=629.06 
# LWR #
# GSA Intersect:                dim=1392    δ=1.002850  β=639.71
# Probabilistic simulation:     dim=1392                β=653.53 
# =============  SMAUGT-1024
# LWE #
# GSA Intersect:                dim=1775    δ=1.002290  β=859.43 
# Probabilistic simulation:     dim=1775                β=879.30
# LWR #
# GSA Intersect:                dim=1784    δ=1.002290  β=872.07 
# Probabilistic simulation:     dim=1784                β=892.19


print("              \t& n   \t&  β \t& β' \t& gates \t& memory ")
print("-"*65)

print("Kyber-1      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1025, 413))
print("Frodo-1      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1297, 496))
print("SMAUG-T1-LWE \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(904 , 417))
print("SMAUG-T1-LWR \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(897 , 416))
print("-"*31+" REQUIRED: 143.0 "+"-"*16+"\n")

print("Kyber-3      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1467, 637))
print("Frodo-3      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1969, 724))
print("SMAUG-T3-LWE \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1360, 629))
print("SMAUG-T3-LWR \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1392, 653))
print("-"*31+" REQUIRED: 207.0 "+"-"*16+"\n")

print("Kyber-5      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1918, 894))
print("Frodo-5      \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(2634, 957))
print("SMAUG-T5-LWE \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1775, 879))
print("SMAUG-T5-LWR \t& %d\t& %d\t& %d\t& %.1f \t& %.1f "%summary(1775, 892))
print("-"*31+" REQUIRED: 272.0 "+"-"*16+"\n")



