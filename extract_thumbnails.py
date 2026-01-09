#!/usr/bin/env python3
"""
Extract 20 random high-resolution thumbnails from a video file.
"""

import cv2
import random
import os
import sys
from pathlib import Path


def extract_random_thumbnails(video_path, num_thumbnails=20, output_dir="thumbnails"):
    """
    Extract random thumbnails from a video file.
    
    Args:
        video_path: Path to the video file
        num_thumbnails: Number of thumbnails to extract (default: 20)
        output_dir: Directory to save thumbnails (default: "thumbnails")
    """
    # Check if video file exists
    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}")
        sys.exit(1)
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        sys.exit(1)
    
    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    duration = total_frames / fps if fps > 0 else 0
    
    print(f"Video info:")
    print(f"  Total frames: {total_frames}")
    print(f"  FPS: {fps:.2f}")
    print(f"  Resolution: {width}x{height}")
    print(f"  Duration: {duration:.2f} seconds")
    print(f"\nExtracting {num_thumbnails} random thumbnails...")
    
    # Generate random frame numbers
    if total_frames < num_thumbnails:
        print(f"Warning: Video has fewer frames ({total_frames}) than requested thumbnails ({num_thumbnails})")
        frame_numbers = list(range(total_frames))
    else:
        frame_numbers = sorted(random.sample(range(total_frames), num_thumbnails))
    
    # Extract frames
    extracted_count = 0
    for i, frame_num in enumerate(frame_numbers, 1):
        # Seek to the specific frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = cap.read()
        
        if ret:
            # Calculate timestamp for filename
            timestamp = frame_num / fps if fps > 0 else frame_num
            minutes = int(timestamp // 60)
            seconds = int(timestamp % 60)
            
            # Save frame as high-quality PNG
            filename = f"thumbnail_{i:02d}_frame_{frame_num:06d}_{minutes:02d}m{seconds:02d}s.png"
            filepath = os.path.join(output_dir, filename)
            
            # Save with high quality (PNG is lossless)
            cv2.imwrite(filepath, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])
            
            print(f"  [{i}/{num_thumbnails}] Extracted frame {frame_num} ({minutes:02d}:{seconds:02d}) -> {filename}")
            extracted_count += 1
        else:
            print(f"  Warning: Could not read frame {frame_num}")
    
    cap.release()
    
    print(f"\nSuccessfully extracted {extracted_count} thumbnails to '{output_dir}' directory")
    return extracted_count


if __name__ == "__main__":
    # Default video path
    video_path = "video-5df6800d-31d4-4fe7-976f-dcd992dd48f6.mp4"
    
    # Allow command line argument for video path
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    
    # Allow command line argument for number of thumbnails
    num_thumbnails = 20
    if len(sys.argv) > 2:
        try:
            num_thumbnails = int(sys.argv[2])
        except ValueError:
            print("Warning: Invalid number of thumbnails, using default: 20")
    
    extract_random_thumbnails(video_path, num_thumbnails)
