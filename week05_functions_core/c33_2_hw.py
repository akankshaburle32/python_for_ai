# c33:       que 2:
## make_config(**settings) jo saari settings ek dict ke roop mein print kare.

def make_config(**settings):
    print(settings)
    for key, value  in settings.items():
        print(f"{key}:{value}")

make_config(movie = "Rajasahab", type = "horror")