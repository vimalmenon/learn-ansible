# Learn Ansible

### Prerequisite
- Software Installed
  - VirtualBox installed
  - Vagrant

### Modules
  - [x] Copy
  - [x] Ping
  - [x] Command
  - [x] Package
    - [ ] yum, apt
  - [x] lineinfile
  - [ ] Fetch
  - [x] Url
  - [ ] zip
  - [ ] user
  - [ ] Git
- [ ] Roles
- [ ] Collection
- [x] post_tasks
- [x] pre_tasks
- [x] handlers
- [ ] Assert

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

### Running Simple Playbook file in example Playbook1
```sh
ansible-playbook ./examples/Playbook1/simple.play.yml -i inventory -v
```

### Checking syntax for simple Playbook file in example Playbook1
```sh
ansible-playbook ./examples/Playbook1/simple.play.yml -i inventory --syntax-check
```

### Encrypt var files
```sh
ansible-vault encrypt <file-path>
```

### Playbook sample
```sh
ansible-playbook ./examples/Playbook2/01.play.yml -i inventory --syntax-check
```
```sh
ansible-playbook ./examples/Playbook3/01.play.yml -i inventory --syntax-check
```
  
### Reference
[VM Images](https://app.vagrantup.com/boxes/search?utf8=%E2%9C%93&sort=downloads&provider=)
