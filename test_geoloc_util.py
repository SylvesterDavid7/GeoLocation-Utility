import subprocess
import pytest

# Helper function to run the utility command
def run_geoloc_util(*locations):
    cmd = ['python', 'geoloc_util.py', '--locations'] + list(locations)
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result

def test_city_state_query():
    result = run_geoloc_util("Madison, WI")
    assert "Madison" in result.stdout
    assert "Lat" in result.stdout
    assert "Lon" in result.stdout

def test_zip_code_query():
    result = run_geoloc_util("12345")
    assert "Lat" in result.stdout
    assert "Lon" in result.stdout

def test_multiple_locations():
    result = run_geoloc_util("Madison, WI", "12345", "Chicago, IL", "90210")
    assert "Madison" in result.stdout
    assert "12345" in result.stdout
    assert "Chicago" in result.stdout
    assert "90210" in result.stdout

def test_invalid_input():
    result = run_geoloc_util("InvalidCity, XX")
    assert "No results found" in result.stdout

if __name__ == '__main__':
    pytest.main()
