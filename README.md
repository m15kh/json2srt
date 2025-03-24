# json2srt

A simple Python utility that converts JSON files with word-level timestamps to SRT subtitle format.

## Description

json2srt takes a JSON file containing speech segments with word-level timing information and converts it to the widely-supported SRT subtitle format. Each word becomes an individual subtitle entry in the output file.

## Requirements

- Python 3.6 or higher

## Example Input

The JSON file (e.g., `time.json`) must follow a structure similar to this:

```json
[
    {
        "id": 0,
        "seek": 0,
        "start": 0.0,
        "end": 4.2,
        "text": "Take the biggest risk of your life right now",
        "tokens": [50365, 3664, ...],
        "temperature": 0.0,
        "avg_logprob": -0.1456975308093396,
        "compression_ratio": 1.5963302752293578,
        "no_speech_prob": 0.02118719182908535,
        "words": [
            { "word": "Take", "start": 0.0, "end": 0.933 },
            { "word": "the", "start": 0.933, "end": 1.4 },
            { "word": "biggest", "start": 1.4, "end": 2.1 },
            { "word": "risk", "start": 2.1, "end": 2.333 },
            { "word": "of", "start": 2.333, "end": 2.8 },
            { "word": "your", "start": 2.8, "end": 3.267 },
            { "word": "life", "start": 3.267, "end": 3.85 },
            { "word": "now", "start": 3.85, "end": 4.2 }
        ]
    },
    ...more entries...
]
```

Ensure your JSON input includes the `words` array with each word object containing the `word`, `start`, and `end` keys.

## Usage

1. Place your JSON file (e.g., `time.json`) in the same directory as `main.py`.
2. Run the script using Python:

   ```powershell
   py main.py
   ```

3. The script will generate an SRT file (e.g., `time_srt.srt`) in the same directory.

## Output

The generated SRT file contains an index, a time range in SRT time format (`HH:MM:SS,MMM`), and the corresponding word for each entry.

Example SRT output:

```
1
00:00:00,000 --> 00:00:00,933
Take

2
00:00:00,933 --> 00:00:01,400
the

3
00:00:01,400 --> 00:00:02,100
biggest

4
00:00:02,100 --> 00:00:02,333
risk

5
00:00:02,333 --> 00:00:02,800
of
```

