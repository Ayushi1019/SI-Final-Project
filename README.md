# ITIS 6177 System Integration Final Project Documentation

## Project Topic

The project was to consume third party vendor APIs provided by Microsoft Azure Cognitive Services. The project utilizes Azure's following Cognitive Services:
 * Entity Linking
 * Language Detection
 * PII
 * Question and Answers 

### Tech Stack
* Flask in Python
* Swagger

### Tools Required
* Postman
* Azure account
  
The proper API documentation can be found here: http://164.92.106.251:5000/api/docs/

You can test the APIs here too.

## Steps to run project on your system

To run the project,first of all create a virtual environment the project directory using the following commands:

```cd project-app```

 ```python -m venv venv```

 ```.\venv\Scripts\activate```

Once the virtual environment is activated you will see 'venv' written at the left side of the terminal.

After this. run the ```pip install -r requirements.txt``` to install all the required dependencies.

Now, create a ```.env``` file with the following variables:
* API_KEY = $$ AZURE API KEY
* LANG_RES = $$ ENDPOINT OF THE AZURE COGNITIVE SERVICE RESOURCE

At last, run ```python ./app.py ``` to run the flask app. The application will run on port ```5000```.

## Description for all the services used

All the services use Azure API_KEY as their headers. The following services are used in the project with their function and their request body.

### Entity Linking

Entity linking is one of the features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Entity linking identifies and disambiguates the identity of entities found in text. For example, in the sentence "We went to Seattle last week.", the word "Seattle" would be identified, with a link to more information on Wikipedia.

```entity_linking()``` function consumes the above service and have the following request body:
 ```
 {
  "kind": "EntityLinking",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975."
      }
    ]
  }
}
```

where ```language``` the abbreviation of the language used and ```text``` is the statement containing different entities.

The response is of the following format:
```
[
  {
    "name": "string",
    "url": "string",
    "data_source": "string",
    "matches": {
      "confidence_score": "string",
      "text": "string"
    }
  }
]
```
There can be multiple enitites with their data source, url and their matches based on the confidence score and text.

### Personally Identifiable Information (PII) detection

PII detection is one of the features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. The PII detection feature can identify, categorize, and redact sensitive information in unstructured text. For example: phone numbers, email addresses, and forms of identification.

```pii()``` function consumes the above service and have the following request body:

```
{
  "kind": "PiiEntityRecognition",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "Call our office at 312-555-1234, or send an email to support@contoso.com"
      }
    ]
  }
}
```
where ```language``` the abbreviation of the language used and ```text``` is the statement containing different pii entities.

The response is of the following format:
```
[
  {
    "category": "string",
    "confidence_score": "string",
    "text": "string"
  }
]
```

where ```category``` is the category of the identitified entity.

### Language Detection

Language detection is one of the features offered by Azure Cognitive Service for Language, a collection of machine learning and AI algorithms in the cloud for developing intelligent applications that involve written language. Language detection can detect the language a document is written in, and returns a language code for a wide range of languages, variants, dialects, and some regional/cultural languages.

```detect_language()``` function consumes the above service and have the following request body:

```
{
  "kind": "LanguageDetection",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "text": "Type statement in any language"
      }
    ]
  }
}
```
The response is of the following format:

```
{
  "detected_language": "string",
  "id": "string",
  "confidence_score": "string",
  "abbv": "string"
}
```

where ```detected_language``` is the language detected by the service along with its ```abbv``` and ```confidence_score```.


### Question Answering

Question answering provides cloud-based Natural Language Processing (NLP) that allows you to create a natural conversational layer over your data. It is used to find the most appropriate answer for any input from your custom knowledge base (KB) of information.

Question answering is commonly used to build conversational client applications, which include social media applications, chat bots, and speech-enabled desktop applications.

We can also use question answering without a knowledge base with the prebuilt question answering REST API, which is called via query-text. In this case, we provide question answering with both a question and the associated text records we would like to search for an answer at the time the request is sent.

```qa()``` function consumes the above service and have the following request body:

```
{
  "question": "How long does it takes to charge a surface?",
  "language": "en",
  "stringIndexType": "Utf16CodeUnit",
  "records": [
    {
      "id": "doc1",
      "text": "Power and charging.It takes two to four hours to charge the Surface Pro 4 battery fully from an empty state. It can take longer if you're using your Surface for power-intensive activities like gaming or video streaming while you're charging it"
    }
  ]
}
```
where ```records``` is a list of records in form of knowledge base(KB) to answer the following question asked.

The response is of the following format:

```
{
  "A": "string",
  "Q": "string"
}
```

where ```Q``` is the question asked and ```A``` is the answers given by the service based on the KB provided.










