**GeoLocation Utility**

A command-line utility for retrieving geographical coordinates (latitude and longitude) from city/state names or zip codes using the Open Weather Geocoding API.

**Features**
* Retrieve latitude and longitude for:
* City and state combinations (e.g., "Madison, WI")
* Zip codes (e.g., "12345")
* Handle multiple locations in a single command
* Provides user-friendly error messages for invalid inputs

**Requirements**
Python 3.6 or higher
requests library
pytest for testing

**Installation**

Clone the repository:

```
git clone <repository_url>
cd geoloc-util
```

**Install the required packages:**

You can install the required packages using pip. It's recommended to do this in a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
pip install requests pytest
```

**Configuration**

1. Set up API Key:

The utility uses the Open Weather Geocoding API. You can use the provided API key for testing:

```
API_KEY = 'f897a99d971b5eef57be6fafa0d83239'
```

Ensure this is set in your geoloc_util.py file.

**Usage**

To run the utility from the command line, use the following format:


```
python geoloc_util.py --locations "City, State" "Zip Code"
```

**Examples**

To get the coordinates for Madison, WI:

```
python geoloc_util.py --locations "Madison, WI"
```

To get the coordinates for multiple locations:

```
python geoloc_util.py --locations "Madison, WI" "12345" "Chicago, IL" "90210"
```

**Running Tests**

To ensure everything is functioning as expected, run the tests using pytest:

```
pytest test_geoloc_util.py
```

**Test Examples**

Valid city/state input
Valid zip code input
Multiple valid locations
Invalid location input
