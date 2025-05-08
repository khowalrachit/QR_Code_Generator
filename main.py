import pyqrcode
s = input("Enter the url here : ")
url = pyqrcode.create(s)
url.png("myqr.png",scale = 6)