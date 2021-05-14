import cv2
from pyzbar import pyzbar

def read_qrcodes(img):
    qrcodes = pyzbar.decode(img)
    for qrcode in qrcodes:
        x, y , w, h = qrcode.rect
        qrcode_info = qrcode.data.decode('utf-8')
        cv2.rectangle(img, (x, y),(x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, qrcode_info, (x + 6, y - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 2)
    return img

def main():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    while ret:
        ret, frame = cap.read()
        frame = read_qrcodes(frame)
        cv2.imshow('QR', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()