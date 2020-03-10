This project aims to perform the following functions:
1) Import images of receipts
2) Preprocess receipts for easier text reading using OpenCV Binarization, Thresholding, etc
3) Use Tesseract OCR to translate receipt contents into text string
4) Perform text processing to extract relevant information from text string
      -Can use spacy module to determine what are stopwords and what are keywords
      -Can use 'recipes' to automatically parse known vendor formats
      -Ca have user manually point to relevant information for new recipes
5) Perform validation on relevant information to ensure the following contents exist
      -Date and Time
      -Vendor and Location
      -Each item (and quantity), plus their cost
      -Total Cost
6) Import relevant information as separate columns into PostgreSQL database
7) Correlate information with financial and nutrition tracking (via item's macro/micronutrients)
8) Create a C# and Flutter frontend to visualize financial/nutrition tracking

Libraries involved are the following so far:
--PYTHON--
openCV
pytesseract
psycopg2
sqlalchemy

--C#--

--Dart--
Flutter
       
