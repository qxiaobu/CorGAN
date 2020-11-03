
We propose a novel Context aware Residual Recurrent Generative Adversarial Network (short for CorGAN) for Sequential Medical Image Generation, which jointly exploits the spatial dependencies of the sequences as well as the peer image generation with generative adversarial networks.

# dataprocess
##	splitdata_aligned.py
Target to concatenate paired MR and CT images 
##	prune_images.py
Target to filter exp images and drop unclear images

# bash command
## - for train

python train.py --dataroot ./expdata_local/aligned --save_epoch_freq 50 --name test_rnngan_20200219_mrct_neckhead --gan_mode lsgan --model runetgan --netG rUnet --gpu_ids 0 --dataset_mode recurrentgan --input_nc 1 --output_nc 1 --direction AtoB --print_freq 500 --batch_size 10 --slice_size 5 --niter 10000

## - for test

python moni_test.py --dataroot ./expdata_local/aligned --name test_rnngan_20200219_mrct_neckhead --model runetgan --netG rUnet --gpu_ids 0 --dataset_mode recurrentgan --input_nc 1 --output_nc 1 --direction AtoB --batch_size 10 --slice_size 5 --epoch 200

## - for output dicom

python output_dicom_1117.py --odd /data/projects/qiaozhi/private/Zhen/NPC --otd ./expdata_local/aligned/test --mdd ./results/test_rnngan_20200219_mrct_neckhead/test_200

# Citation
@inproceedings{

  title={CorGAN: Context aware Recurrent Generative Adversarial Network for Medical Image Generation}, 
  
  author={Qiao, Zhi; Qian, Zhen; Tang, Hui; Yin, Yong; Huang, Chao Huang; Fan, Wei}, 
  
  booktitle = {Accepted by BIBM},
  
  year={2020}, 

}
