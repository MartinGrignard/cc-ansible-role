<!-- Header -->
<a href="https://notioly.com/"><img align="right" style="margin-left: 30pt;" width="40%" src="https://github.com/MartinGrignard/cc-ansible-role/raw/main/img/magic.png"></img></a>

# Cookiecutter - Ansible role

> Let's create [Ansible][ansible] roles! 🪄

This [Cookiecutter][cookiecutter] template aims at providing an easy way to bootstrat a new [Ansible][ansible] role project.
It is mainly built to speed up the definition of the test environments and repository automation.

[![](https://img.shields.io/badge/version-0.1.0-white?labelColor=white&logo=semver&logoColor=3F4551&style=flat-square)](CHANGELOG.md)
[![](https://img.shields.io/badge/license-MIT-white?labelColor=white&logo=open-source-initiative&logoColor=3DA639&style=flat-square)](LICENSE.md)
[![](https://img.shields.io/badge/cookiecutter-white?logo=cookiecutter&logoColor=D4AA00&style=flat-square)][cookiecutter]
[![](https://img.shields.io/badge/cruft-white?logo=cookiecutter&logoColor=D4AA00&style=flat-square)][cruft]
[![](https://img.shields.io/badge/buy_me_a_coffee-FF5E5B?logo=ko-fi&logoColor=white&style=flat-square)][ko-fi]

<!-- Body -->
## Features

Here are the main features included in this template:

| Feature | Description |
|---------|-------------|

## Usage

To use this template, one can simply run the following [Cookiecutter][cookiecutter] command:

```shell
cookiecutter https://github.com/MartinGrignard/cc-ansible-role
```

Or its [Cruft][cruft] equivalent:

```shell
cruft create https://github.com/MartinGrignard/cc-ansible-role
```

## Variables

Here are the variables accepted by this template:

| Variable | Description | Default |
|----------|-------------|---------|
| `author_name` | The name of the author. | `"Martin Grignard"` |
| `author_github_name` | The Github ID of the author. | `"MartinGrignard"` |
| `author_link` | The URL of a profile page of the author. | `"https://github.com/{{ author_github_name }}"` |
| `author_kofi_link` | The URL of the Ko-fi profile of the author. | `"https://ko-fi.com/martingrignard"` |
| `role_name` | The name of the role. | `"My role"` |
| `role_short_description` | The short description of the role. | `"An ansible role."` |
| `role_repository` | The URL of the repository of the role. | `"https://github.com/{{ author_github_name }}/ansible-role-{{ __role_slug }}"` |
| `credit_template` | Whether or not to credit this Cookiecutter template in the README file of the role. | `true` |

## License

This project is published under [MIT license](LICENSE.md).
Feel free to use, modify and redistribute it at will, in accordance with the terms of this permissive license, promoting collaboration and open development.

## Want to support my work?

<a href="https://notioly.com/"><img align="left" style="margin-right: 30pt;" width="20%" src="https://github.com/MartinGrignard/MartinGrignard/raw/main/img/coffee.png"></img></a>

You love this project and want to support my work?
You can always buy me a coffee on [Ko-fi](https://ko-fi.com/martingrignard):

[![Ko-fi](https://img.shields.io/badge/Buy_me_a_coffee-FF5E5B?logo=kofi&logoColor=white&style=for-the-badge)][ko-fi]

<!-- Footer -->
---
*Built with* ❤️ *by [Martin Grignard][martin-grignard].*\
*All the illustrations are from [notioly.com][notioly], by [Mary Amato][mary-amato].*

<!-- References -->
[ansible]: https://www.ansible.com/
[cookiecutter]: https://cookiecutter.readthedocs.io/en/stable/index.html
[cruft]: https://cruft.github.io/cruft/
[ko-fi]: https://ko-fi.com/martingrignard
[martin-grignard]: https://github.com/MartinGrignard
[mary-amato]: https://twitter.com/maryamato88
[notioly]: https://notioly.com/
