#!/usr/bin/python3

from os import system
import subprocess

# local imports
from join_node import join_node

init_command = "kubeadm init --cri-socket /run/containerd/containerd.sock --pod-network-cidr=10.244.0.0/16"


created = system(init_command)

#kubeadm init --cri-socket /run/containerd/containerd.sock --pod-network-cidr=196.168.0.0/16 
#--kubernetes-version stable

system("mkdir -p $HOME/.kube")
system("sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config")
system("sudo chown $(id -u):$(id -g) $HOME/.kube/config")
print("*"*5, "config files created and granted to user", "*"*5)

system("sudo kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml")
#system("curl https://docs.projectcalico.org/v3.20/manifests/calico.yaml -O")
# curl https://docs.projectcalico.org/manifests/calico.yaml -O
#curl https://docs.projectcalico.org/v3.5/getting-started/kubernetes/installation/hosted/kubernetes-datastore/calico-networking/1.7/calico.yaml -O
#curl https://docs.projectcalico.org/v3.14/manifests/calico.yaml -O
#system("curl https://docs.projectcalico.org/manifests/calico-typha.yaml -o calico.yaml")

#print('start apply calico file')
#system("yes | kubectl apply -f calico.yaml")
#print('calico config file applied')

# test antrea pod network, not working currently (client not int correct namespace)
#TAG=v1.2.3
#kubectl apply -f https://github.com/antrea-io/antrea/releases/download/$TAG/antrea.yml

"""
    Generate new join token and join client
"""
print('start generating new token')
token_command = [
    "kubeadm", "token", "create",
    "--print-join-command"
]
token_result = subprocess.run(token_command, stdout=subprocess.PIPE)
print('token result is', token_result)
token_string = token_result.stdout.decode() + " --cri-socket /run/containerd/containerd.sock"
print('token string is', token_string)

print('start joining node')
join_node(
    token_string = token_string,
    hostname = "80.78.253.246",
    username = "root",
    password = "343845",
)
print('eof joining node')


#system("watch kubectl get pods -A")
