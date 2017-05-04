# GeneGAN: Learning Object Transfiguration and Attribute Subspace from Unpaired Data

By Shuchang Zhou, Taihong Xiao, Yi Yang, Dieqiao Feng, Qinyao He, Weiran He

### Introduction

This is the official source code for the paper GeneGAN: Learning Object Transfiguration 
and Attribute Subspace from Unpaired Data. All the experiments are initially done in 
our private deep learning framework. For convenience, we reproduce the results using TensorFlow.


<div style="text-align: center">
<img align="center" src="https://lh5.googleusercontent.com/kaT-oG3rx0MCfmVhr31LgRL5pGuF6ntMB-TNAYmtWFFxUx-h2EAWe71sXNmnO_fhQyMdF7qPbjxyOCk=w1220-h927" width="450" alt="Hair">
<center>Hair</center>
</div>   
<br/>

GeneGAN is a deterministic conditional generative model that can learn to disentangle the object
features from other factors in feature space from weak supervised 0/1 labeling of training data.
It allows fine-grained control of generated images on a certain attribute in a continous way.

### Training GeneGAN on celebA dataset

1.  Download [celebA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) dataset and unzip it into 
`dataset` directory. Please ensure that you have the following directory tree structure, and the 
resolution of all images is 418x594.
```
├── datasets
│   └── celebA
│       ├── data
│       ├── list_attr_celeba.txt
│       └── list_landmarks_celeba.txt
```

1.  Run `preprocess.py`. It will take several miniutes to preprocess all face images. 

1.  Run `python train.py -a Smiling -g 0` to train a GeneGAN. You can find all available 
attribute names in the `list_attr_celeba.txt` file. 

1.  Run `tensorboard --logdir='./' --port 6006` to examine the training process.

### Results


##### 1. Swapping of Attributes 

You can easily replace the object for images in each row with those of the column heads. 

<div style="text-align: center">
<img align="center" src="https://lh4.googleusercontent.com/wQ5LI891sz6R2n7TyVEoOL8_YZzdT6hm-4NPtgT5ffvel-T78ymq9xfgfoi1YwXfIzTjYiV8bEzgF9k=w1220-h927" alt="Hair">
<center>Bangs</center>
</div>   
<br/>

<div style="text-align: center">
<img align="center" src="https://lh3.googleusercontent.com/eslrBQtMf94HFHRUXS5eGQJFXL9HEnWdn5-ZPTUS5e9RScz8CC9sqJVqOgYMirJOParkm8k07RpOivQ=w1220-h927" alt="Smiling">
<center>Smiling</center>
</div>
<br/>

<div style="text-align: center">
<img align="center" src="https://lh3.googleusercontent.com/NexLizC6_UMdvyHd_3VQBNs9V-DtJQPKptCKqNYSU_1TLUDOBebDBvY29GqDw__X2Qm5hdkSvVbdjoo=w1220-h927" alt="Eyeglasses">
<center>Eyeglasses</center>
</div>
<br/>


##### 2. Generalization to Unseen Images 

We can use GeneGAN trained on celebA dataset to swap attributes of images in the Wider Face dataset.

<div style="text-align: center">
<img align="center" src="https://lh4.googleusercontent.com/bjG6xj5_g_CgXeJJ6EAHP_mgqrCQYXWco23Wt3AiCRbFFmlS6jEsNR_gns2PJDYvQsKEDjqKLGdcOyg=w1220-h927" alt="Eyeglasses">
<center>Bangs</center>
</div>
<br/>

##### 3. Interpolation in Attribute Subspace

GeneGAN can disentangle certain attribute from a large image space. The attributes subspace is almost linear 
so that we can do interpolation in this subspace.

<div style="text-align: center">
<img align="center" src="https://lh3.googleusercontent.com/gb-kYAbeMwxl7sqdnvI2U0EglDPCy5nQiWdvfGfFZn0640jFsFxtoL3yxPsFUNOabKAO3vyVuhIAFEE=w1220-h927" alt="Eyeglasses">
<center>Bangs</center>
</div>
<br/>

