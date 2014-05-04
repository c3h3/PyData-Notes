PLaY Data Note
**************


Vagrant build from a clean Ubuntu Server 14.04 LTS
==================================================

This shows you how to build the `trusty64-gnome` we use. Take VirtualBox as example,

.. code-block::

    vagrant init ubuntu/trusty64
    # some downloading at first time ...

Install minimal GNOME desktop
-----------------------------
Then modify the ``Vagrantfile``, uncomment the line to use gui

.. code-block::

    vb.gui = true

Then start the Vagrant normally, the VM screen should be popped u

.. code-block::
    vagrant up
    vagrant ssh

    # shold be inside vm
    sudo apt-get xorg gnome-core
    # lots of packages to be installed (~750)
    sudo reboot

If everything works normally, you will see GNOME grahical login screen.


Clean up, Settings
------------------

.. code-block::

    # Traditional Chinese Support
    sudo apt-get install language-pack-zh-hant firefox-locale-zh-hant
    sudo apt-get install language-selector-gnome
    sudo gnome-language-selector  # install missing fonts and etc.

    # Time Zone
    sudo dpkg-reconfigure tzdata

    # Remove cloud-init, not really matters
    sudo apt-get purge --auto-remove -y cloud-init


Package the current VM as a new box

.. code-block::

    vagrant package --output trusty64-gnome.box

Then use this box for the following settings by pointing ``trusty64-gnome`` to correct path on your machine in ``Vagrantfile``:

.. code-block::

    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "trusty64-gnome"
    config.vm.box_url = "~/trusty64-gnome.box"  # change this path!

