
nodes = [
  {
    "value" => "node-1",
    "box" => "ubuntu/jammy64",
    "ip" => "192.168.33.10"
  },
  {
    "value" => "node-2",
    "box" => "ubuntu/jammy64",
    "ip" => "192.168.33.11"
  },
  {
    "value" => "node-3",
    "box" => "ubuntu/jammy64",
    "ip" => "192.168.33.12"
  }
]


Vagrant.configure("2") do |config|
  nodes.each do |i|
    config.vm.define i["value"] do |node|
      node.vm.box = i["box"]
      node.vm.network "private_network", ip: i["ip"]
    end
  end
end
