from flask import Flask
from flask import request # different from the one we use on jupyter Notebook!!

app = Flask(__name__) # invoke the Flask class


# define the first route, the home route
@app.route('/') 
def index(): # define the function that responds to the above route
  return 'Hello, World! Welcome to our review app' 

# defines the home route
@app.route('/reviews', methods=['GET', 'POST']) 
def reviews():
	if request.method =='GET':
		return {"response_code":200, "data":'Welcome to the home page!'}
	elif request.method == 'POST':
		return {"response_code":200, "data":'Add a new item to a collection'}

# To work with reviews identified by ID
@app.route('/reviews/<id>', methods=['GET', 'POST', 'DELETE'])
def unique_review(id):
	if request.method =='GET':
		return {"response_code":200, "data":'Show details of a specific item identified by its id'}
	elif request.method =='POST':
		return {"response_code":200, "data":'Update details of a specific item identified by its id'}
	elif request.method == 'DELETE':
		return {"response_code":200, "data":'Delete an item identified by its id'}

	
# To create a new review
@app.route('/reviews/new', methods=['GET'])
def new():
	return {"response_code":200, "data":'Show the form to create a new item'}

# to edit a review
@app.route('/reviews/<id>/edit', methods=['GET'])
def edit():
	return {"response_code":200, "data":'Show the form to update a specific item'}


if __name__ == '__main__':
    app.run(debug=True) # Start the server listening for requests

