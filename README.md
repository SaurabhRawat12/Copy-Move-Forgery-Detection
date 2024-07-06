# Copy Move Forgery Detection

The Copy Move Forgery Detection project aims to detect copy-move and splice forgeries in images using deep learning and diverse image representation methods.

## Project Structure

The project consists of the following main folders:

- **forgery_detect**: Contains the program code.
  - `Blocks.py`
  - `Container.py`
  - `features.py`
  - `forgery_detect.py`
  - `image_object.py`
  - `main.py`
- **test_images**: Should contain the images to be tested (each image as its original and fake copy).
- **output_images**: The directory where the images resulting from forgery detection will be placed.
- **image_dataset**: Contains some sample images to test.

## How to Test an Image

1. Move the image file to be tested to the `test_images` directory.

2. Open a Terminal or Shell.

3. Navigate to the `forgery_detect` directory.

4. Run the following command:

    ```bash
    python main.py
    ```

5. Enter the name of the image file when prompted, e.g., `horse_fake.png` (without quotes), which should be present in the `test_images` folder.

6. The output images will be generated in the `output_images` folder.

## Dependencies

Ensure you have the necessary Python packages installed. You can install the required packages using pip:

```bash
pip install -r requirements.txt
```
# Features

- **Forgery Detection**: Detects copy-move and splice forgeries in images using deep learning techniques.
- **Image Representation**: Utilizes diverse image representation methods for accurate forgery detection.
- **Output Generation**: Generates output images highlighting detected forgeries.

## Usage

- Place the images to be tested in the `test_images` directory.
- Run the main script (`main.py`) and follow the prompts to enter the image file name.
- Check the `output_images` folder for the results.

## Contributing

Feel free to fork this repository, create branches, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
