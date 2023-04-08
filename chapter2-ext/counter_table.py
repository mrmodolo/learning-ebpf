#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from time import sleep

from bcc import BPF


def load_program(filename):
    with open(filename, 'r') as program:
        return program.read()


def main():
    bpf = BPF(text=load_program('./counter_table.bpf'))
    syscall = bpf.get_syscall_fnname("execve")
    bpf.attach_kprobe(event=syscall, fn_name="hello")
    try:
        while True:
            sleep(2)
            s = ""
            for k, v in bpf["counter_table"].items():
                s += f"ID {k.value}: {v.value}\t"
            print(s)
    except KeyboardInterrupt:
        sys.exit()


if __name__ in '__main__':
    main()
