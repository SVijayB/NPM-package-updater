[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7947793&assignment_repo_type=AssignmentRepo)

<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- Removed because the repository is private and the banners don't work if private -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dyte-submissions/dyte-vit-2022-SVijayB">
    <img src="assets/logo.png" alt="Logo">
  </a>

<h3 align="center">SDK Tooling Challenge</h3>

  <p align="center">
    Automate updating Node.JS packages and dependencies!
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-SVijayB"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-SVijayB">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/issues">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/issues">Request Feature</a>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://dyte-internship.herokuapp.com/)

Given a list of Github repositories, assuming all of them are node js projects with a package.json and package-lock.json in the root, \
and the name and version of a dependency is provided, the goal would be to tell if the version present is higher or equal to provided version and if \ lower, the user must have the option to update the dependency.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

-   [Python](https://www.python.org/)
-   [Flask](https://flask.palletsprojects.com/en/2.1.x/)
-   [GitHub API](https://docs.github.com/en/rest)

The application is also currently deployed on the cloud at [Heroku](https://www.heroku.com/).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Alright, let us look into how we can go about setting up the project locally on your system.

### Prerequisites

There are a few prerequisites that we need to install before we can proceed.

-   python-3
    ```sh
    sudo apt-get install python3.8 python3-pip
    ```
-   pip
    ```sh
    sudo apt-get install python3-pip
    ```
-   git
    ```sh
    sudo apt-get install git
    ```

Once you have the prerequesis installed, we can proceed with the installation of the application.

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/dyte-submissions/dyte-vit-2022-SVijayB.git
    ```
2. Install Python Packages
    ```sh
    pip install -r requirements.txt
    ```
3. Create a virtual environment
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment
    ```sh
    source venv/bin/activate
    ```
5. Create an .env file with the following variables
    ```sh
    API_TOKEN = <your-api-token>
    GH_TOKEN = <your-github-token>
    ```

For step 5, API_TOKEN can be any string of characters that you want to use in order to access the API safely.
To create a GitHub token, check out the [GitHub API docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

Alright, the project is all setup. How do we run it? Simple, head over to the `main.py` file in the root of the project and run it.

Your server should be up and running.

    ```sh
    python main.py
    ```

Head over to your the browser and navigate to the following URL: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
The application should be running there.

For more documentation and usage examples, check out the [docs](http://127.0.0.1:5000/api).

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

S Vijay Balaji - [@linkedIn](linkedin.com/in/svijayb) - vijaykumar.19bce7571@vitap.ac.in

Project Link: [https://github.com/dyte-submissions/dyte-vit-2022-SVijayB](https://github.com/dyte-submissions/dyte-vit-2022-SVijayB)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/dyte-submissions/dyte-vit-2022-SVijayB.svg?style=for-the-badge
[contributors-url]: https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dyte-submissions/dyte-vit-2022-SVijayB.svg?style=for-the-badge
[forks-url]: https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/network/members
[stars-shield]: https://img.shields.io/github/stars/dyte-submissions/dyte-vit-2022-SVijayB.svg?style=for-the-badge
[stars-url]: https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/stargazers
[issues-shield]: https://img.shields.io/github/issues/dyte-submissions/dyte-vit-2022-SVijayB.svg?style=for-the-badge
[issues-url]: https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/issues
[license-shield]: https://img.shields.io/github/license/dyte-submissions/dyte-vit-2022-SVijayB.svg?style=for-the-badge
[license-url]: https://github.com/dyte-submissions/dyte-vit-2022-SVijayB/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/SVijayB
[product-screenshot]: assets/screenshot.png
