from scipy import stats

# For TSS
t_stat_tss = -2.27
df_tss = 8
p_value_tss = stats.t.sf(abs(t_stat_tss), df_tss) * 2  # To-tailed test
print("P-verdi for TSS:", p_value_tss)

# For COD
t_stat_cod = 0.78
df_cod = 8
p_value_cod = stats.t.sf(abs(t_stat_cod), df_cod) * 2  # To-tailed test
print("P-verdi for COD:", p_value_cod)

# For TOC
t_stat_toc = -1.41
df_toc = 8
p_value_toc = stats.t.sf(abs(t_stat_toc), df_toc) * 2  # To-tailed test
print("P-verdi for TOC:", p_value_toc)
