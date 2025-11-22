
:blogpost: true
:date: December 28, 2024
:category: Blog Post
:tags: Software Engineering, 12-28-2024
:nocomments:

####################################
*Installing Tailscale With Ansible*
####################################

:bdg-primary:`Blog Post` :bdg-primary-line:`Software Engineering`


***********************
Tailscale Introduction
***********************

I recently found out about Tailscale [1]_ from
the Level1Tech's interview with its CEO Avery Pennarun. After trying it out, I
can say that I am more than satisfied with its performance, ease of use,
and ability to network all of my devices together across different
intranets.

.. dropdown:: Level1Tech's interview with its CEO Avery Pennarun'

   .. youtube:: UyczOQTx5Gg

As someone who prefers to configure their computer using
infrastructure-as-code (IaC) practices, I decided to write an Ansible [2]_
play for installing Tailscale. The following is the play that I created:

.. dropdown:: Ansible play to install Tailscale

   .. code:: yaml

      - name: Install Tailscale
      hosts: myhosts
      become: true
      tasks:
         - name: Download Tailscale GPG Key
            ansible.builtin.uri:
            dest: /usr/share/keyrings/tailscale-archive-keyring.gpg
            url: https://pkgs.tailscale.com/stable/ubuntu/jammy.noarmor.gpg

         - name: Add Tailscale repository
            ansible.builtin.uri:
            dest: /etc/apt/sources.list.d/tailscale.list
            url: https://pkgs.tailscale.com/stable/ubuntu/jammy.tailscale-keyring.list

         - name: Install Tailscale
            ansible.builtin.apt:
            name: tailscale
            update_cache: true
            state: present


This play is my attempt at a direct translation from the Tailscale
download instructions [3]_ .

.. [1] `<https://tailscale.com/>`_

.. [2] `<https://docs.ansible.com/>`_

.. [3] `<https://tailscale.com/download/linux>`_
