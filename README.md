# vector-search-quickstart
Demonstrate https://www.mongodb.com/docs/atlas/atlas-vector-search/tutorials/vector-search-quick-start

### Setup .env file
Requires a MongoDB Atlas cluster URI and Voyage AI API Key
```bash
MONGODB_URI='mongodb+srv://<username>:<password>@<cluster-url>.mongodb.net/'
VOYAGE_API_KEY='<API Key from dashboard.voyageai.com>'
```

### Setup Python3 environment

```
python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## Run demos

### Create Vector Index in MongoDB Atlas
```bash
python3 vector-index.py
# Expected output...

# New search index named vector_index is building.
# Polling to check if the index is ready. This may take up to a minute.
# vector_index is ready for querying.
```

### Run Vector Search query for the term "time travel"
```json
python3 atlas-vector-search-quick-start.py
# Expected output...
{
  "plot": "A reporter, learning of time travelers visiting 20th century disasters, tries to change the history they know by averting upcoming disasters.",
  "title": "Thrill Seekers",
  "score": 0.926971435546875
}
{
  "plot": "At the age of 21, Tim discovers he can travel in time and change what happens and has happened in his own life. His decision to make his world a better place by getting a girlfriend turns out not to be as easy as you might think.",
  "title": "About Time",
  "score": 0.9267120361328125
}
{
  "plot": "An officer for a security agency that regulates time travel, must fend for his life against a shady politician who has a tie to his past.",
  "title": "Timecop",
  "score": 0.9235687255859375
}
{
  "plot": "Hoping to alter the events of the past, a 19th century inventor instead travels 800,000 years into the future, where he finds humankind divided into two warring races.",
  "title": "The Time Machine",
  "score": 0.9228668212890625
}
{
  "plot": "After using his mother's newly built time machine, Dolf gets stuck involuntary in the year 1212. He ends up in a children's crusade where he confronts his new friends with modern techniques...",
  "title": "Crusade in Jeans",
  "score": 0.9228515625
}
```

### Run example of Vector Embedding with Voyage AI
```bash
python3 vector-embedding.py
# Expected output...
[-0.009375211782753468, 0.07005840539932251, -0.014787266962230206, 0.07431986182928085, .....]
```