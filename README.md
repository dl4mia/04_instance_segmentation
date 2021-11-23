# Exercise Session 3: Introduction to Instance Segmentation

## Connect to your HT Jupyter instance...


1. SSH into our cluster to enable port forwarding. The command is something like:

```
ssh your.user@hpclogin.fht.org -L 8888:gnodeXX:YYYY
```

Replace XX and YYYY, as well as insert your real user name.

2. Now connect to your Jupyter instance from your local broser by going to:
```
localhost:8888
```

## Clone this repo...

In Jupyter...

* Open a terminal window (inside the browser, from within Jupyter).
* Clone this repository by writing `git clone https://github.com/dl4mia/03_instance_segmentation`.
* Navigate into the new folder, containing the envorinment setup and the exercises  


## Setup Environment

From within the same terminal in your browser, create a `conda` environment for this exercise and activate it:


```
conda env create -f environment.yaml
```

Test whether tensorflow and stardist was properly installed and run the following in a fresh notebook:

```
import tensorflow as tf
print(tf.test.is_gpu_available())

import stardist 
```

Now navigate to the exercise folder we cloned just before and start with the exercises! 
