
nodes = [
  {
    "value" => "node-1",
    "hostname" => "app1.test",
    "box" => "centos/7",
    "ip" => "192.168.33.10"
  },
  {
    "value" => "node-2",
    "hostname" => "app2.test",
    "box" => "centos/7",
    "ip" => "192.168.33.11"
  },
  {
    "value" => "node-3",
    "hostname" => "app3.test",
    "box" => "centos/7",
    "ip" => "192.168.33.12"
  }
]


Vagrant.configure("2") do |config|
  nodes.each do |i|
    config.vm.define i["value"] do |node|
      node.vm.hostname = i["hostname"]
      node.vm.box = i["box"]
      node.vm.network "private_network", ip: i["ip"]
    end
  end
end
