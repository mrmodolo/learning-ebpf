#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from bcc import BPF

PROGRAM = r"""
int hello(void *ctx) {
bpf_trace_printk("Hello World!");
return 0;
}
"""


def main():
    b = BPF(text=PROGRAM)
    syscall = b.get_syscall_fnname("execve")
    b.attach_kprobe(event=syscall, fn_name="hello")
    try:
        b.trace_print()
    except KeyboardInterrupt:
        sys.exit()


if __name__ in '__main__':
    main()
