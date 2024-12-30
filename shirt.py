from sys import exit, argv
from PIL import Image, UnidentifiedImageError, ImageOps


def shirt(input_p: str, output_shirt: str)-> None:
    """_Given a name or path of an  input image , paste a cs50 shirt on it and save it as output shirt_

    Args:
        input_p (str): _A name or path to an image_
        output_shirt (str): _A name or path to an image_
    """
    cs_shirt = open_image("shirt.png")
    input_s =fit_input_image_to_cs_size(input_p=input_p, cs_shirt=cs_shirt)


    mask = cs_shirt.split()[-1]
    input_s.paste(cs_shirt, mask=mask)
    input_s.save(output_shirt)
    input_s.close()
    cs_shirt.close()



def fit_input_image_to_cs_size(input_p: str, cs_shirt: str)-> None:
    """_Given an input shirt and second shirt , get the size of the second shirt and fit input shirt to that size_

    Args:
        input_p (str): _Path to shirt you wish to fit_
        cs_shirt (str): _Path to shirt whose size you will copy_
    """
    cs50_shirt = open_image(cs_shirt)
    cs50_shirt_size = cs50_shirt.size
    input_shirt: Image = open_image(input_p)
    return ImageOps.fit(input_shirt, size= cs50_shirt_size)




def open_image(image_file: str)-> Image:
    """_Given a name or  path to an image , open it and return the Image_

    Args:
        image_file (str): _Name or path to image to open_

    Returns:
        Image: _Opened image_
    """

    try:
            input_image = Image.open(image_file, 'r')
    except FileNotFoundError:
            exit(f"Could not find {image_file}")
    except AttributeError:
            return image_file
    except UnidentifiedImageError:
            exit(f"{image_file} could not be opened")
    else:
            return input_image


def main()->None:
    argv_len = len(argv)

    if argv_len > 3:
        exit("Too many command-line arguments.")
    elif argv_len < 3:
        exit("Too few command-line arguments.")
    else:
        input_image ,output_image= argv[1:]

        input_ext, output_ext = map(lambda value: value.split(".")[-1] ,argv[1:])

        if input_ext.lower() not in ["jpg", "jpeg", "png"] or output_ext not in ["jpg", "jpeg", "png"]:
            exit("Unsupported format")

        if input_ext.lower() != output_ext.lower():
            exit("File extension do not match")
        shirt(input_p= input_image, output_shirt=output_image)

if __name__ == "__main__":
    main()
