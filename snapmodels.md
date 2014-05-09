SNAP APP

Why should you separate tables?  
The thing in each table is a "model"

for the Code for Progress application, we had six models:

(1) Student
(2) Application
(3) Recommender
(4) Recommendation
(5) Evaluator
(6) Evaluation


Table tool: diagrams.seaquail.net/

In your model you need?

Nullable in a table:  Is it able to be empty/nullable?
Type:  example--String(250) ...memory allocation

Integers, Floats, Strings, Booleans, DateTime
......

Objects:  


User:
	*Name (type: string)
	*Address (type: string)
	*Zip Code (type: integer)
	*Business (type: string)
		* Business (type: string)
	*EBT Balance (type: integer)
	*Calculator (type: integer)
		*Calculator Table (type: integer)

Calculator Model
	*BarCode (type: integer)
	 *Universal pricing

Business Model
		
		*Name (type: string)
		*Address (type: string)
		*Zip Code (type: integer)
		*Geocoding (type: float)
		*Business Model
			*Business Model
				*Grocery Store (type: string)
				*Liquor Store  (type: string)
				*Convenient Store (type: string)
				*Retail Store (type: string)
				*Specialty Store (type: string)
				*Warehouse Store
		*Food Type Model
			*Food Type Model (Do I need a separate table?)
				*Fruits (type: string)
				*Vegetables (type: string)
				*Meat (type: string)
		*Comment Model
			*Comment Model (type: string)
				*Comment
				*Date (type: datetime)
				*Time (type: datetime)


Comments:

	*How would I define a business type on their fruits, vegetables, and meat?
	*What is the state 



Who owns this data?
		*