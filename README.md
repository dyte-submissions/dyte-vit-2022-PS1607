[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7942788&assignment_repo_type=AssignmentRepo)
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

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/dyte-submissions/dyte-vit-2022-PS1607">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Dyte Project</h3>

  <p align="center">
    A command line tool to manage dependency versions.
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-PS1607"><strong>Explore the docs » (Currently NA)</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-PS1607">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-PS1607/issues">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-PS1607/issues">Request Feature</a>
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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Submission for Dyte Internship shortlisting. Works on macOS/Linux.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To run this tool on your system locally, follow the installation steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
  ```sh
  pip install --upgrade pip
  ```

### Installation

1. Download the repository as zip. Unzip.
2. Put your GitHub Access Token in [github_token.py](https://github.com/dyte-submissions/dyte-vit-2022-PS1607/blob/main/src/dyteproject/github_token.py) in the variable _token_
3. cd to the repository folder
4. Run this command

   ```sh
   python3 setup.py install
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

---> The name of the console script is _dependency_.
For help, run the below command:
  ```sh
  dependency -h
  ```
<br>---> The command _-i_ expects 3 Arguments;  PATH_TO_INPUT_CSV_FILE,  DEPENDENCY_NAME,  DEPENDENCY_VERSION<br>


Usage example#1
  ```sh
  dependency -i /Users/prakhar/downloads/input.csv axios 0.23.0
  ```
Usage example#2
  ```sh
  dependency -i /Users/prakhar/downloads/input.csv eslint 7.32.0
  ```
<br>
---> The tool returns the list in the format as shown below
<img width="749" alt="image" src="https://user-images.githubusercontent.com/77260373/171464381-f234049e-ae58-4de2-80eb-c665347f6564.png">

---> The same is stored in the CSV file used for input

  

_For more examples, please refer to the [Documentation](https://doesnotexist.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Integrate -update feature. (Unable to complete because of time limit)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE.txt`](https://github.com/dyte-submissions/dyte-vit-2022-PS1607/blob/main/LICENSE.txt) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@prakhar16072002](https://twitter.com/prakhar16072002) - prakharsharma1607@gmail.com

LinkedIn - [https://www.linkedin.com/in/prakhar-sharma-2020/](https://www.linkedin.com/in/prakhar-sharma-2020/)

Github Link: [https://github.com/PS1607](https://github.com/PS1607)

Google Developer: [https://g.dev/ps1607](https://g.dev/ps1607)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dyte-submissions/dyte-vit-2022-PS1607.svg?style=for-the-badge
[contributors-url]: https://github.com/dyte-submissions/dyte-vit-2022-PS1607/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dyte-submissions/dyte-vit-2022-PS1607.svg?style=for-the-badge
[forks-url]: https://github.com/dyte-submissions/dyte-vit-2022-PS1607/network/members
[stars-shield]: https://img.shields.io/github/stars/dyte-submissions/dyte-vit-2022-PS1607.svg?style=for-the-badge
[stars-url]: https://github.com/dyte-submissions/dyte-vit-2022-PS1607/stargazers
[issues-shield]: https://img.shields.io/github/issues/dyte-submissions/dyte-vit-2022-PS1607.svg?style=for-the-badge
[issues-url]: https://github.com/dyte-submissions/dyte-vit-2022-PS1607/issues
[license-shield]: https://img.shields.io/github/license/dyte-submissions/dyte-vit-2022-PS1607.svg?style=for-the-badge
[license-url]: https://github.com/dyte-submissions/dyte-vit-2022-PS1607/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/prakhar-sharma-2020/
[product-screenshot]: images/screenshot.png
