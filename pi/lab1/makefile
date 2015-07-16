obj-m += hello.o
 
KERNEL=/lib/modules/`uname -r`/build
 
all:
	make -C $(KERNEL) M=$(shell pwd) modules V=1 ARCH=arm
clean:
	make -C $(KERNEL) M=$(shell pwd) clean