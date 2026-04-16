# Cell 3/5: Volatility Engine
import numpy as np

def yang_zhang_series(df, window, tdy=252):
    log_ho = np.log(df['high'] / df['open'])
    log_lo = np.log(df['low'] / df['open'])
    log_co = np.log(df['close'] / df['open'])
    log_oc = np.log(df['open'] / df['close'].shift(1))
    rs = log_ho * (log_ho - log_co) + log_lo * (log_lo - log_co)
    n = window
    k = 0.34 / (1.34 + (n + 1) / (n - 1)) if n > 1 else 0.34
    var_o = log_oc.rolling(n).var()
    var_c = log_co.rolling(n).var()
    var_rs = rs.rolling(n).mean()
    return np.sqrt((var_o + k * var_c + (1 - k) * var_rs) * tdy)