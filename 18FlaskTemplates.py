# To fake a database, the collection below will be our application's "data"
book_reviews = [
    {"book_title":"Confessions of a Python Programmer", "review_text":"A cautionary tale for all would-be programmers", "score":5, "id":"1"},
    {"book_title":"To Serve Man", "review_text":"Delicious recipes", "score":3, "id":"2"},
    {"book_title":"Pride and Prejudice", "review_text":"The pride is ok but the prejudice not so much", "score":4, "id":"3"},
]


# import what we need to use from the flask library
from flask import Flask, render_template, request 
from flask import request

# invoke the Flask class 
app = Flask(__name__) 



@app.route("/example")
def example_route():
    return render_template("example.html", adjective="fun")

@app.route("/example/<adjective>")
def route_adjective(adjective):
	return render_template("example.html", adjective=adjective)


# Create a route with the url reviews/ID, where ID is a route variable
# Render the show.html template, providing the review with the matching id
# In the show.html template, display the book_title and review_text information.
# The book_title should be an h2 element, while the review_text should be a paragraph element

@app.route("/reviews/<id>") # route to show a specific review
def review_id(id):
	# Find the id that matches in the review dictionnary
	for i in range(0, len(book_reviews)):
	    if book_reviews[i]['id'] == str(id):
	    	review = book_reviews[i]
	    	return render_template("18show.html", review=review)


# Create a route with the url "reviews"
# Render the index.html template, providing the entire list of reviews as a keyword argument
@app.route("/reviews")
def reviews():
	return render_template('index.html', book_reviews=book_reviews)



@app.route("/accept_data", methods=["POST"])
def handle_data_submission():
	request.form["property"] # request.form contains the POST data

# Create a route that accepts a POST request to "/reviews"
# The route should create a new_review dictionary that contains the attached request's data
# Add the new_review dictionary to the reviews list
# Return a dictionary as follows: { "status": 201, "data": reviews } as the response from this route
@app.route("/reviews", methods=['POST'])
def reviews_post():

	new_title = request.form.get('<book.title>')
	new_review = request.form.get('<book.review>')
	new_book_review = {'book_title': new_title, "new_review": new_review}
	book_reviews.append(new_book_review)
	
	return { "status": 201, "data": book_reviews }



 # Start the server listening for requests (leave at the bottom of the file)
if __name__ == '__main__':
    app.run(debug=True)