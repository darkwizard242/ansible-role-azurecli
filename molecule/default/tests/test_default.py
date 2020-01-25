import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_azurecli_repofile_exists(host):
    assert host.file('/etc/apt/sources.list.d/azure-cli.list').exists or \
      host.file('/etc/yum.repos.d/azure-cli.repo').exists


def test_azurecli_repofile_isfile(host):
    assert host.file('/etc/apt/sources.list.d/azure-cli.list').is_file or \
      host.file('/etc/yum.repos.d/azure-cli.repo').is_file


def test_azurecli_package_installed(host):
    assert host.package("azure-cli").is_installed


def test_azurecli_binary_exists(host):
    host.file('/usr/bin/az').exists


def test_azurecli_binary_isfile(host):
    assert host.file('/usr/bin/az').is_file


def test_azurecli_binary_which(host):
    assert host.check_output('which az') == '/usr/bin/az'
