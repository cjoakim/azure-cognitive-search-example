# azure-cognitive-search-example

<p align="center" width="95%">
  <img src="img/azure-cognitive-search-example.png">
</p>

---

## Project Overview 

This github project demonstrates an Azure Solution based on **Azure Cognitive Search**,
and other Azure PaaS services, including:
- **Azure Cognitive Service** - used by the Search service to invoke **built-in** skills
- **Azure Storage** - stores documents to be indexed
- **Azure CosmosDB** w/SQL API  - stores documents to be indexed
- **Azure Function** implemeting a HTTP-triggered **Custom Cognitive Skill**

Two **Indexes** are created in this project:
- **Airports** - US Airports in JSON format in CosmosDB.  Simple text-based indexing, minimal dependent PaaS services.
- **Documents** - PDF, image, and HTML files in Storage.  Advanced document-cracking, knowledge mining, and AI. 

**Python 3** is used as the sole programming language for this project, to do the following:
- Generate Azure Cognitive Search JSON **schemas**
- Upload a curated set of documents to Azure Storage; see the documents/ directory
- Upsert JSON Airport documents to CosmosDB; see file data/us_airports.json
- Implement the Custom Cognitive Skill Azure Function; see the FunctionApp/ directory
- Invoke the **REST API** of the **Azure Cognitive Search**, using the **requests** library

Python 3 was chosen because it is cross-platform, practical, and is commonly used by Data Scientists.

The initial implementation of this project focuses on the **bash** shell and the **linux** 
and **macOS** operating systems, but **Windows** and **PowerShell** support will be added
in the near future.

---

## Provisioning Azure Resources

In Azure, you can provision resources in one of several ways, including the **Azure Portal**,
**ARM templates**, the **az CLI**, and others.  Some scripts using the **az CLI** are
provided in this repo; I recommend using the Azure Portal Web UI to create the others.

The az CLI scripts are located in directory **automation/az/**.
Edit file **config.sh** in this directory per your desired Azure Region, Resource Group,
and resource names.

### Azure Cognitive Search

```
$ ./search.sh create
```

### Azure Cognitive Service

```
$ ./cognitive.sh create
```

### Azure Storage

```
$ ./storage.sh create
```

### Azure CosmosDB

Create a Cosmos/SQL account.  Then add a **dev** database, with an **airports** container
specifying a partition key field named **/pk**.

### Azure Function

Create a Function app with your tool-of-choice; Visual Studio, Visual Studio Code, or the
**func** command line tools.  See https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Ccsharp%2Cbash

I used the **func** command line tools; see the section below titled **Custom Skill Azure Function**.

---

## Environment Variables

Using environment variables is a "best practice" for handling configuration values on your
workstation.  Using these enables you to eliminate "hard coded" configuration values and
secrets.

This project uses the following environment variables; some example values are shown.
These values can be obtained from Azure Portal once your above resources have been created;
see the keys section of the UI for each service.

Please use your own name and not cjoakim for your Azure Services!

```
AZURE_SUBSCRIPTION_ID= ... your Azure Subscription Id ...
AZURE_COSMOSDB_SQLDB_ACCT=cjoakimcosmossql
AZURE_COSMOSDB_SQLDB_KEY= ... secret ...
AZURE_COSMOSDB_SQLDB_URI=https://cjoakimcosmossql.documents.azure.com:443/
AZURE_SEARCH_STORAGE_ACCOUNT=cjoakimsearch
AZURE_SEARCH_STORAGE_KEY= ... secret ...
AZURE_SEARCH_STORAGE_CONNECTION_STRING= ... secret ...
AZURE_SEARCH_NAME=cjoakimsearch
AZURE_SEARCH_URL=https://cjoakimsearch.search.windows.net
AZURE_SEARCH_ADMIN_KEY= ... secret ...
AZURE_SEARCH_QUERY_KEY= ... secret ...
AZURE_SEARCH_COGSVCS_ALLIN1_KEY= ... secret ...
AZURE_FUNCTION_CUSTOM_SKILL_LOCAL=http://localhost:7071/api/TopWordsSkill
AZURE_FUNCTION_CUSTOM_SKILL_REMOTE=https://cjoakimsearchapp.azurewebsites.net/api/TopWordsSkill?code=...secret...
```

---

## Concepts

