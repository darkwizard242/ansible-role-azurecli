import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

PACKAGE = 'azure-cli'
PACKAGE_BINARY = '/usr/bin/az'
REPO_DEBIAN_FILE = '/etc/apt/sources.list.d/azure-cli.list'
REPO_EL_FILE = '/etc/yum.repos.d/azure-cli.repo'


def test_azurecli_package_installed(host):
    """
    Tests if azure-cli package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_azurecli_binary_exists(host):
    """
    Tests if az binary exists.
    """
    host.file(PACKAGE_BINARY).exists


def test_azurecli_binary_isfile(host):
    """
    Tests if az binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_azurecli_binary_which(host):
    """
    Tests the output to confirm az's binary location.
    """
    assert host.check_output('which az') == PACKAGE_BINARY


def test_azurecli_repofile_exists(host):
    """
    Tests if azure-cli repo file exists.
    """
    assert host.file(REPO_DEBIAN_FILE).exists or \
        host.file(REPO_EL_FILE).exists


def test_azurecli_repofile_isfile(host):
    """
    Tests if azure-cli repo file is file type.
    """
    assert host.file(REPO_DEBIAN_FILE).is_file or \
        host.file(REPO_EL_FILE).is_file
