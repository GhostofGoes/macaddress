# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrant Documentation: https://docs.vagrantup.com/v2/
# More boxes at: https://app.vagrantup.com

# Prerequisites: latest versions of Vagrant and VirtualBox
# If you're on Linux, do NOT use apt/yum to install, they are severely outdated.
# Instead, download the .deb from https://www.vagrantup.com/downloads.html,
# and install using "sudo apt install ./<file>.deb".

# Usage: Navigate to the folder containing this file in your CLI (Windows CMD, Linux BASH)
# Create VM:        "vagrant up [name]"
# Destroy VM:       "vagrant destroy [name]"
# Power down VM:    "vagrant halt [name]"
# Power on VM:      "vagrant up [name]"
# VM Command line:  "vagrant ssh [name]"
# Provision:        "vagrant provision [name]"

# Example: "vagrant up centos" creates a CentOS 7 dev/test machine

Vagrant.configure(2) do |config|
  # CentOS 7
  config.vm.define "centos" do |centos|
    centos.vm.box = "centos/7"
    centos.vm.host_name = "macaddress-centos7"
    centos.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "1024"
      vb.name = "macaddress-CentOS-7"
    end
    centos.vm.provision "shell", path: "scripts/centos-provision.sh", privileged: false
  end

  # OpenBSD 6
  config.vm.define "openbsd" do |openbsd|
    openbsd.vm.box = "generic/openbsd6"
    openbsd.vm.host_name = "macaddress-openbsd"
    openbsd.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
      vb.name = "macaddress-OpenBSD-6"
    end
    openbsd.vm.synced_folder ".", "/home/vagrant/macaddress"
    openbsd.vm.provision "shell", path: "scripts/openbsd-provision.sh", privileged: false
  end

  # NetBSD 8
  config.vm.define "netbsd" do |netbsd|
    netbsd.vm.box = "generic/netbsd8"
    netbsd.vm.host_name = "macaddress-netbsd"
    netbsd.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
      vb.name = "macaddress-NetBSD-8"
    end
    netbsd.vm.synced_folder ".", "/home/vagrant/macaddress"
  end

  # FreeBSD 11 (version currently used by PFSense)
  config.vm.define "freebsd" do |freebsd|
    freebsd.vm.box = "generic/freebsd11"
    freebsd.vm.host_name = "macaddress-freebsd"
    freebsd.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
      vb.name = "macaddress-FreeBSD-12"
    end
    freebsd.vm.synced_folder ".", "/home/vagrant/macaddress"
    freebsd.vm.provision "shell", path: "scripts/freebsd-provision.sh", privileged: false
  end

  # OpenSUSE 42
  config.vm.define "opensuse" do |opensuse|
    opensuse.vm.box = "generic/opensuse42"
    opensuse.vm.host_name = "macaddress-opensuse"
    opensuse.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
      vb.name = "macaddress-OpenSUSE-42"
    end
    opensuse.vm.synced_folder ".", "/home/vagrant/macaddress"
  end

  # Solaris 10
  config.vm.define "solaris" do |solaris|
    solaris.vm.box = "tnarik/solaris10-minimal"
    solaris.vm.host_name = "macaddress-solaris"
    solaris.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.memory = "512"
      vb.name = "macaddress-Solaris-10"
    end
    solaris.vm.synced_folder ".", "/home/vagrant/macaddress"
    solaris.vm.provision "shell", path: "scripts/solaris-provision.sh", privileged: false
  end

  # Android
  config.vm.define "android" do |android|
    android.vm.box = "lgromb/androidx86-kk"
    android.vm.host_name = "macaddress-android"
    android.vm.provider "virtualbox" do |vb|
      vb.gui = true
      vb.memory = "1024"
      vb.name = "macaddress-Android-KitKat"
    end
    android.vm.synced_folder ".", "/home/vagrant/macaddress"
  end

  # Windows Server 2012 R2
  config.vm.define "winserver" do |winserver|
    winserver.vm.box = "opentable/win-2012r2-standard-amd64-nocm"
    winserver.vm.host_name = "macaddress-winserver"
    winserver.vm.provider "virtualbox" do |vb|
      vb.gui = true
      vb.memory = "2048"
      vb.name = "macaddress-Windows-Server-2012R2"
    end
    winserver.vm.synced_folder ".", "/home/vagrant/macaddress"
  end

  # Windows 10
  config.vm.define "win10" do |win10|
    win10.vm.box = "Microsoft/EdgeOnWindows10"
    win10.vm.host_name = "macaddress-win10"
    win10.vm.provider "virtualbox" do |vb|
      vb.gui = true
      vb.memory = "2048"
      vb.name = "macaddress-Windows-10"
    end
    win10.vm.synced_folder ".", "/home/vagrant/macaddress"
  end

  # Windows 7
  config.vm.define "win7" do |win7|
    win7.vm.box = "datacastle/windows7"
    win7.vm.host_name = "macaddress-win7"
    win7.vm.provider "virtualbox" do |vb|
      vb.gui = true
      vb.memory = "2048"
      vb.name = "macaddress-Windows-7"
    end
    win7.vm.synced_folder ".", "/home/vagrant/macaddress"
  end
end
