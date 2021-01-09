# Get TEfficiency in Matplotlib

This function still depends on CERN ROOT python libraries.

### Usage:
```
import ROOT
import matplotlib.pyplot as plt
from matplotlib_efficiency import *

eff = GetEfficiency(X_total,X_passed,nBins,binXmin,binXmax)
plt.errorbar(**eff,fmt="o:")
plt.ylabel("Efficiency")
plt.xlabel(var)
plt.show()	
	
```
