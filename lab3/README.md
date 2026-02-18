# Lab 03: Web Services & RESTful APIs

# Team Members:
    - Junsoo Kim <junsooki@usc.edu>
    - Mo Jiang

# Lab Questions:

## Question 1: Why are RESTful APIs scalable?
RESTful APIs are scalable because of its statelessness, which means that each request from a client to a server contains all the information needed to process the request and it is not affected by previous requests.

## Question 2: According to the definition of “resources” provided in the AWS article above, what are the resources the mail server is providing to clients?
According to the definition of "resources" provided in the AWS article above, the resources the mail server is providing to clients are the mail entries, and a mail.
- 

## Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
One common REST Method not used in our mail server is PUT. We could extend our mail server to use this method to update a specific field of a mail entry.

## Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve?
API keys are used for many RESTful APIs to identify the client making the request. They serve as a way to authenticate the client and authorize them to access the API.
