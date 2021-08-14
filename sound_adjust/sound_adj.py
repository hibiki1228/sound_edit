import pydub
from pydub import AudioSegment
from pydub.utils import db_to_float, ratio_to_db
import glob, os

# fileの読み込み
# base_sound = AudioSegment.from_mp3("/sound_adjust/mp3_data/*.mp3")

# select 1
def cut_sound(start, end):
  sound = AudioSegment.from_mp3('mp3_data/祇園町3.mp3')
  separate_sound = sound[start:end]
  separate_sound.export('mp3_data/Muda_short.mp3')

# select 3
def change_volume(db):
  for filename in glob.glob( 'mp3_data/*.mp3' ):
    base_sound = AudioSegment.from_mp3(filename)
    ratio = db
    quiet_sound = base_sound + ratio_to_db(ratio)
    quiet_sound.export(filename, format='mp3')
  print("finished!")

# select 4
def change_format():
  for filename in glob.glob( 'm4a_data/*.m4a' ):
    a = filename[len("m4a_data")+1:][:-4] # ファイル名だけ取り出す ex) m4a_data/hoge.m4a → hoge
    os.system("ffmpeg -i m4a_data/{}.m4a -ab 256k mp3_data/{}.mp3".format(a,a))
  print("finished!")