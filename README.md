# lat-long-2-address
Got a list of Latitude and Longitude coordinates and want to know what street address it belongs to?
<a name="readme-top"></a>
<!-- PROJECT LOGO -->

<br />
<div align="left">

<h3 align="center">Latitude Longitude to Address</h3>

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
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project


Ever need to convert a list of  Latitude and Longitude coordinates to Street Addresses?  

Run this simple Python 3 script to import a list of your addresses, 'coordinates.csv' and output will include a header, latitude, longitude, and addresses in a CSV file format, 'addresses.csv'

The output file can then be renamed and uploaded to Splunk as a lookup table in a search.

Key Apps to help with managing Lookup Tables and Splunk Configurations, respectively:

[Splunk App for Lookup File Editing](https://splunkbase.splunk.com/app/1724) | [Config Explorer (not compatible with Splunk Cloud)](https://splunkbase.splunk.com/app/4353)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

Python 3

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

This script is designed to work in Linux, MacOS and Windows with Python3 installed.

Assumption: Python and Git are installed on your system.

### Prerequisites

Install the latest version of [geopy](https://github.com/geopy/geopy)

* pip
  
  ```sh
  pip install geopy
  ```
or
* yum
  
  ```sh
  yum install pyton3-geopy
  ```
* apt
  
  ```sh
  apt install pyton3-geopy
  ```  
or however your OS requires you to install geopy

### Installation

1. Simple: Copy/Paste the [[python code](https://raw.githubusercontent.com/PMJeffery/street-address-to-lat-long/main/address2latlong.py)](https://raw.githubusercontent.com/PMJeffery/lat-long-2-address/main/lat-long-2-street.py)

2. Via 'git' command clone the repo
   
   ```sh
   git clone https://github.com/PMJeffery/lat-long-2-address.git
   ```

<!-- USAGE EXAMPLES -->

## Usage


Populate 'coordinates.csv' with a list of Latitude and Longitude coordinates.  CSV Header is NOT required!


```sh
python3 lat-long-2-address.py
```
Results will generate a CSV file, 'addresses.csv'

Depending upon how many coordinates you have entered, it may take more than several seconds to return the results.  If you have a large data set or you rapidly run the script many times, you may get an error regarding excessive API usage.

If you are getting excessive API usage errors, either slice your input file into multiple files or switch to another [geocoder](https://github.com/DenisCarriere/geocoder/tree/master/geocoder) - be sure to read the python code for how to access the geocoder API and adjust the python code accordingly. 

Note that some geocoders may require a login or paid-subscription for higher or unlimited API calls. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
