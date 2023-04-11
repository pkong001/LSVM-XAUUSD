// Set up the request parameters
string url = "https://example.com/api";
string headers = "Content-Type: application/json";
string data = "{\"key1\":\"value1\",\"key2\":\"value2\"}";

// Send the request and get the response
string response;
int result = WebRequest("POST", url, headers, data, 5000, response);

// Check if the request was successful and print the response
if (result == 200) {
    Print("Response received:", response);
} else {
    Print("Request failed with error code:", result);
}
