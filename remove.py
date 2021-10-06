#!/usr/bin/python3

from os import system

system("cd ~ && yes | rm -r .kube")
system("yes | kubeadm reset")
system("rm -r /etc/cni/net.d")

print("kubeadm removed")
