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
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>

  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A Python microservice that will spawn a web server and return the price of Bitcoin in EUR and CZK in json format.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.logo]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

To run this microservice, you would need python and the requests module installed
* Download Python
  ```sh
  https://www.python.org/downloads/
  ```
* Requests Module
  ```sh
  pip install requests
  ```

### Installation

1. Get a free API Key at [https://apilayer.com](https://apilayer.com)
2. Clone the repo
   ```sh
   git clone https://github.com/ematai1/BTC_Price.git
   ```
3. Install Python packages
   ```pip install requests
   ```
4. Enter your API in `python_price.py`
   ```headers= {
        "apikey": "YOUR_API_KEY"
    }
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

* Running the project inside a container:
Convert the project to a container image and deploy in K8s, 'Dockerfile' and K8s manifest file 'deployment.yml' is present in the repository. 
When deployed, the microservice will autostart and listen in port 8080 by default. 
Listening port can be customized in `python_price.py`
   ```def run(server_class=HTTPServer, handler_class=httpdServer, addr="0.0.0.0", port=8080):
   ```

* Non-container project 
Run the project by executing `python_price.py` file
   ```python3 python_price.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-url]: https://www.python.org/
[Python.logo]: https://img.shields.io/badge/Python-0?style=for-the-badge&logo=python&logoColor=white
