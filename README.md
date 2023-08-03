# Learn Ansible

### Prerequisite
- Software Installed
  - VirtualBox installed
  - Vagrant

### Create VirtualEnv
```sh
python -m venv ./venv
```

### Activate VirtualEnv
```
source ./venv/bin/activate
```
### Install ansible
```sh
pip install ansible
```

### Vagrant get Id
```sh
vagrant global-status --prune
```
### Vagrant create VM's
```sh
vagrant up
```
```sh
sh ./up.sh
```
### Vagrant destroy
```sh
vagrant destroy {id}
```
```
sh ./destory.sh  
```
### Vagrant list the box
```sh
vagrant box list
```

### Ansible Adhoc command
```
ansible app -i ./inventory -a "whoami"
```
### Ansible using module
```
ansible app -i ./inventory -m ping  
```