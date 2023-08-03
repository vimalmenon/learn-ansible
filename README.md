# Learn Ansible

### Prerequisite
- Software Installed
  - VirtualBox installed
  - Vagrant

[VM Images](https://app.vagrantup.com/boxes/search?utf8=%E2%9C%93&sort=downloads&provider=)

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
### Vagrant list the VM Downloaded
```sh
vagrant box list
```

### Ansible Adhoc command
```sh
ansible app -i ./inventory -a "whoami"
```
### Ansible Adhoc command with module ping
```sh
ansible app -i ./inventory -m ping
```
### Ansible Adhoc command with module setup
```sh
ansible app -i ./inventory -m setup
```

### SSH without checking known_hosts
```sh
ssh -o StrictHostKeyChecking=no vagrant@192.168.33.10 -i ${key}
```