import whisper
import os
import json
import glob
import sys

VIDEO_DIR = os.path.expanduser("~/chinatown-ar-interviews")
TRANSCRIPT_DIR = os.path.join(VIDEO_DIR, "transcripts")
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

# Use medium model for good balance of speed and accuracy
print("Loading Whisper model (medium)...")
model = whisper.load_model("medium")

mp4_files = sorted(glob.glob(os.path.join(VIDEO_DIR, "*.MP4")))
print(f"Found {len(mp4_files)} MP4 files to transcribe.\n")

for i, mp4_path in enumerate(mp4_files):
    basename = os.path.splitext(os.path.basename(mp4_path))[0]
    txt_path = os.path.join(TRANSCRIPT_DIR, f"{basename}.txt")
    json_path = os.path.join(TRANSCRIPT_DIR, f"{basename}.json")

    # Skip if already transcribed
    if os.path.exists(json_path):
        print(f"[{i+1}/{len(mp4_files)}] SKIP (already done): {basename}")
        continue

    print(f"[{i+1}/{len(mp4_files)}] Transcribing: {basename}...")
    sys.stdout.flush()

    result = model.transcribe(mp4_path, language="en", verbose=False)

    # Save plain text
    with open(txt_path, "w") as f:
        f.write(result["text"])

    # Save detailed JSON with timestamps
    segments = []
    for seg in result["segments"]:
        segments.append({
            "start": seg["start"],
            "end": seg["end"],
            "text": seg["text"].strip()
        })

    with open(json_path, "w") as f:
        json.dump({
            "file": basename,
            "text": result["text"],
            "segments": segments
        }, f, indent=2, ensure_ascii=False)

    print(f"  Done. {len(segments)} segments, ~{len(result['text'].split())} words.")
    sys.stdout.flush()

print("\nAll transcriptions complete!")
