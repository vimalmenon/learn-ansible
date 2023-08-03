# Learn Ansible

### Prerequisite
- Software Installed
  - VirtualBox installed
  - Vagrant

### Create VirtualEnv
```
python -m venv ./venv
```

### Activate VirtualEnv
```
source ./venv/bin/activate
```
### Install ansible
```
pip install ansible
```

### Vagrant get Id
```
vagrant global-status --prune
```
### Vagrant destroy
```
vagrant destroy {id}
```
### Vagrant list the box
```
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