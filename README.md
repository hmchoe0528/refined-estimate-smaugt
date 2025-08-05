# Refined SMAUG-T's security estimation
Based on https://github.com/lducas/leaky-LWE-Estimator/tree/NIST-round3

Try 
```
sage Refined-estimate/smaugt-bkz.sage
```
to simulate BKZ or use pre-computed BKZ predictions for gates-count estimation: 
```
python3 Refined-estimate/smaugt-gates.py
```

You may get the following, for each NIST's security level requirements (1, 3, and 5):

| Scheme         | n    | β   | β'  | Gates  | Memory |
|----------------|------|-----|-----|--------|--------|
| Kyber-1        | 1025 | 413 | 375 | 151.5  | 93.8   |
| Frodo-1        | 1297 | 496 | 453 | 175.1  | 110.4  |
| SMAUG-T1-LWE   |  904 | 417 | 379 | 152.4  | 94.6   |
| SMAUG-T1-LWR   |  897 | 416 | 378 | 152.1  | 94.4   |
| **REQUIRED**   |      |     |     | **143.0** |        |

| Scheme         | n    | β   | β'  | Gates  | Memory |
|----------------|------|-----|-----|--------|--------|
| Kyber-3        | 1467 | 637 | 586 | 215.1  | 138.5  |
| Frodo-3        | 1969 | 724 | 668 | 240.0  | 155.8  |
| SMAUG-T3-LWE   | 1360 | 629 | 578 | 212.5  | 136.8  |
| SMAUG-T3-LWR   | 1392 | 653 | 601 | 219.4  | 141.7  |
| **REQUIRED**   |      |     |     | **207.0** |        |

| Scheme         | n    | β   | β'  | Gates  | Memory |
|----------------|------|-----|-----|--------|--------|
| Kyber-5        | 1918 | 894 | 829 | 287.3  | 189.7  |
| Frodo-5        | 2634 | 957 | 888 | 305.4  | 202.1  |
| SMAUG-T5-LWE   | 1775 | 879 | 814 | 282.6  | 186.5  |
| SMAUG-T5-LWR   | 1775 | 892 | 827 | 286.5  | 189.3  |
| **REQUIRED**   |      |     |     | **272.0** |        |

