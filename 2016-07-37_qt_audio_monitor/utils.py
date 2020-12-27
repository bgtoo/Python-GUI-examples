import numpy as np

#get new jitters
def new_jitters(jitter, z_dims):
    jitters=np.zeros(z_dims)
    for j in range(z_dims):
        if np.random.uniform(0, 1) < 0.5:
            jitters[j] = 1
        else:
            jitters[j] = 1 - jitter
    return jitters

#get new update directions
def new_update_dir(nv2, update_dir, truncation):
    for ni, n in enumerate(nv2):
        #if n >= 2 * truncation - tempo_sensitivity:
        if n > truncation:
            update_dir[ni] = -1
        #elif n < -2 * truncation + tempo_sensitivity:
        elif n < -1 * truncation:
            update_dir[ni] = 1
    return update_dir