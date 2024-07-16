
```
bloom-generate rosdebian
fakeroot  debian/rules binary
```

## fakeroot
The fakeroot command is a utility that simulates the effect of having root privileges for file manipulation operations without actually elevating the user's privileges.

```
fakeroot debian/rules binary
```

**debian/rules** need root privilege to execute


---

# CPACK
```
# add to CMakeLists.txt

include(CPack)
```
```
cmake .. -DCMAKE_INSTALL_PREFIX=/opt/ros/humble/share/joystick_interface \
-DCPACK_GENERATOR=DEB \
-DCMAKE_INSTALL_PREFIX=`pwd` \
-DCPACK_DEBIAN_PACKAGE_MAINTAINER='a'
```

---

```bash
cmake ..
cpack -G DEB
```