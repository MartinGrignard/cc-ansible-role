<!-- Header -->
<a href="https://notioly.com/"><img align="right" style="margin-left: 30pt;" width="40%" src="https://raw.githubusercontent.com/MartinGrignard/MartinGrignard/main/img/tools.png"></img></a>

# Ansible role - {{ cookiecutter.role_name }}

> {{ cookiecutter.role_short_description }}

Describe the goal of this role here.

[![](https://img.shields.io/badge/version-0.1.0-white?labelColor=white&logo=semver&logoColor=3F4551&style=flat-square)](CHANGELOG.md)
[![](https://img.shields.io/badge/license-MIT-white?labelColor=white&logo=open-source-initiative&logoColor=3DA639&style=flat-square)](LICENSE.md)
[![](https://img.shields.io/badge/ansible-white?logo=ansible&logoColor=EE0000&style=flat-square)](https://www.ansible.com/)
{% if cookiecutter.author_kofi_link -%}
[![](https://img.shields.io/badge/buy_me_a_coffee-FF5E5B?logo=ko-fi&logoColor=white&style=flat-square)]({{ cookiecutter.author_kofi_link }})
{%- endif %}

<!-- Body -->
## Features

Here are the main features included in this role:

| Feature | Description |
|---------|-------------|

## Usage

To use this role in a project, one can simply use the command:

```shell
ansible-galaxy --roles-path './roles' {{ cookiecutter.role_repository }}.git
```

## Variables

Here are the variables accepted by this role:

| Variable | Description | Default |
|----------|-------------|---------|

## Example playbook

Here is an example of how to use this role in a playbook:

```yaml
- hosts: all
```

## License

This project is published under [MIT license](LICENSE.md).
Feel free to use, modify and redistribute it at will, in accordance with the terms of this permissive license, promoting collaboration and open development.

{% if cookiecutter.author_kofi_link -%}
## Want to support my work?

<a href="https://notioly.com/"><img align="left" style="margin-right: 30pt;" width="20%" src="https://github.com/MartinGrignard/MartinGrignard/raw/main/img/coffee.png"></img></a>

You love this project and want to support my work?
You can always buy me a coffee on [Ko-fi](https://ko-fi.com/martingrignard):

[![Ko-fi](https://img.shields.io/badge/Buy_me_a_coffee-FF5E5B?logo=kofi&logoColor=white&style=for-the-badge)]({{ cookiecutter.author_kofi_link }})
{%- endif %}

<!-- Footer -->
---
*Built with* ❤️ *by [{{ cookiecutter.author_name }}][author].*\
{% if cookiecutter.credit_template -%}
*Generated from [cc-ansible-role](https://github.com/MartinGrignard/cc-ansible-role), by [Martin Grignard](https://github.com/MartinGrignard).*\
{%- endif %}
*All the illustrations are from [notioly.com][notioly], by [Mary Amato][mary-amato].*

<!-- References -->
[author]: {{ cookiecutter.author_link }}
