import os
import shutil
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-root_dir', default='../expdata_npc_whole_zhen', type=str, help="original data root dir")
parser.add_argument('-mr_folder_name', default='NPC_MRI_2', type=str, help="mr folder name")
parser.add_argument('-ct_folder_name', default='NPC_CT_2', type=str, help="ct folder name")
parser.add_argument("--exp_data_folder_name", type=int, default='./expdata_local', help="how to normalize the data")
parameters = parser.parse_args()
root_dir = parameters.root_dir
ct_fold_name = parameters.ct_folder_name
mri_fold_name = parameters.mr_folder_name
exp_dir = parameters.exp_data_folder_name

if os.path.isdir(exp_dir) is False:
    os.mkdir(exp_dir)

exp_dir = os.path.join(exp_dir, 'aligned')
if os.path.isdir(exp_dir):
    shutil.rmtree(exp_dir)
os.mkdir(exp_dir)

ct_dir = os.path.join(root_dir, ct_fold_name'NPC_CT_2')
mr_dir = os.path.join(root_dir, mri_fold_name'NPC_MRI_2')
ratio = 0.8
pids = {}
pids_list = []
for imagename in os.listdir(ct_dir):
    pid = imagename.split('_')[0]
    if pids.get(pid) is None:
        pids[pid] = len(pids)
        pids_list.append(pid)

os.mkdir(os.path.join(exp_dir, 'train'))
os.mkdir(os.path.join(exp_dir, 'test'))

test_set = pids_list[int(len(pids_list)*ratio):]
print(test_set)
for ct_i in os.listdir(ct_dir):
    wct = ct_i.split('.')[0].split('_')
    maybe_wmr = wct[0]+'_MRI_matched_'+wct[-1]+'.png'
    if maybe_wmr in os.listdir(mr_dir):
        dirAB = ''
        if wct[0] in test_set:
            dirAB = 'test'
        else:
            dirAB = 'train'
        # print(ct_i, maybe_wmr)
        ctImage = Image.open(os.path.join(ct_dir, ct_i))
        mrImage = Image.open(os.path.join(mr_dir, maybe_wmr))

        width, height = ctImage.size
        result = Image.new(ctImage.mode, (2 * width, height))
        result.paste(mrImage, box=(0, 0))
        result.paste(ctImage, box=(width, 0))
        
        result.save(os.path.join(exp_dir, dirAB+'/'+wct[0]+'_mrL_ctR_'+wct[-1]+'.png'))
