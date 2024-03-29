# Guitar Theory Tool

Web Application built on Flask library in Python.

Tool to aid guitarist in practicing target notes in solos. Specify a scale and underlying chords to see all musically proper notes available and target notes for underlying chords.

## Example

![Form](https://github.com/Khaleeb/GuitarTheoryTool/blob/master/Screenshots/Form.png)
![Results](https://github.com/Khaleeb/GuitarTheoryTool/blob/master/Screenshots/Output.png)

## Instructions

### Host app on local port via Docker image:
*Vist on [Dockerhub](https://hub.docker.com/r/khaleeb/guitartheorytool)*

1. Requires Docker
2. Retrieve image 
    * `docker pull khaleeb/guitartheorytool:latest`
3. Run image
    * `docker run -d -p8080:8080 khaleeb/guitartheorytool`
4. Open web browser to `localhost:8080`

### Manually host app on local port:

1. Requires Python, pip, and virtualenv
2. From FlaskApp directory:
    * Windows:
        * `virtualenv --python <C:\path\to\python.exe> venv`
        * `.\venv\Scripts\activate`
        * `pip install -r requirements.txt`
        * `python server.py`
    * Linux:
        * `python -m venv venv`
        * `source venv/bin/activate`
        * `pip install -r requirements.txt`
        * `python server.py`
3. Open web browser to `localhost:8080`
    * *port number can be changed by modifying PORTNO in server.py*

### Alernatively, console version can be run from root directory:
`python base.py`

#### Future Ideas

* *5,6,7,8 note scales; user programmable*
