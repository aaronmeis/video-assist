# Video Thumbnail Extractor

A utility for converting any video file into a series of random high-resolution thumbnails.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Extract 20 random thumbnails from a video file:

```bash
python extract_thumbnails.py path/to/your/video.mp4
```

Or specify a custom number of thumbnails:

```bash
python extract_thumbnails.py path/to/your/video.mp4 30
```

**Note:** The video filename in the script (`video-5df6800d-31d4-4fe7-976f-dcd992dd48f6.mp4`) is just an example default. You can use this utility with any video file by specifying the path as shown above.

## Output

Thumbnails will be saved in the `thumbnails/` directory as high-quality PNG files. Each filename includes:
- Sequential number
- Frame number
- Timestamp (minutes:seconds)

Example: `thumbnail_01_frame_012345_05m23s.png`
