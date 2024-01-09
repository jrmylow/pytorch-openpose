#%%
import pstats

p1 = pstats.Stats('out1.profile')
p2 = pstats.Stats('out2.profile')

# %%
from pstats import SortKey
p2.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats(30)

#%%
p2.strip_dirs().sort_stats(SortKey.TIME).print_stats(30)
# %%
