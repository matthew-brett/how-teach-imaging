""" Make chaos plots
"""

import numpy as np
import matplotlib.pyplot as plt

chaos = """
          1994 1996 1998 2000 2002 2004 2006 2008 2010 2012
Successful 16% 27% 26% 28%    34% 29% 35% 32%     37% 39%
Challenged 53% 33% 46% 49%    51% 53% 46% 44%     42% 43%
Failed     31% 40% 28% 23%    15% 18% 19% 24%     21% 18%
""".splitlines()
chaos = [L for L in chaos if L.strip()]

years = chaos[0].split()
all_vals = []

for line in chaos[1:]:
    type, percents = line.split(' ', 1)
    vals = [float(v) for v in percents.replace('%', '').split()]
    assert len(vals) == len(years)
    plt.plot(years, vals, label=type)
    all_vals.append(vals)
int_years = [int(year) for year in years]
assert np.all(np.sum(all_vals, axis=0) == 100)
plt.axis([min(int_years), max(int_years), 0, 60])
plt.legend()
plt.title('CHAOS software project outcomes')
plt.xlabel('Year')
plt.ylabel('Percent of projects')
plt.savefig('chaos_results.png')
