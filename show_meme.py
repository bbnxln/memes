from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    image_path = 'memes/meme.jpeg'
    img = Image.open(image_path)

    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print("warning bug")
    print("new bug")
    print("bug fixed")
    