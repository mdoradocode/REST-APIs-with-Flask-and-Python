##What is a REST API?
    ##Is a way of thinking about how a web server responds to your requests, that responds with more than data, it responds with resources

##Example: Item Resouces
    ##GET /item/chair
    ##POST /item/chair
    ##PUT /item/chair
    ##Delete /item/chair
    ##Item List Resouces
    ##GET /items
##REST APIs are "Stateless", meaning that the API doesnt know about anything except the current request, it doesnt know what data the server has, any of the previous requests, or if an object exists
    ##Example:
    ##User logs into something like twitter
    ##The Web server doesnt know that the user is logged in (it cant remember a state)
    ##So, the web app must send enough data with each interaction so that the server will associate and identify the user in every request