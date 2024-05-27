# Image Optimizer

This project is a Python script that converts PNG images to AVIF format.

## Requirements

Make sure you have Python 3.x installed on your system.

## Installation
Create and activate a virtual environment (optional but recommended):

```sh
python -m venv venv
```

- On Windows:

    ```sh
    .\venv\Scripts\activate
    ```

- On Linux:

    ```sh
    source venv/bin/activate
    ```

Install the dependencies:

```sh
pip install -r requirements.txt
```

## Usage

1. Place the PNG images you want to convert into the `png_input` folder.
2. Run the conversion script:

    ```sh
    python conversor.py
    ```

3. The converted images will be saved in the `avif_output` folder.


## Notes

- Make sure the `png_input` and `avif_output` folders exist or they will be created automatically when running the script.
- If you encounter any issues, ensure the dependencies are installed correctly and you are using an appropriate virtual environment.

## Contributions

Contributions are welcome. Please open an issue or a pull request to discuss any changes.

## License

This project is licensed under the MIT License.
