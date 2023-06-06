# CLI Calculator

This is a simple four-function calculator with an interactive command line interface.

## Technology Choice

The calculator application is written in Python, a widely used and beginner-friendly programming language. Python provides a simple syntax and a rich ecosystem of libraries, making it suitable for developing command-line applications quickly.

## Getting Started

### Prerequisites

- Python 3.10 or later

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/erikc96/calculator-assessment.git
   ```

2. Navigate to the project directory:


    ```shell
    cd calculator-cli
    ```

    (Optional) Create a virtual environment:

    ```shell

    python3 -m venv venv
    ```

    Activate the virtual environment:

    ```shell

    source venv/bin/activate
    ```

    Install the dependencies (can skip until dependencies are added!):

    ```shell
    pip install -r requirements.txt
    ```

3. Start the calculator app:

    ```shell

        python3 main.py
    ```

    or 

    ``` shell
        make run
    ```

    or

    ``` shell

        make docker-run
    ```


### Usage

    The calculator app provides a prompt where you can enter mathematical expressions. The supported operations are addition, subtraction, multiplication, and division. The following keys can be used for specific operations:

        + for addition
        - for subtraction
        * for multiplication
        / for division
        c to clear the calculator
        ! to toggle the sign of the current value
        = to calculate the result

    Here's an example usage:

    ```shell
    > 5 + 4
    9
    > 10 * 2
    20
    > -5 / 2
    -2.5
    > c
    0
    ```

    To quit the calculator app, simply press Ctrl+C or enter q at the prompt.

### Testing

    The calculator app includes a test suite to ensure the correctness of its operations. To run the tests, use the following command:

    ```shell
    make test
    ```

    The tests are implemented using the Python unittest framework.

    Feel free to explore and modify the code to suit your needs. If you encounter any issues or have any questions, please don't hesitate to reach out.
