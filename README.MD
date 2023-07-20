# Casting Agency

## Capstone project for Udacity fullstack-web-developer program
a simple backend based application to create delete, update movies and actors
hosted online on RENDER
The application includes all CRUD features and JWT decoding, coding using AUTH0

##  Getting started

the application is deployed and hosted using RENDER using RENDER webservice and RENDER postgresql on this URL:
https://capstone-service.onrender.com
the db dump created to include some data from the local testing db to add data to showcase resutls in endpoints
- TO RUN THE APP LOCALLY
1. change the config.py data to your local database
2. pip install -r requirements.txt to install all dependecies
3. set FLASK_APP=app.py
4. flask run --reload

#### Error handling 
- Errors excpected 
- 404: Not found
- 422: Unprocessable Entity
- 500: Internal Server Error
- Errors are formated using Json with this format:
({"success": False,
 "error": 404,
 "message": "resource not found"
 })

### Endpoints

#### GET /movies
- General:  
    - returns available movies
    - sample: curl https://capstone-service.onrender.com/movies
{"Movies":
[{"id":3,"release_date":"Wed, 19 Jul 2023 00:00:00 GMT","title":"batman23"},
{"id":4,"release_date":"Sun, 08 May 2005 00:00:00 GMT","title":"batman"},
{"id":5,"release_date":"Tue, 18 Jul 2023 00:00:00 GMT","title":"Test Movie"},
{"id":6,"release_date":"Tue, 18 Jul 2023 00:00:00 GMT","title":"Test Movie"},]}


### GET /actors
- General:  
    - returns available actors
    - sample: curl https://capstone-service.onrender.com/actors
{"Actors:":
[{"age":31,"gender":"male","id":3,"name":"moh"},
{"age":31,"gender":"male","id":4,"name":"moh2"},{"age":31,"gender":"male","id":5,"name":"moh3"},
{"age":31,"gender":"male","id":6,"name":"moh4"},{"age":31,"gender":"male","id":7,"name":"moh5="},
{"age":30,"gender":"Male","id":11,"name":"Test Actor"},{"age":30,"gender":"Male","id":12,"name":"Test Actor"}]}    


## ROLE BASE AUTHENTICATION USING AUTH0
the application has Role Based Authentication and roles-based access control (RBAC) for three roles with permissions:
Using this syntax and changing the user data (password,email)
curl --request POST --url https://3z12k.eu.auth0.com/oauth/token 
--header "content-type: application/json" 
--data "{\"grant_type\":\"password\",\"username\": \"ACTUALL_EMAIL\",\"password\": \"ACTUALLPASSWORD\",\"audience\": \"http://127.0.0.1:5000\",\"client_id\": \"cEuXaQ5NojpZwxODfaiowwP3kfPmD26T\",\"client_secret\": \"kftzuAAquSWq_tol2biwXb0TzHcvZeZPQaByE3J-AOv5ZNVDxG-6qLqquU1fkQ15\"}"

- PERMISSIONS includes
1. castingassistance 
    "get:actors",
    "get:movies"
2. castingdirector
    "delete:actor",
    "get:actors",
    "get:movies",
    "patch:actor",
    "patch:movie",
    "post:actor"
3. executiveproducer
    "delete:actor",
    "delete:movie",
    "get:actors",
    "get:movies",
    "patch:actor",
    "patch:movie",
    "post:actor",
    "post:movie"

