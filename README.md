[![Flask Change Microservice Test](https://github.com/noahgift/flask-change-microservice/actions/workflows/main.yml/badge.svg)](https://github.com/noahgift/flask-change-microservice/actions/workflows/main.yml)

# flask-change-microservice
Small Flask Microservice that makes change

*Coursera Lab:  duke-coursera-ccb-lab2*

![coursera-lab](https://user-images.githubusercontent.com/58792/108137449-df0e0300-7089-11eb-8b11-74f478b71d11.png)


## Invoke Endpoint

* Create virtualenv and source it: `python3 -m venv ~/.fcm && source ~/.venv/bin/fcm`
* Install and Test:  `make all`
* Run it:  `python app.py`
* Invoke it.  Options include curl, Postman, httpie.  These methods are documented below


### Curl

`curl http://127.0.0.1:8080/change/1/34`

```bash
[
  {
    "5": "quarters"
  }, 
  {
    "1": "nickels"
  }, 
  {
    "4": "pennies"
  }
]
```




