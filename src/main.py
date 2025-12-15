import qrcode

def main(): 
    url = input("Enter a link:" )

    img = qrcode.make(url)
    img.save("qrcode.png")


if __name__ == "__main__": 
    main()