### JWT TOKENS
1. casting_assistant_token: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZQSkpuQmhjdUNTS3JxVm5ZX055VyJ9.eyJpc3MiOiJodHRwczovLzN6MTJrLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGI4ZjVkYzBiN2ViN2M1Nzk3MWUyMzAiLCJhdWQiOiJodHRwOi8vMTI3LjAuMC4xOjUwMDAiLCJpYXQiOjE2ODk4NDc0ODMsImV4cCI6MTY4OTkwNzk2MywiYXpwIjoiY0V1WGFRNU5vanBad3hPRGZhaW93d1Aza2ZQbUQyNlQiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.YoLo5Xm0pmlGpJsEc0p21PWtTrdu-MQg1jBWLqj6d2zK52pLGlqrRkgA2jk2eXBhCER_NcjcRJrBw4muU3BeUhHxAK3ZR5bpvNuFtaHQ45X_ZtjclUouLgZRsZyefpw5KW3hgk_N0UzgqfCEN3CzqSf_Q32UnoNLi9FpQ6R8BMqosTFIEpAOezXwLtUudzKJhXsSBL5uUiOcOvu8YNpDLaljAf6PUg5qRYA2Flyx2u7SeOZC_5zcMaGKFVa-qIeso1Jh9fhkOmV3hdr6z_A9l-1X3iNxUcWiIec6tLUHLzqQPOX5x2BSH68ubpONZT83FryPtyPi_QftnfuV_9d3hA

2. casting_director_token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZQSkpuQmhjdUNTS3JxVm5ZX055VyJ9.eyJpc3MiOiJodHRwczovLzN6MTJrLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGI4ZjYzZTBjNDA2Y2RhZGQ0MzE3Y2UiLCJhdWQiOiJodHRwOi8vMTI3LjAuMC4xOjUwMDAiLCJpYXQiOjE2ODk4NDc0ODksImV4cCI6MTY4OTkwNzk2OSwiYXpwIjoiY0V1WGFRNU5vanBad3hPRGZhaW93d1Aza2ZQbUQyNlQiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiXX0.obm39eJwKfce8-gPSfbPz0OjEYudmoW0ax_WAiyJG5ufyQxAViQpxBVj24DK-rdkE4RpKusmEXHApfjVYOTlALNTlwmtQiwMcjcrc9yN_g49jdLU_iR5l_a165slfnWhANhZtNi4CmsXMytsGiT4wKXE7Ijn9kfNKz1jpCayhTTAF8ZuplBBOOGisy7biD10ma4y1evBgT6GQosocBdL3vTeIQql6CwLvQdHK_w85jG0IFaq5hs0OJdKG_lI9eeAv-LcbfTL23DlEk4CZVTjtTjivxCdOIWgxP-FoLkO18f4vIBPiF8zfeb-DFtxEvLbBZeeluPMu8judCoAcnOdcQ

3. executive_producer_token:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkZQSkpuQmhjdUNTS3JxVm5ZX055VyJ9.eyJpc3MiOiJodHRwczovLzN6MTJrLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGI4ZjY4ZDBjNDA2Y2RhZGQ0MzE3ZDMiLCJhdWQiOiJodHRwOi8vMTI3LjAuMC4xOjUwMDAiLCJpYXQiOjE2ODk4NDcwNjIsImV4cCI6MTY4OTkwNzU0MiwiYXpwIjoiY0V1WGFRNU5vanBad3hPRGZhaW93d1Aza2ZQbUQyNlQiLCJndHkiOiJwYXNzd29yZCIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3IiLCJwYXRjaDptb3ZpZSIsInBvc3Q6YWN0b3IiLCJwb3N0Om1vdmllIl19.Hs4-lUHtndJyABhP2l6mhpxP2UVpI2mocylHwZJvoDkYfKUJdEExpmEAlMFX7j3dxEWROBoBKLXzU0k6fgleEyJ6DkByulhYD74kzm-LNUD4GuCGgckHljxroBdfhIAnRa_lEciAJRVxtnWgPceu4wkUNptRTmbA9PB8hlaElQSf_dlMenwq2qwh0w-K8dfKbTbmr3t0r_If4rsCJF-ooliouQMQ5zJERnNCmYPofJEUx52_5IHJ6fUHCzFDBqgSklCQnVqkBQe2l6EsY5CIN12usHUBHJjHBEIztTUFJKqJT2ST7TduQPc1fJhaZXw_kEwYWQBbrFjht5qouXW1nA



### AUTHORS
Abdulaziz I. Hijazi