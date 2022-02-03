[![build-test](https://github.com/darkwizard242/ansible-role-azurecli/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-azurecli/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-azurecli/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-azurecli/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/46026?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/46026?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/46026?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-azurecli&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-azurecli) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-azurecli&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-azurecli) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-azurecli&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-azurecli) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-azurecli&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-azurecli) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-azurecli?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-azurecli?color=orange&style=flat-square)

# Ansible Role: azurecli

Role to install (_by default_) [azure-cli](https://github.com/Azure/azure-cli) package for Debian based and EL based systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
azurecli_pre_reqs_debian:
  - apt-transport-https
  - curl
  - ca-certificates
  - lsb-release
  - gnupg
azurecli_pre_reqs_debian_desired_state: present
azurecli_app_name: azure-cli
azurecli_desired_state: present
azurecli_debian_gpg_key: https://packages.microsoft.com/keys/microsoft.asc
azurecli_repo_debian: "deb [arch={{ ansible_architecture }}] https://packages.microsoft.com/repos/azure-cli/ {{ ansible_lsb['codename'] }} main"
azurecli_repo_debian_when_x86_64: "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ {{ ansible_lsb['codename'] }} main"
azurecli_repo_debian_filename: "{{ azurecli_app_name }}"
azurecli_el_gpg_key: https://packages.microsoft.com/keys/microsoft.asc
azurecli_repo_el_name: azure-cli
azurecli_repo_el_description: Azure CLI
azurecli_repo_el: https://packages.microsoft.com/yumrepos/azure-cli
azurecli_repo_el_filename: "{{ azurecli_app_name }}"
azurecli_repo_el_gpgcheck: yes
azurecli_repo_el_enabled: yes
azurecli_repo_desired_state: present
```

### Variables table:

Variable                               | Description
-------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
azurecli_pre_reqs_debian               | Package required by Azure CLI on Debain based systems.
azurecli_pre_reqs_debian_desired_state | State of the azurecli_pre_reqs_debian_desired_state packages. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
azurecli_app_name                      | Name of Azure CLI package i.e. `azure-cli`
azurecli_desired_state                 | State of the azurecli_app_name package (i.e. `azure-cli` package itself.). Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
azurecli_debian_gpg_key                | Azure CLI GPG required on Debian based systems.
azurecli_el_gpg_key                    | Azure CLI GPG required on EL based systems.
azurecli_repo_debian                   | Repository URL for Debian based systems. Utilized facts such as `ansible_architecture`.
azurecli_repo_debian_when_x86_64       | This variable is used only against systems that are x86_64 type as the architecture is overridden to `arch=amd64` as per Azure CLI's Installation steps.
azurecli_repo_debian_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
azurecli_repo_el_name                  | Repository name for Azure CLI on EL based systems.
azurecli_repo_el_description           | Description to be added in EL based repository file for Azure CLI.
azurecli_repo_el                       | Repository `baseurl` for Azure CLI on EL based systems.
azurecli_repo_el_gpgcheck              | Boolean for whether to perform gpg check against Azure CLI on EL based systems.
azurecli_repo_el_enabled               | Boolean for whether to set Azure CLI repo as 'enabled' on EL based systems.
azurecli_repo_desired_state            | `present` indicates creating the repository file if it doesn't exist on Debian or EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **azure-cli** pacakge).
azurecli_repo_el_filename              | Name of the repository file that will be stored at `/etc/yum/sources.list.d/` on EL based systems.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **azure-cli** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.azurecli
```

For customizing behavior of role (i.e. installation of latest **azure-cli** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.azurecli
  vars:
    azurecli_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **azure-cli** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.azurecli
  vars:
    azurecli_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-azurecli/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
