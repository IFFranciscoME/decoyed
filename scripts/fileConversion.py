
# --- ------------------------------------------------------------------- --- #
# -- 
# -- 
# --- ------------------------------------------------------------------- --- #

from pydub import AudioSegment

# files                                                                         
# src = "/Users/franciscome/git/iteralabs/pydub/files/LaChoraInterminable20240418.mp3"
# src = "/Users/franciscome/git/iteralabs/whisper.cpp/examples/python/Hubbi_Hollis_20min.m4a"

# convert wav to mp3                                                            

# --- ------------------------------------------------------------------- --- #
# --- ------------------------------------------------------------------- --- #

def convert_audio_file(
        input_filename:str,
        input_fileroute:str,
        output_format:str = "wav", 
        **kwargs):
    """
    Utility function to convert a file from accepted audio format into 
    .wav

    Args:
        input_file:
        output_format:
    
    kwargs:

        sample_rate: 16000
        ini_ts:0
        end_ts:30
        gain_effect: 6

    """

    in_file = input_fileroute + input_filename

    episode = AudioSegment.from_file(in_file, sample_width=2)

    short_episode = episode[
        kwargs["ini_ts"]:kwargs["end_ts"]*1000
    ].set_frame_rate(kwargs["sample_rate"]) + kwargs["gain_effect"]
    
    short_episode.export(input_fileroute + input_filename[:-3] + ".wav",
                         format=output_format)

