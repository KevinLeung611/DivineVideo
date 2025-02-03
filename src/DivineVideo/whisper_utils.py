import whisper

model = whisper.load_model("turbo")
model.transcribe("data/audio/demo.wav")
