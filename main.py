import json

def format_time(seconds):
    """Convert seconds to SRT time format (HH:MM:SS,MMM)."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def json_to_srt(json_file, srt_file):
    """Convert word-level JSON timestamps to SRT format."""
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)

    index = 1
    with open(srt_file, "w", encoding="utf-8") as file:
        for entry in data:
            for word_info in entry["words"]:
                start_time = format_time(word_info["start"])
                end_time = format_time(word_info["end"])
                text = word_info["word"]
                file.write(f"{index}\n{start_time} --> {end_time}\n{text}\n\n")
                index += 1

# Usage
json_to_srt("time.json", "time_srt.srt")
print(f"SRT file saved to time_srt.srt")
