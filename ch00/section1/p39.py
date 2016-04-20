from scipy import stats

year    = array([0, 5, 10, 15, 20])
vne     = array([25200, 39300, 60800, 88900, 141200])
vmw     = array([20100, 30100, 51900, 58900, 74000])

ne_slope, ne_intercept, ne_r_value, ne_p_value, ne_slope_std_error = stats.linregress(year, vne)
mw_slope, mw_intercept, mw_r_value, mw_p_value, mw_slope_std_error = stats.linregress(year, vmw)


degrees_of_freedom = len(year) - 2

ne = ne_intercept + ne_slope * year
ne_error = vne - ne
ne_residual_std_error = sqrt(sum(ne_error**2)/degrees_of_freedom)

mw = mw_intercept + mw_slope * year
mw_error = vmw - mw
mw_residual_std_error = sqrt(sum(mw_error**2)/degrees_of_freedom)

