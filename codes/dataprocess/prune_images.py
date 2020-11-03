import os
from PIL import Image
import numpy as np

dict = {}
rdir = './expdata_local_brain_prune/aligned/test'

print (len(os.listdir(rdir)))
for fn in os.listdir(rdir):
    pid = fn.split('_')[0]
    if dict.get(pid) is None:
        dict[pid] = []
    dict[pid].append((int(fn.split('.')[0].split('_')[-1]), os.path.join(rdir, fn)))

print (len(dict))
#exit()
for pid, slice_list in dict.items():
    print (pid)
    cur_list = sorted(slice_list, key = lambda x: x[0])
    for i in range(0, len(cur_list)):
        cur_img = Image.open(cur_list[i][1]).convert('L')
        w, h = cur_img.size
        mra = np.array(cur_img)[:int(w/2), :h]
        mra[mra > 0] = 2
        mra[mra == 0] = 1
        mra[mra == 2] = 0
        ratio = float(np.sum(mra)) / (int(w / 2) * h)
        if ratio > 0.6:
            os.remove(cur_list[i][1])
        else:
            break

    for i in range(len(cur_list)-1, -1, -1):
        cur_img = Image.open(cur_list[i][1]).convert('L')
        w, h = cur_img.size
        mra = np.array(cur_img)[:int(w/2), :h]
        mra[mra > 0] = 2
        mra[mra == 0] = 1
        mra[mra == 2] = 0
        ratio = float(np.sum(mra)) / (int(w / 2) * h)
        if ratio > 0.3:
            os.remove(cur_list[i][1])
        else:
            break
print (len(os.listdir(rdir)))
