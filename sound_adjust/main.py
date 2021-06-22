import sound_adj as sa

def main():
  while True:
    query_num = int(input("[Sound Adjust Tool] What do you want?\ntype {0:quit, 1:cut sound,2:add audio segments, 3:change volume, 4:change format}\n"))

    # 0が入力されたとき
    if query_num == 0:
      print("[Sound Adjust Tool] Aborted!\n")
      break
    # 1が入力されたとき
    elif query_num == 1:
      print("[Sound Adjust Tool] Cut sound.\n")
      print("[Sound Adjust Tool] input time.\n")
      start, end = int(input()), int(input())
      sa.cut_sound(start, end)

      # which_data = int(input("[Sound Adjust Tool] type {0:back, 1:weathers, 2:winds3:waves\n"))
      # if which_data == 0:
      #   print("[Sound Adjust Tool] Back.\n")
      #   continue
      # elif which_data == 1:
      #   we.weather_all(data)
      # elif which_data == 2:
      #   we.winds_all(data)
      # elif which_data == 3:
      #   we.waves_all(data)
      # else:
      #   print("[Sound Adjust Tool] {} is not supported!\n".format(which_data))
      #   continue
    # 2が入力されたとき
    elif query_num == 2:
      print("[Sound Adjust Tool] Add audio segments.\n")
    # 3が入力されたとき
    elif query_num == 3:
      print("[Sound Adjust Tool] Cahnge volume.\n")
      print("[Sound Adjust Tool] Enter a magnification of sounds.\n")
      db = input()
      sa.change_volume(db)
    # 4が入力されたとき
    elif query_num == 4:
      print("[Sound Adjust Tool] Change format.\n")
      sa.change_format()
    # その他の値が入力されたとき
    else:
      print("[Sound Adjust Tool] {} is not supported!\n".format(query_num))

if __name__ == "__main__":
  main()