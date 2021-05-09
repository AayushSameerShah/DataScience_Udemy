import numpy as np
def cov(df):
    return sum((df.X - df.X.mean()) * (df.Y - df.Y.mean())) / len(df)

def sx__sy(df):
    return np.sqrt(sum((df.X - df.X.mean()) ** 2) / len(df)), np.sqrt(sum((df.Y - df.Y.mean()) ** 2) / len(df))

def r(df):
    sx, sy = sx__sy(df)
    return cov(df) / (sx * sy)