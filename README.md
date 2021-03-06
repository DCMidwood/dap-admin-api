<div id="top"></div>
=======

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/DCMidwood/dap-admin-api">
    <img src="static/images/dap_logo.jpg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">dap admin api</h3>

  <p align="center">
    Flask api application for managing an admin db. Utilising Flask, Flask-SQLAlchemy, Psycopg2 and Postgres SQL
    <br />
    <a href="https://github.com/DCMidwood/dap-admin-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/DCMidwood/dap-admin-api">View Demo</a>
    ·
    <a href="https://github.com/DCMidwood/dap-admin-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/DCMidwood/dap-admin-api/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

dap admin api. Flask Application built to manage an admin db for our design automation platform

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)
- [flask](https://flask.palletsprojects.com/en/2.1.x/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Following section indicates how to dpeloy and use the application.

### Prerequisites

Requires a postgres sql database called dapadmin
Check it complies with SQLALCHEMY_DATABASE_URI in the app.py module
Requires tables, values and views, which can be created by running the prompts resources -> postgressql text files

=======
> create a virtual environment
> make sure pipenv is installed
> use pipenv to install the Pipfile
> pipenv shell

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/DCMidwood/dap-admin-api.git
   ```
2. Move into the directory where we have the project files :
   ```bash
   cd dap-admin-api
   ```
3. Create virtual environment
   ```bash
   python -m venv venv
   ```
4. Install the requirements :
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app.py in a python terminal:
   ```bash
   python app.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap
To view trello board [board](https://trello.com/b/u0DfnIM1/dap-admin-kanban)
- [] Feature 1
- [] Feature 2
- [] Feature 3
  - [] Nested Feature

See the [open issues](https://github.com/DCMidwood/dap-admin-api/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Your Name - [@DCMidwood](https://twitter.com/DCMidwood) - daniel.c-m@outlook.com

Project Link: [https://github.com/DCMidwood/dap-admin-api](https://github.com/DCMidwood/dap-admin-api)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- []()
- []()
- []()

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/DCMidwood/dap-admin-api.svg?style=for-the-badge
[contributors-url]: https://github.com/DCMidwood/dap-admin-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DCMidwood/dap-admin-api.svg?style=for-the-badge
[forks-url]: https://github.com/DCMidwood/dap-admin-api/network/members
[stars-shield]: https://img.shields.io/github/stars/DCMidwood/dap-admin-api.svg?style=for-the-badge
[stars-url]: https://github.com/DCMidwood/dap-admin-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/DCMidwood/dap-admin-api.svg?style=for-the-badge
[issues-url]: https://github.com/DCMidwood/dap-admin-api/issues
[license-shield]: https://img.shields.io/github/license/DCMidwood/dap-admin-api.svg?style=for-the-badge
[license-url]: https://github.com/DCMidwood/dap-admin-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/danielcm1
[product-screenshot]: images/screenshot.png
