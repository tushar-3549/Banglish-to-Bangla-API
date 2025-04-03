### Banglish to Bangla API

This FastAPI project provides an API to convert Banglish (Romanized Bengali) text to Bangla (Bengali script) using a SQLite database. It supports adding, updating, deleting, and retrieving translations, as well as transliterating Banglish to Bangla based on a pre-defined mapping.

### Features

    - Convert Banglish text to Bangla using a transliteration function.
    - Store Banglish to Bangla translations in a SQLite database.
    - Manage translations with RESTful API endpoints (CRUD operations).
    - Mapping of Banglish words to Bangla characters stored in a JSON file.

### Tech Stack

    - Python (for backend logic)
    - FastAPI (for creating the API)
    - SQLite3 (for the database)
    - Pydantic (for data validation)
    - JSON (for mapping Banglish to Bangla)
    - SQLite for storing translations

Installation & Setup
- Create the Mapping JSON File
Create a mapping.json file that maps Banglish words to Bangla words. The format of the file should be:
```
{
    "ami": "আমি",
    "khub": "খুব",
    "valo": "ভাল"
}
```
This mapping file will be used to transliterate the Banglish text into Bangla.

***Start the FastAPI server by running:***

`uvicorn main:app --reload`

- This will run the application on `http://127.0.0.1:8000`


- Add a New Translation

Endpoint: POST 

***Request Body:***
```
{
    "banglish": "ami khub valo"
}
```

***Response:***
```
    {
        "banglish": "ami khub valo",
        "bangla": "আমি খুব ভাল"
    }
```
- Translate Banglish to Bangla

- Endpoint: GET 

  Example Request: GET 

***Response:***
```
    {
        "id": 1,
        "banglish": "ami khub valo",
        "bangla": "আমি খুব ভাল"
    }
```


**/docs**
![image](https://github.com/user-attachments/assets/1f96d8d1-43fb-4ebe-8198-147549ff40ba)

**Final API**
```

  {
    "id": 1,
    "banglish": "kemon acho tumi",
    "bangla": "কেমন acho তুমি"
  },
  {
    "id": 3,
    "banglish": "ami valo asi",
    "bangla": "আমি ভালো আসি"
  },
  {
    "id": 4,
    "banglish": "amar nam tushar",
    "bangla": "আমার নাম তুষার"
  },
  {
    "id": 5,
    "banglish": "ami ekjon software engineer",
    "bangla": "আমি একজন সফটওয়্যার ইঞ্জিনিয়ার"
  },
  {
    "id": 6,
    "banglish": "ami dhaka savar thaki",
    "bangla": "আমি ঢাকা সাভার থাকি"
  },
  {
    "id": 7,
    "banglish": "cholo khelte jai",
    "bangla": "চলো খেলতে যাই"
  },
  {
    "id": 8,
    "banglish": "shuvo sokal",
    "bangla": "শুভ সকাল"
  },
  {
    "id": 9,
    "banglish": "dhonnobad dekha hobe",
    "bangla": "ধন্যবাদ দেখা হবে"
  },
  {
    "id": 10,
    "banglish": "tumi ki khaicho",
    "bangla": "তুমি কি খেয়েছো"
  },
  {
    "id": 11,
    "banglish": "tumi kise poro",
    "bangla": "তুমি কীসে পড়ো"
  },
  {
    "id": 12,
    "banglish": "rosogolla",
    "bangla": "রসগোল্লা"
  }
]
```
