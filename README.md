SliDL: a Python library of pre- and post-processing tools for applying deep learning to whole-slide images
==========================================================================================================
[SliDL](https://github.com/markowetzlab/slidl) is a Python library for performing deep learning image analysis on whole-slide images (WSIs), including deep tissue, artefact, and background filtering, tile extraction, model inference, model evaluation and more.

Please see our [tutorial repository](https://github.com/markowetzlab/slidl-tutorial) to learn how to use `SliDL` on an example problem from start to finish.

<p align="center">
  <img src="https://raw.githubusercontent.com/markowetzlab/slidl/main/docs/source/_static/figure1.png" width="700" />
</p>

Installing SliDL and its depedencies
----
Install SliDL by cloning its repository:
```
git clone https://github.com/markowetzlab/slidl
```

SliDL is best run inside an Anaconda environment. Once you have [installed Anaconda](https://docs.anaconda.com/anaconda/install), you can create `slidl-env`, a conda environment containing all of SliDL's dependencies, then activate that environment. Make sure to adjust the path to your local path to the slidl repository:
```
conda env create -f /path/to/slidl/slidl-environment.yml
conda activate slidl-env
```
Note that `slidl-environment.yml` installs Python version 3.7, PyTorch version 1.4, Torchvision version 0.5, and CUDA version 10.0. Stable versions above these should also work as long as the versions are cross-compatible. Be sure that the CUDA version matches the version installed on your GPU; if not, either update your GPU's CUDA or change the `cudatoolkit` line of `slidl-environment.yml` to match your GPU's version before creating `slidl-env`.

Some users have run into an error message saying that something from libvips is missing when `SliDL` tries to import pyvips. This is because on some operating systems, the pip install of pyvips performed in the ```conda env create``` command leads to a flawed pyvips build. To solve this issue, also install pyvips using conda in `slidl-env`:
```
conda install -c conda-forge pyvips
```

For users who don't wish to use conda, `SliDL` can also be installed via pip. To do so, navigate to to the `slidl` directory containing `setup.py`, and run the following command:
```
pip install -e .
```

Learning to use SliDL
----
See our extensive tutorial [here](https://github.com/markowetzlab/slidl-tutorial).

Documentation
----
The complete documentation for `SliDL` including its API reference can be found [here](https://slidl.readthedocs.io/).

Disclaimer
----
Note that this is prerelease software. Please use accordingly.
