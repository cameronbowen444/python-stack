# one to one realtionship: 
    # This item can only be assigned to this person
    # This peron can only be assigned to this item
    # EX: SSN can only be given to one person 
    # and only one person can have one designated SSN

# one to many realtionship:
    # One person can have many orders but those orders
    # belong to that one person
    # EX: One City is only in one State, but one State 
    # can have many Cities.

# many to many relationship:
    # Many orders can have many items and many items can
    # be given to many orders
    # EX: One User can have many Interest, one interest can be 
    # applied to many Users


# Normalization (3 Forms):
    # Why we use it? Organized and to Not Repeat Data
    
    # Form 1: First example is instead of using a full name line,
    # have a first_name and last_name line. Also even more important,
    # instead of having a line that is an address feild with entire address seperated
    # by commas, it's better to have another table with line of street/city/state and 
    # using an id like address_id for the other table to refer to that table.
    
    # Form 2: Having a movie table with a genre repeated muitiple times, instead have the 
    # movie table and another table that has an id with different movie genres and refer
    # to the other table with an id reteaded like 1, 1, 1, 4, 3, 4 instead of 
    # comedy, comedy, comedy, horror, family, horror

    # Form 3: Must pass form 1 and form 3 before even making it to form 3. 
    # Example would be having a table of books with just the title and publisher_id
    # and the publishers table woud have the name and rank and the id woud refer to both of these
    

