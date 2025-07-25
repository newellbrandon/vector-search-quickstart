from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
from dotenv import load_dotenv  
import time
import os  
# Load environment variables from .env file  
load_dotenv(dotenv_path='.env')  
# Now you can access them  
mongodb_uri = os.getenv("MONGODB_URI")
if mongodb_uri is None:
    raise ValueError("MONGODB_URI environment variable not set. Please set it in the .env file.")
# Connect to your Atlas deployment
client = MongoClient(mongodb_uri)

# Access your database and collection
database = client["sample_mflix"]
collection = database["embedded_movies"]

# Create your index model, then create the search index
search_index_model = SearchIndexModel(
  definition={
    "fields": [
      {
        "type": "vector",
        "path": "plot_embedding",
        "numDimensions": 1536,
        "similarity": "dotProduct",
        "quantization": "scalar"
      }
    ]
  },
  name="vector_index",
  type="vectorSearch"
)

result = collection.create_search_index(model=search_index_model)
print("New search index named " + result + " is building.")

# Wait for initial sync to complete
print("Polling to check if the index is ready. This may take up to a minute.")
predicate=None
if predicate is None:
  predicate = lambda index: index.get("queryable") is True

while True:
  indices = list(collection.list_search_indexes(result))
  if len(indices) and predicate(indices[0]):
    break
  time.sleep(5)
print(result + " is ready for querying.")

client.close()
