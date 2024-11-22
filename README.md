# Single command run 
`docker build -t zj-challenge . && docker run zj-challenge`

# Local setup
For this we expect you to have python > 3.11 installed on your machine

1. Install poetry on your local machine
2. `cd src`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `poetry install`

To check if the project is set up correctly run `python3 app/main.py`. 
You should see `Uvicorn running on http://0.0.0.0:8080` in your output logs. 

# Challenges

## Challenge 1
Make tests in the `src/app/tests/donuts_test.py` pass, 
for that please implement the functions in `src/app/api/donuts.py` with NotImplementedError exception.

**Constraint** - please don't change tests in `src/app/tests/donuts_test.py`


## Challenge 2
Make the test in `src/app/tests/recommender_test.py` pass by improving the test itself.

**Constraint** - please don't change the implementation of `src/app/api/recommender.py`

## Challenge 3 (AI Challenge)
Improve `src/app/chain/marketing_chain.py` according to the following requirements:
- return a list of 5 names from the function `create_new_donut_name`
- one of the names should contain a substring with the exact name of one of the existing donuts. 
  Example existing donuts [Raised, Old Fashioned], 
  generated names [New Age Classics, Sugar Addiction, VW for Villy Wonka, Old Fashioned Smokey]. 
  'Old Fashioned Smokey' has a substring 'Old Fashioned' which is the name of one of the existing donuts.
- Extra challenge: make the chain more resilient to errors   

