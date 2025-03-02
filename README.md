# Flight Price Prediction & Comparison Tool

The **Flight Price Prediction & Comparison Tool** is a Python application aimed at fetching, comparing, and predicting the price of flight tickets based on real-time data provided by the **Skyscanner API**. The tool enables users to:
- Retrieve airline fares for a given origin, destination, and departure date.
- Contrast prices offered by various airlines to choose the lowest.
- Foresee the cost of flights to a particular destination according to past trends.
This project is perfect for travelers who want to maximize their flight reservations with data-driven decisions and predictive modeling.

## Features
- **Retrieve Flight Prices**: Fetches real-time flight price data from the Skyscanner API.
- **Compare Airline Prices**: Evaluates ticket prices across multiple airlines for the same route and date.
- **Automated Testing**: Implements unit tests using `pytest` to ensure code reliability and correctness.
- **Dependency Management**: Uses a `requirements.txt` file for easy installation of necessary libraries.

## Project Structure
The project consists of several key files that contribute to its functionality:

### `project.py`
This is the main script containing the core functionalities of the tool. It includes:
1. `get_flight_prices(origin, destination, date)`: 
   - Fetches real-time ticket prices for a given route and date using the Skyscanner API.
   - Returns a structured list of available flights with details on prices and airlines.

2. `compare_airlines(prices_list, airlines)`: 
   - Takes a list of flight prices and airline names as input.
   - Compares the prices and returns the cheapest option.

3. `predict_future_prices(destination, months_ahead)`: 
   - Analyzes historical price trends for a given destination.
   - Utilizes statistical methods or machine learning algorithms to estimate future ticket prices.

4. `main()`: 
   - Acts as the entry point of the program.
   - Handles user inputs, calls the respective functions, and displays the results in a user-friendly format.

### `test_project.py`
This file contains unit tests for validating the correctness of the functions in `project.py`. It includes:
- `test_get_flight_prices()`: Ensures that API responses return valid price data.
- `test_compare_airlines()`: Verifies that the comparison function correctly identifies the lowest price.
- `test_predict_future_prices()`: Checks the predictive model’s output for consistency.

### `requirements.txt`
A list of required Python libraries necessary for the project, including:
- `requests` 
- `pytest` 
- `pandas` 
- `sklearn` 

## Example Usage
Below are sample outputs from the tool when searching for flights:

### Example 1: Flight Search from MIA to JFK
```
Enter your name: Nicolas
Enter origin airport code: MIA
Enter destination airport code: JFK
Enter departure date (YYYY-MM-DD): 2025-03-02

Nicolas, here are the available flight options:
+---------+--------+
| Airline | Price  |
+---------+--------+
| B6      | $252.23|
| B6      | $338.23|
| B6      | $396.28|
| B6      | $396.28|
+---------+--------+
```

### Example 2: Flight Search from AMS to CDG
```
Enter your name: Amir
Enter origin airport code: AMS
Enter destination airport code: CDG
Enter departure date (YYYY-MM-DD): 2025-04-10

Amir, here are the available flight options:
+---------+--------+
| Airline | Price  |
+---------+--------+
| AZ      | $166.17|
| AZ      | $166.17|
| AZ      | $166.17|
| AZ      | $166.17|
| AZ      | $175.62|
+---------+--------+
```
These outputs demonstrate how the tool retrieves and formats flight price information.

## Design Choices
### 1. **Use of Skyscanner API**
We chose Skyscanner’s API because it provides real-time and historical flight price data, ensuring accuracy and reliability in predictions and comparisons.

### 2. **Function-Based Modular Approach**
- Breaking down the project into individual functions (`get_flight_prices`, `compare_airlines`, `predict_future_prices`) ensures maintainability and readability.
- Allows for easier testing and debugging.

### 3. **Testing Strategy**
- Ensuring robust unit testing with `pytest` minimizes errors and enhances reliability.
- We focused on edge cases, such as handling API failures and missing data scenarios.

## How to Run the Project

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run the program:
   ```sh
   python project.py
   ```

3. Run tests:
   ```sh
   pytest test_project.py
   ```

## Future Improvements
- Implement a graphical user interface (GUI) for better usability.
- Expand support to additional flight search APIs for better coverage.
- Enhance the predictive model using deep learning techniques.
- Add a caching mechanism to optimize API calls and reduce costs.


The **Flight Price Prediction & Comparison Tool** is a practical and efficient way for travelers to make informed flight booking decisions. With its modular design, predictive capabilities, and testing framework, this project demonstrates the power of data-driven decision-making in travel planning.