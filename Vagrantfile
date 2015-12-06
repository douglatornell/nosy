# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant configuration for testing nosy across multiple Python versions

# The default Vagrant folder syncing configuration is used,
# so the nosy repo clone is available at /vagrant/ on the VM.


# Vagrantfile API/syntax version. Don't touch unless you know what
# you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Ubuntu 14.04 LTS
  config.vm.box = "ubuntu/trusty64"
  config.vm.define "nosy" do |nosy|
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y git make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
        libncurses5-dev
    apt-get autoremove -y

    su vagrant -c "git clone git://github.com/yyuu/pyenv.git /home/vagrant/.pyenv"
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> /home/vagrant/.bash_aliases
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> /home/vagrant/.bash_aliases
    echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bash_aliases

    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv install 3.5.0"
    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv install 3.3.6"
    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv install 3.2.6"
    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv install 2.6.9"
    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv install 2.5.6"
    su vagrant -l -c "/home/vagrant/.pyenv/bin/pyenv global 3.5.0 system 3.3.6 3.2.6 2.6.9 2.5.6"
    su vagrant -l -c "/home/vagrant/.pyenv/shims/pip3 install tox"
  SHELL
end
