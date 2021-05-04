<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jiun0507/investurtle">
    <img src="static/img/logo.webp" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Investurtle</h3>

  <p align="center">
    <br />
    <a href="https://tranquil-journey-32319.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/jiun0507/investurtle/issues">Report Bug</a>
    ·
    <a href="https://github.com/jiun0507/investurtle/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
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
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Investurtle:
**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`github_username`, `repo_name`, `email`, `project_title`, `project_description`

### Built With

- [Python](https://www.python.org/downloads/release/python-392/)
- [Django](https://www.djangoproject.com/)
- [Heroku](www.heroku.com)
- [PostgresDB](www.postgresql.org)

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

- pipenv
  ```sh
  pip install pipenv
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jiun0507/investurtle.git
   ```
2. Create a pipenv shell
   ```sh
   pipenv shell
   ```
3. Makesure you have the right Pythonpath and right python version configured
   ```sh
   which python
   # This should print your pipenv's python
   python --version
   # This should give you python 3.9.2. Other python versions are not tried out.
   ```
4. Install pipenv packages
   ```sh
   pipenv install
   ```
5. Run migrations and createsuperuser for Django app
   ```sh
   python manage.py migrate
   # This will migrate all the migration files to the SQLlite database
   python manage.py createsuper
   # Follow this step to create the superuser(for admin)
   ```
6. It's ready to run on your local server. Go to 127.0.0.1:8000/home after running this command.
   ```sh
   python manage.py runserver 8000
   # Run local copy on the localhost port 8000.
   ```

<!-- USAGE EXAMPLES -->

## Usage

- Stock Fianncials: investurtle provides the financial statements of publicly enlisted companies in United States. All the financial statements data comes from the [polygon.io](https://polygon.io).
- Valuation: Investurtle provides an interface through which anyone can evaluate the company's worth based on the financial statements.
- Community: Investurtle provides a platform on which people can share their thoughts and valuations of the companies.
- Alarm system: Investurtle has real-time stock price. If you set the price for a stock ticker, Investurtle will send you an notification when the stock price is below your price of interest.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/jiun0507/investurtle/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Anyone who makes a pull request will be made a contributor.

<!-- LICENSE -->

## License

This is a personal project without any licensing.

<!-- CONTACT -->

## Contact

Jiun Kim - email: jkim2@bodoin.edu

Project Link: [https://github.com/jiun0507/investurtle](https://github.com/jiun0507/investurtle)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

Libraries and templates used

- [polygon.io](https://polygon.io)
- [IEXCloud](https://iexcloud.io)
- [requests](https://docs.python-requests.org/en/master/user/quickstart/)
- [whitenoise](http://whitenoise.evans.io/en/stable/)
- [polygon-api-client](https://pypi.org/project/polygon-api-client/)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- [gunicorn](https://docs.gunicorn.org/en/stable/configure.html)
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/jiun0507/investurtle.svg?style=for-the-badge
[contributors-url]: https://github.com/jiun0507/investurtle/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jiun0507/investurtle.svg?style=for-the-badge
[forks-url]: https://github.com/jiun0507/investurtle/network/members
[stars-shield]: https://img.shields.io/github/stars/jiun0507/investurtle.svg?style=for-the-badge
[stars-url]: https://github.com/jiun0507/investurtle/stargazers
[issues-shield]: https://img.shields.io/github/issues/jiun0507/investurtle.svg?style=for-the-badge
[issues-url]: https://github.com/jiun0507/investurtle/issues
[license-shield]: https://img.shields.io/github/license/jiun0507/investurtle.svg?style=for-the-badge
[linkedin-url]: https://linkedin.com/in/jiun0507
