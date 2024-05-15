# Credit Risk Model

This is a Python application for implementing a credit risk model that calculates PD (Probability of Default), EAD (Exposure at Default), and LGD (Loss Given Default) for a portfolio of obligors and facilities.

## Background

The credit risk model is designed to assess the risk associated with lending to obligors, such as companies or individuals. It calculates three key metrics:

- **PD (Probability of Default):** The likelihood that an obligor will default on their obligations.
- **EAD (Exposure at Default):** The amount that a lender is exposed to when an obligor defaults.
- **LGD (Loss Given Default):** The proportion of the exposure that the lender loses when an obligor defaults.

## Components

The application consists of several components:

- **REST API:** Provides an endpoint for calculating Risk Weighted Assets (RWA) of the portfolio based on a given assessment date.
- **Database:** Uses SQLite to store obligor and facility data, which is queried by the model calculator.
- **Model Calculator:** Implements the credit risk model logic to calculate PD, EAD, and LGD for the portfolio.
- **Testing:** Includes unit tests for the model calculator and REST API, as well as integration testing.
- **Data Validation:** Performs data validation within the model calculator to ensure data integrity.
- **Docker:** Containerizes the application for easy deployment.

## Usage

To use the application:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/cemtanrikut/credit-risk-model.git
    cd credit-risk-model
    ```

2. **Install the required dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```

3. **Set up the SQLite database:**

    ```bash
    python3 setup_database.py
    ```

4. **Run the application:**

    ```bash
    python3 main.py
    ```

5. **Access the REST API endpoint to calculate RWA for the portfolio:**

    Use a tool like Postman or cURL to send a POST request to the `/calculate_risk` endpoint with the following JSON payload:

    ```json
    {
        "risk_measure": "RWA",
        "assessment_date": "20211231"
    }
    ```

## Docker

To run the application using Docker:

1. **Build the Docker image:**

    ```bash
    docker build -t credit-risk-model .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -d -p 8000:8000 --name credit-risk-model-container credit-risk-model
    ```

3. **Access the REST API endpoint:**

    The API will be accessible at `http://localhost:8000`. You can use Postman or cURL to send requests as described above.

4. **Stop and remove the Docker container:**

    ```bash
    docker stop credit-risk-model-container
    docker rm credit-risk-model-container
    ```


## Directory Structure

```
project_root/
│
├── app/
│   ├── api.py
│   ├── calculator.py
│   ├── database.py
│   └── models.py
│   └── validation.py
│
├── data/
│   ├── Obligor.csv
│   └── Facility.csv
│
├── Dockerfile
├── requirements.txt
├── setup_database.py
├── credit_risk.db
└── main.py
```

## Testing

To run tests, use the following command:

```
pytest
```

This will execute all tests in the project.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
