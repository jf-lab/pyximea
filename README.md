pyximea
=======

Python bindings for ximea XiAPI

## Requirement
python3

## example code
```python
import pyximea as xi
cam = xi.Xi_Camera(DevID=0)
cam.set_param('exposure',10000.0)
img =  cam.get_image()
cam.close()
```


## installing
###Linux (Arch)
install ximea driver using the `PKGBUILD` in the repo
cd your_local_clone
python setup.py build_ext -i

###MacOS
install ximea framework
cd your_local_clone
python setup.py build_ext -i

###Windows
install wheel package in the `dist` folder, require python3.5
