# Location Data Application
First of all, I decided to do it in Python because I understand that it is a language that I have a good command of and that I could do something very different. But in thtdo he saw that something that could be different.

The planning that I did, includes the use of a wiremock that returns the data that will be used in the frontend through an API request and the development of an app that represents the frontend itself.

For the frontend, I decided to use the Flask template to redefine the data on the screen. In defining how to present the map with the locations I ended up choosing to use the html canvas tag, however I ended up having some setbacks in rendering the past data for the template and in the end I saw that something was much more accomplished in javascript than using CSS as i usually like to work. But when I saw that this was happening, I would have no more time to start doing it again via CSS, so I didn't develop the divs in a way that might be more focused on frontend issues with more HTML and CSS.

The backend url is being defined as an environment variable, and is being informed in the docker-compose for simulation and demonstration of communication between containers. So, if the backend URL changes, just change the value of that variable.

## Requirements
- Docker
- Docker Compose

## How to run
- start:
```
./start.sh
```

- stop:
```
./stop.sh
```