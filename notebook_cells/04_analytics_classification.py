# Cell 4/5: Analytics & Classification
def classify_skew(v, thr):
    if v is None: return 'unknown'
    if v < thr.skew_left: return 'left'
    if v > thr.skew_right: return 'right'
    return 'symmetric'
