def clear_data(**kwgs):
    return {k: v for k, v in kwgs.items() if v is not None}
