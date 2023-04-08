# IO Visor Project

https://github.com/iovisor

## BPF Compiler Collection (BCC)

https://github.com/iovisor/bcc

## Installing BCC

[Installing BCC](https://github.com/iovisor/bcc/blob/master/INSTALL.md#kernel-configuration)

### For Jammy (22.04)

```bash
sudo apt install -y \
bison \
build-essential \
cmake \
flex \
git \
libedit-dev \
libllvm14 \
llvm-14-dev \
libclang-14-dev \
zlib1g-dev \
libelf-dev \
libfl-dev \
python3-setuptools
```

### For Lua support

```bash
sudo apt install luajit luajit-5.1-dev
```

### Install and compile BCC

```bash
git clone https://github.com/iovisor/bcc.git
mkdir bcc/build; cd bcc/build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/opt/bcc ..
make
sudo make install
cmake -DPYTHON_CMD=python3 .. # build python3 binding
pushd src/python/
make
~~sudo make install~~
popd
```
### Build examples in src/bcc/libbpf-tools

Before build, install dependencies

```bash
sudo apt install llvm libbfd-dev
```
For include error:

> In file included from javagc.bpf.c:6:
> In file included from /srv/GOBEKLI_TEPE/src/bcc/libbpf-tools/.output/bpf/usdt.bpf.h:6:
> /usr/include/linux/errno.h:1:10: fatal error: 'asm/errno.h' file not found
> #include <asm/errno.h>

Solution: Add **-I/usr/include/x86_64-linux-gnu**

> diff --git a/libbpf-tools/Makefile b/libbpf-tools/Makefile
> index 955d59ef..9cf43c4d 100644
> --- a/libbpf-tools/Makefile
> +++ b/libbpf-tools/Makefile
> @@ -8,7 +8,7 @@ BPFTOOL ?= $(BPFTOOL_OUTPUT)/bootstrap/bpftool
>  LIBBPF_SRC := $(abspath ../src/cc/libbpf/src)
>  LIBBPF_OBJ := $(abspath $(OUTPUT)/libbpf.a)
>  LIBBLAZESYM_SRC := $(abspath blazesym/target/release/libblazesym.a)
> -INCLUDES := -I$(OUTPUT) -I../src/cc/libbpf/include/uapi
> +INCLUDES := -I$(OUTPUT) **-I../src/cc/libbpf/include/uapi** **-I/usr/include/x86_64-linux-gnu**
>  CFLAGS := -g -O2 -Wall
>  BPFCFLAGS := -g -O2 -Wall
>  INSTALL ?= install

## Python3 and Virtualenv

```bash
cd ~/playground/learning-ebpf/ch02/helloword
python -mvenv venv
source venv/bin/activate
tar xf /home/modolo/src/bcc/build/src/python/bcc-python3/dist/bcc-0.27.0+9371e844.tar.gz
cd bcc-0.27.0+9371e844
python setup.py install
```

## Python System Wild

- bpfcc-tools
- libbpf0:amd64
- libbpfcc
- libbpfcc-dev
- libpfm4:amd64
- python3-bpfcc

## bpftool

```bash
sudo apt install bpftool
sudo apt install linux-tools-generic
```

## Docs

[What is CMake equivalent of 'configure --prefix=DIR && make all install '?](https://stackoverflow.com/questions/6003374/what-is-cmake-equivalent-of-configure-prefix-dir-make-all-install)

