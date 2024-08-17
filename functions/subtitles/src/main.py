import json

from youtube_transcript_api import YouTubeTranscriptApi

def subtitle_extract(url):
  url = url.split('/watch?v=')[1]
  subtitle_text = ""
  subtitles = YouTubeTranscriptApi.get_transcript(url)
  try:
    for subtitle in subtitles:
        subtitle_text += " " + subtitle.get("text", "")
    return subtitle_text
  except Exception as e:
    print(e)
    return ""

def main(context):
    context.log("Hello, Logs!")

    req = context.req
    body = json.dumps(req.body)
    context.log(body)
    subtitles = subtitle_extract(body)
    context.log(subtitles)

    return context.res.json(
        {
            "subtitles": subtitles
        }
    )