- [HTTP REST API](https://docs.microsoft.com/en-us/rest/api/searchservice/)
  - [HTTP Status Codes](https://docs.microsoft.com/en-us/rest/api/searchservice/http-status-codes)
  - [HTTP Status Codes; Explained as Dogs](https://httpstatusdogs.com)
  - [Python Requests Library; HTTP for Humans](https://requests.readthedocs.io/en/master/)
- [Indexes](https://docs.microsoft.com/en-us/azure/search/search-what-is-an-index)
  - A search index stores searchable content, called Documents, used for full text and filtered queries
- [Index from Storage](https://docs.microsoft.com/en-us/azure/search/search-blob-storage-integration)
- [Index from CosmosDB, and document "flattening"](https://docs.microsoft.com/en-us/azure/search/search-howto-index-cosmosdb)
- [Indexers](https://docs.microsoft.com/en-us/azure/search/search-indexer-overview)
  - An indexer in is a crawler that extracts searchable data and metadata from an external Azure data source and populates an index based on field-to-field mappings.
  - An indexer **cracks** binary documents (PDF, Word, Images, etc) to extract their text
- [Synonyms](https://docs.microsoft.com/en-us/azure/search/search-synonyms)
  - Synonyms in search engines associate equivalent terms
- [Skillsets](https://docs.microsoft.com/en-us/azure/search/cognitive-search-defining-skillset)
  - A skillset is an optional collection of cognitive skills used for AI enrichment of the indexed documents
- [Skills and Document Cracking](https://docs.microsoft.com/en-us/azure/search/cognitive-search-concept-intro)
- [Built-In Skills](https://docs.microsoft.com/en-us/azure/search/cognitive-search-predefined-skills)
- [Custom Skills](https://docs.microsoft.com/en-us/azure/search/cognitive-search-defining-skillset#add-a-custom-skill)

### JSON Schemas

#### Documentation

- [Index](https://docs.microsoft.com/en-us/rest/api/searchservice/create-index)
- [Datasource](https://docs.microsoft.com/en-us/rest/api/searchservice/create-data-source)

#### This Project

- [Datasource CosmosDB](schemas/datasource-cosmosdb-dev-airports.json)
- [Datasource Storage](schemas/datasource-azureblob-documents.json)
- [Airports Index](schemas/airports_index_v1.json)
- [Airports Indexer](schemas/airports_indexer_v1.json)
- [Documents Index](schemas/documents_index_v1.json)
- [Documents Indexer](schemas/documents_indexer_v1.json)
- [Documents Skillset](schemas/skillset_v1.json)
- [Synonyms](schemas/synonym_map_v1.json)

### Other Links

- [Azure Cognitive Search Overview](https://azure.microsoft.com/en-us/services/search/)
- [Azure Cognitive Search Documentation](https://docs.microsoft.com/en-us/azure/search/)
- [Data Types](https://docs.microsoft.com/en-us/rest/api/searchservice/supported-data-types)
- [API Versions](https://docs.microsoft.com/en-us/rest/api/searchservice/search-service-api-versions)
- [Postman HTTP Client UI](https://www.postman.com)
- [curl HTTP Client CLI program](https://curl.haxx.se/docs/httpscripting.html)

---

## Implementation and Execution

This project is implemented using shell scripts, python programming, and JSON files.

First, you'll need to clone this repository and create the python virtual environment
as shown here.

```
$ git clone https://github.com/cjoakim/azure-cognitive-search-example.git
$ cd azure-cognitive-search-example
$ mkdir tmp                      <-- some output files are written to the tmp/ directory
$ ./venv.sh create               <-- activate the python virtual environment
$ source bin/activate            <-- activate the python virtual environment
```

To create the **airports** Index run the following script.  The airports index does **not** 
require the Azure Cognitive Service, Azure Storage, Azure Function, but it does require Azure CosmosDB.

```
$ ./recreate_airports.sh
```

To create the **documents** Index, from Azure Storages blobs (PDFs, Images, html files) run the following script.
You'll also need to first create your Azure Function, as described below in section "Custom Skill Azure Function".
This index does **not** use CosmosDB, but it does use the other Azure PaaS services listed above.

```
$ ./recreate_documents.sh
```

**See each of these scripts for the details.  But essentially they create a datasource, an index, and and indexer
for each index after uploading the underlying documents to Azure Storage or Azure CosmosDB.  All of these
actions are done in code with Python, and interact with the Azure Search Service via the REST API.**

### The Python Code

- [base.py](base.py) - Implements the abstract BaseClass inherited by the other classes below
- [search-client.py](search-client.py) - Implements class SearchClient and invokes the Azure Cognitive Search REST API
- [storage-client.py](storage-client.py) - Implements class StorageClient and uploads the documents to Azure Storage
- [cosmos.py](cosmos.py) - Implements class CosmosClient and uploads US Airport documents to CosmosDB
- [schemas.py](schemas.py) - Used by class SearchClient to generate and load JSON Schemas from files
- [urls.py](urls.py) - Used by class SearchClient to create the many REST API URLs from dynamic parameters
- The tests/ directory - contains unit tests which use the **pytest** library

---

## Skillset

An optional **Skillset**, containing **Skills**, can be used in a **pipeline** by the Indexer to
augment the raw text extracted from the documents.  Skills can be either **built-in** or **custom**.

The Skillset in this project uses the following Skills in the pipeline; see file schemas/skillset_v1.json.
This Skillset pipeline greatly augments the raw extracted text, and transforms a simple **Search App**
into an AI-driven **Cognitive Search App**.

For example, PDF and other documents are **cracked** and their embedded text and images are further
analyzed for **Entity Recognition, Sentiment, Key Phrases, and Image Analysis**.

The implementations of **WebApiSkills** are up to you and are only limited by your creativity.
In this app, the WebApiSkill invokes the Azure Function to identify the top n-number of words
in the combined mergedText of the document (i.e. - document and image text). 

```
"@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
"@odata.type": "#Microsoft.Skills.Text.SentimentSkill",
"@odata.type": "#Microsoft.Skills.Text.KeyPhraseExtractionSkill",
"@odata.type": "#Microsoft.Skills.Vision.OcrSkill",
"@odata.type": "#Microsoft.Skills.Text.MergeSkill",
"@odata.type": "#Microsoft.Skills.Vision.ImageAnalysisSkill",
"@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",            <-- Custom Skill implemented as an Azure Function
"@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
```

### OCR, Image Analysis, and TopWords - Sample Outputs

The [OCR](https://docs.microsoft.com/en-us/azure/search/cognitive-search-skill-ocr) and 
[Image Analysis](https://docs.microsoft.com/en-us/azure/search/cognitive-search-skill-image-analysis)
built-in Skills are used to **crack** the indexed documents to extract their embedded text, 
as well as leveraging AI to recognize the contents of the image.  The **TopWords Custom WebApiSkill**
is implemented as an Azure Function


#### Of the above diagram

```
"imageDescription": [
  "{\"tags\":[\"diagram\"],\"captions\":[{\"text\":\"diagram\",\"confidence\":0.82125532627105713}]}"
],
"imageText": [
  "Azure Cognitive Search Example Concepts: - Paas - Datasource - Index - Indexer - Synonyms - Knowledge Mining - Built-in Skills Custom Skill - Custom Skills Function (HTTP) - Skillset - Search - Lookup O Cognitive Service ( Built-in Skills - OCR, etc. ) REST API HTTP Client Azure ( Console Program ) Cognitive Search Python Client CosmosDB Datasource ( loader program ) Azure Storage Explorer Blob Storage Datasource Python Client (PDFs, Images, Html, etc.) ( loader program ) Https://github.com/cjoakim/azure-cognitive-search-example"
],
"mergedText": " Azure Cognitive Search Example Concepts: - Paas - Datasource - Index - Indexer - Synonyms - Knowledge Mining - Built-in Skills Custom Skill - Custom Skills Function (HTTP) - Skillset - Search - Lookup O Cognitive Service ( Built-in Skills - OCR, etc. ) REST API HTTP Client Azure ( Console Program ) Cognitive Search Python Client CosmosDB Datasource ( loader program ) Azure Storage Explorer Blob Storage Datasource Python Client (PDFs, Images, Html, etc.) ( loader program ) Https://github.com/cjoakim/azure-cognitive-search-example \n",
"topwords": [
  "azure",
  "cognitive",
  "search",
  "datasource",
  "skills",
  "client",
  "program",
  "built-in",
  "custom",
  "http",
  "etc",
  "python",
  "loader",
  "storage",
  "example",
  "concepts:",
  "paas",
  "index",
  "indexer",
  "synonyms"
]
```

---

#### Of a UPS Truck

<p align="center" width="95%">
  <img src="documents/UPSWEB-800x533.jpg">
</p>

```
"imageDescription": [
  "{\"tags\":[\"outdoor\",\"truck\",\"road\",\"transport\",\"parked\",\"car\",\"front\",\"sitting\",\"side\",\"bus\",\"large\",\"street\",\"parking\",\"standing\",\"old\",\"green\",\"man\"],\"captions\":[{\"text\":\"a truck is parked on the side of a road\",\"confidence\":0.96122339571435267}]}"
],
"imageText": [
  "ups 150472 Worldwide Services Low Emission Hybrid Electric Vehicle USDOT 021800"
],
"mergedText": " ups 150472 Worldwide Services Low Emission Hybrid Electric Vehicle USDOT 021800 \n",
"topwords": [
  "ups",
  "150472",
  "worldwide",
  "services",
  "low",
  "emission",
  "hybrid",
  "electric",
  "vehicle",
  "usdot",
  "021800"
]
```

---

#### Of a Marathon Finish

<p align="center" width="95%">
  <img src="documents/sfny.jpg">
</p>

```
"imageDescription": [
  "{\"tags\":[\"person\",\"road\",\"outdoor\",\"sport\",\"street\",\"man\",\"walking\",\"holding\",\"woman\",\"people\",\"jumping\",\"young\",\"standing\",\"riding\",\"city\",\"playing\",\"player\",\"group\",\"ball\"],\"captions\":[{\"text\":\"Shalane Flanagan et al. walking down the street\",\"confidence\":0.7455881694062344}]}"
],
"imageText": [
  "B TATA CONSULTANCY SERVICES TATA TCS NEW FLANAGAN 2017 % WOR YORK CITY airbnb"
],
"mergedText": " B TATA CONSULTANCY SERVICES TATA TCS NEW FLANAGAN 2017 % WOR YORK CITY airbnb \n",
"topwords": [
  "tata",
  "consultancy",
  "services",
  "tcs",
  "new",
  "flanagan",
  "2017",
  "wor",
  "york",
  "city",
  "airbnb"
]
```

---

## Custom Skill Azure Function

Creating the Azure Function with the CLI tooling.

First, create the Function App, which will contain the Function(s):

```
az functionapp create \
  --resource-group AzureFunctionsQuickstart-rg \
  --os-type Linux \
  --consumption-plan-location eastus \
  --runtime python \
  --runtime-version 3.7 \
  --functions-version 2 \
  --name <APP_NAME> \
  --storage-account <STORAGE_NAME>
```

Then use the **func** utility to generate and deploy the Azure Function to the Function App.

```
$ func init --help
$ func init FunctionApp --worker-runtime python

$ cd FunctionApp

$ func new --name TopWordsSkill --template "HTTP trigger"

$ ./venv.sh    (with an empty requirements.in file)

  ... edit the generated TopWordsSkill/__init__.py file, which implements the Function ...

$ func start
Found Python version 3.8.5 (python3).
Azure Functions Core Tools (3.0.2912 Commit hash: bfcbbe48ed6fdacdf9b309261ecc8093df3b83f2)
Function Runtime Version: 3.0.14287.0
Hosting environment: Development
Now listening on: http://0.0.0.0:7071
Application started. Press Ctrl+C to shut down.

Functions:
	TopWordsSkill: [GET,POST] http://localhost:7071/api/TopWordsSkill
```

Invoke the HTTP Function, running locally, from another Terminal.

```
$ python search-client.py invoke_local_function pyf-onedrop.png
```

After you're satisfied with how the Function runs locally, deploy it to Azure:

```
$ func azure functionapp publish $app_name
  - or -
$ ./publish.sh
```

## Searching!

Finally, the purpose of an **Azure Cognitive Search** solution is to have the ability
to search the contents (i.e. - the Indices) in a fluent and accurate manner.

### Links

- [Simple Query Syntax](https://docs.microsoft.com/en-us/azure/search/query-simple-syntax)
- [Lucene Query Syntax](https://docs.microsoft.com/en-us/azure/search/query-lucene-syntax)

Examples are shown below...

### Searching and Lookup

```
$ python search-client.py search_index documents all
$ python search-client.py lookup_doc documents aHR0cHM6Ly9jam9ha2ltc2VhcmNoLmJsb2IuY29yZS53aW5kb3dzLm5ldC9kb2N1bWVudHMvMjAyMS1zdXBlci1jdWItYzEyNS1nYWxsZXJ5LTA0LTI0MDB4YXV0by5qcGc1
```


