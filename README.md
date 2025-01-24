# MP4 to GIF Converter 🎥➡️🎞️

A Python script to batch convert `.mp4` video files into animated GIFs using the **MoviePy** library. This tool supports custom time range selection and automatic output directory creation for seamless processing.

## Features

- **Batch Conversion**: Automatically converts all `.mp4` files in the input folder to `.gif` format.
- **Custom Time Range**: Specify start and end times (in seconds) to trim the GIFs.
- **Easy Setup**: Automatically creates the output folder if it doesn’t exist.
- **Quality Control**: Adjustable frame rate (`fps`) for optimized GIF quality and size.

## Requirements

- Python 3.x
- MoviePy (`pip install moviepy`)

## Usage

1. Place your `.mp4` files in the `source` folder.
2. Run the script to convert all videos to GIFs in the `output` folder.
3. Optionally, set `start_time` and `end_time` in seconds to customize GIF segments.

### Example

```python
input_folder = "source"  # Folder containing .mp4 files
output_folder = "output"  # Folder to save the GIFs
start_time = 5  # Start time in seconds
end_time = 50   # End time in seconds
```

## Run the Script

```bash
python script_name.py
```

## Output

GIFs are saved in the `output` folder with the same names as the original `.mp4` files.

Robot Execution :
![Demo](assets/demo.gif)
