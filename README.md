# Micro-LED-based-FSPI

## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image1](fig/fig.1.png)

## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image2](fig/fig.2.png)

## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image3](fig/fig.3.png)
## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image4](fig/fig.4.png)
## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image5](fig/fig.5.png)
## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image6](fig/fig.6.png)
## Sparse view PAT reconstruction based on alternating cyclic iteration of wavelet refinement multi-diffusion model

![image7](fig/fig.7.png)


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
