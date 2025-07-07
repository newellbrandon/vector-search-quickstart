from dotenv import load_dotenv 
import voyageai
import os  
# Load environment variables from .env file  
load_dotenv(dotenv_path='.env')  
# Now you can access them  
voyageai_api_key = os.getenv("VOYAGE_API_KEY")

vo = voyageai.Client(voyageai_api_key)
# This will automatically use the environment variable VOYAGE_API_KEY.
# Alternatively, you can use vo = voyageai.Client(api_key="<your secret key>")

result = vo.embed(["hello world"], model="voyage-3.5")

print(result.embeddings[0])