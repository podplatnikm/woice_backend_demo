<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Stargazers][stars-shield]][stars-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/podplatnikm/woice_backend_demo">
    <h3 align="center">Woice Backend Demo</h3>
  </a>
  <p align="center">
    Demo / Test Backend REST and WebSocket api for woice.me first voice messenger
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
        <li><a href="#local-development">Local Development</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#docs">Docs</a></li>
    <li><a href="#changelog">Changelog</a></li>
    <li><a href="#todo">Todo</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Woice Backend is a demo project that implements basic REST and WebSocket API and includes Users and Chat module.
It enables users to authenticate, create chat rooms, publish, edit and delete messages 

### Built With

* [Python 3.8](https://www.python.org/)
* [Django 3](https://www.djangoproject.com/)
* [Django Rest Framework 3](https://www.django-rest-framework.org/)
* [Django Channels 3](https://github.com/django/channels)
* [PostgreSQL](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project heavily relies on **Docker** and (now built in) tool **Docker Compose.** It sets up a 
python docker image with correct version and also a Postgres database. For Channels, this projet uses
in memory broker but should you require redis for production or any other reason, feel free to add that to
`docker-compose.yml`.

### Local Development

**This project features a couple of ready-made scripts to get you up and running quickly.** Basically, scripts run
bash / shell commands. Using .py scripts instead of .bat or .sh makes them non OS specific and if you have python
installed, you can run them.

To start developing:
1. First scaffold docket containers by running:
    * `python .\scripts\docker\up.py` on Windows,
    * `python ./scripts/docker/up.py` on MacOS or Linux,
    * or just run `docker compose up -d`.
    
2. Once the containers are up, 'ssh' into web container, so we can run server and migration scripts.
I like to do this manually vs. specifying them in docker-compose, since by doing former gives me more control.
   To do this, run next script:
   * `python .\scripts\docker\web_bash.py` on Windows,
    * `python ./scripts/docker/web_bash.py` on MacOS or Linux,
    * or just run `docker exec -it woice_web /bin/bash`.
    
3. Run migrations script by executing `python ./scripts/dev_full_migrate.py` in root in container.
4. Run development server on port 8016 by executing `python ./scripts/dev_server.py`

<!-- USAGE -->
## Usage
This project uses a [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow), so make sure you check it out. Always create a
feature branch and go from there. Never do any development on master.
After running the server, you can find API Docs under `{{url}}/api/schema/swagger-ui/` and on [Postman](https://documenter.getpostman.com/view/5623349/TzRa5NwK)

<!-- DOCS -->
## Docs
Swagger docs (openapi) are available as a schema or schema UI when you start a development server under `{{url}}/api/schema/swagger-ui/`.  
Postman docs about REST Api (could be incomplete) and WebSocket are available at: https://documenter.getpostman.com/view/5623349/TzRa5NwK#a272c013-a70e-4481-af83-c055451b3528



<!-- CHANGELOG -->
## Changelog
View [CHANGELOG.md](CHANGELOG.md) for more details

<!-- TODO -->
## Todo
* ~~log in/out (basic JWT token auth is more than ok)~~ **DONE**
* ~~create chat rooms~~ **DONE**
* ~~(optional) create private chat rooms with invites~~ **DONE**
* (optional) add/revoke admin privileges for chat rooms
* ~~find other users~~ **DONE**
* ~~notify users that a user is typing~~ **DONE**
* ~~send messages to users and chat rooms~~ **DONE**
* ~~edit and delete sent messages~~ **DONE**
* (optional) send email notications for missed chats

<!-- LICENSE -->
## License
Distributed under the MIT License



<!-- CONTACT -->
## Contact

Miha Podplatnik - [@mpodplatnik](https://twitter.com/mpodplatnik) - miha.podplatnik@gmail.com

Project Link: [https://github.com/podplatnikm/woice_backend_demo](https://github.com/podplatnikm/woice_backend_demo)

<!-- CONTRIBUTING -->
## Contributing
Please make sure to update tests as appropriate.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/podplatnikm/woice_backend_demo
[stars-url]: https://github.com/podplatnikm/woice_backend_demo/stargazers
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/miha-podplatnik/