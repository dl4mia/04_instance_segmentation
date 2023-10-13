# DL4MIA 2023: 04 - Instance Segmentation with StarDist and Cellpose

**[Return to the Welcome page](https://tinyurl.com/33y2b2hk)**

### Goals

1. Train and infer with a 2D *StarDist* network
2. Train and infer with a 3D *StarDist* network
3. Fine-tune a pre-trained *Cellpose* model on a 2D dataset for a few epochs
4. Fine-tune a pre-trained *Cellpose* model on a 3D dataset for a few epochs

### Overview

In this tutorial, we shall learn to use *StarDist* and *Cellpose* notebooks to train a model for **2D** and **3D** instance segmentation on microscopy images.

### [0/4] Create Environment

Open a fresh terminal window (click on *Activities* at top-left and select *Terminal* Window), change directory to `DL4MIA` and enter the following commands:

```bash
cd DL4MIA
conda create -y -n kerasEnv python=3.7
conda activate kerasEnv
conda install -c conda-forge tensorflow-gpu=2.6.0 jupyter
pip install keras==2.6.* 
pip install stardist CSBDeep gdown
git clone https://github.com/dl4mia/04_instance_segmentation.git
cd 04_instance_segmentation
```

### [1/4] Train and infer with a 2D *StarDist* network

Browse to the 2D exercise (*instance_segmentation_2D.ipynb*):

```bash
cd stardist
jupyter notebook
```

### [2/4] Train and infer with a 3D *StarDist* network

Browse to the 3D exercise (*instance_segmentation_3D.ipynb*) in the browser.

### [3/4] Fine-tune a pre-trained *Cellpose* model on a 2D dataset for a few epochs

To use *Cellpose*, we run a couple of scripts (instead of going through a notebook!)

First, let’s download a 2D data of interest. Open a fresh terminal window, change directory to `cellpose` and run `download_cellpose2D_data.py`. This downloads the images and masks to a directory named `data/cellpose_2D`.

```bash
cd cellpose
python3 download_cellpose2D_data.py
```

Next, let’s activate the environment `pytorchEnv` (which we created in the U-Net example and which already has a working installation of pytorch). And let’s install `cellpose` in it.

```bash
conda activate pytorchEnv
pip install cellpose
```

Next, we train the model by first initializing to the pre-trained model weights (`--pretrained_model nuclei`).

```bash
python -m cellpose --train --dir data/cellpose_2D/train/ --pretrained_model nuclei --n_epochs 10 --img_filter _img --mask_filter _masks --use_gpu --verbose
```

Finally, let’s evaluate the result of the fine-tuned model on the test data. Adjust the path to the `pretrained_model` appropriately. (Hint: Look into the directory `data/cellpose_2D/train/models/<right_file_name>`.)

```bash
python -m cellpose --dir data/cellpose_2D/test --pretrained_model data/cellpose_2D/train/models/<right_file_name> --save_tif --use_gpu --verbose  --img_filter _img  --mask_filter _masks
```

### [4/4] Fine-tune a pre-trained *Cellpose* model on a 3D dataset for a few epochs

Let’s download a 3D data of interest `Mouse-Skull-Nuclei-CBG`.

Open a fresh terminal window, change directory to `cellpose` and run `download_mouse-skull-nuclei-cbg_data.py`. This downloads the images and masks to a directory named `data/mouse-skull-nuclei-cbg/download`.

```bash
python3 download_mouse-skull-nuclei-cbg_data.py
```

Next, let’s activate the environment (if not activated already) and train the model by first initializing to the pre-trained model weights (`--pretrained_model nuclei`).

```bash
conda activate pytorchEnv
python -m cellpose --train --dir data/Mouse-Skull-Nuclei-CBG/download/train/ --pretrained_model nuclei --n_epochs 25 --img_filter _im --mask_filter _ma --use_gpu --verbose
```

Finally, let’s evaluate the result of the fine-tuned model on the test data. Adjust the path to the `pretrained_model` appropriately. (Hint: Look into the directory `data/Mouse-Skull-Nuclei-CBG/download/train/models`.)

Note: Adjust the `anisotropy` (ratio of z pixel size to x or y pixel size) based on settings of your acquired data. Also crucial to specify `do_3D`

```bash
python -m cellpose --dir data/Mouse-Skull-Nuclei-CBG/download/test --pretrained_model data/Mouse-Skull-Nuclei-CBG/download/train/models/cellpose_residual_on_style_on_concatenation_off_train_2022_07_17_13_22_14.311969 --save_tif --use_gpu --verbose  --img_filter _im  --mask_filter _ma --do_3D --anisotropy 2.7397
```
