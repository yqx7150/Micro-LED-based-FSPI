# Micro-LED-based-FSPI

## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image1](fig1.jpg)

## The actual PAT system

![image2](fig2.jpg)

## Reconstruction results of data acquired from actual PAT System

![image3](fig3.jpg)


train:
python main.py --config=aapm_sin_ncsnpp_gb.py --workdir=exp --mode=train --eval_folder=result

test:
python A_PCsampling_demo.py

test默认调用exp_demo下的模型

--workdir=exp_zl
--mode=train
--eval_folder=result
--config=aapm_sin_ncsnpp_gb.py

CUDA_VISIBLE_DEVICES=1 python main.py --config=aapm_sin_ncsnpp_gb.py --workdir=exp_zl --mode=train --eval_folder=result


vali[vali < 0] = 0
