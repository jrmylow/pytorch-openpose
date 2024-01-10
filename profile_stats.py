#%%
import pstats

p1 = pstats.Stats('out1.profile')
p2 = pstats.Stats('out2.profile')
p3 = pstats.Stats('out3.profile')
p4 = pstats.Stats('out3.profile')

p = p4

# %%
from pstats import SortKey
p.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(30)

#%%
p.strip_dirs().sort_stats(SortKey.TIME).print_stats(30)
# %%
