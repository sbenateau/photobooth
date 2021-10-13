import cv2
import time

# select font (for timer)
font = cv2.FONT_HERSHEY_DUPLEX

# select the USB webcam
cam = cv2.VideoCapture("/dev/video2")

# open window in full screen
cv2.namedWindow("photo_booth", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("photo_booth", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# reduce buffer to limit latence trouble
cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# set larger resolution
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# get applied resolution
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

# set margin
width_margin = 128*2
height_margin = 72*2

# add a counter
img_counter = 0

first_timer = 3
second_timer = 2

def get_square_image(margin):
    test, frame = cam.read()
    frame_croped = frame[0:720, 280:1000]
    frame_border = cv2.copyMakeBorder(frame_croped, margin, margin, margin, margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
    return test, frame_croped

def timer_image(timer):
    start_time = time.time()
    while timer > 0:
        current_time = time.time()
        test, frame = get_square_image(margin)
        cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
        cv2.imshow("photo_booth", frame)
        if current_time - start_time > 1:
            timer -= 1
            start_time = current_time


# infinite loop to keep camera running
while True:
    # get image from camera
    ret, frame = get_square_image(72,72)
    # crop to work with squares
    frame = frame[0:720, 280:1000]
    if not ret:
        print("failed to grab frame")
        break

    # add borders and view frame
    frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
    cv2.imshow("photo_booth", frame)
    k = cv2.waitKey(1)

    # if key is pressed
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 8:
        print('you pressed enter')
        # ENTER pressed
        # prendre photo 1
        timer = first_timer
        start_time = time.time()
        while timer > 0:
            current_time = time.time()
            ret, frame = cam.read()
            frame = frame[0:720, 280:1000]
            frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
            cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
            cv2.imshow("photo_booth", frame)
            cv2.waitKey(1)
            if current_time - start_time > 1:
                timer -= 1
                start_time = current_time

        ret, frame = cam.read()
        frame = frame[0:720, 280:1000]
        photo = cv2.copyMakeBorder(frame, height_margin, height_margin - 72, width_margin + 128 - 72, width_margin - 128 * 2 + 72, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        photo1 = photo
        frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        cv2.putText(frame, "click", (int(width // 2 - 300 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
        cv2.imshow("photo_booth", frame)
        cv2.waitKey(500)

        # prendre photo 2
        timer = second_timer
        start_time = time.time()
        while timer > 0:
            current_time = time.time()
            ret, frame = cam.read()
            frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
            cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
            cv2.imshow("photo_booth", frame)
            cv2.waitKey(1)
            if current_time - start_time > 1:
                timer -= 1
                start_time = current_time

        ret, frame = cam.read()
        frame = frame[0:720, 280:1000]
        photo = cv2.copyMakeBorder(frame, height_margin - 72, height_margin, width_margin + 128 - 72, width_margin - 128 * 2 + 72, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        photo2 = photo
        frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        cv2.putText(frame, "click", (int(width // 2 - 300 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
        cv2.imshow("photo_booth", frame)
        cv2.waitKey(500)


        # prendre photo 3
        timer = second_timer
        start_time = time.time()
        while timer > 0:
            current_time = time.time()
            ret, frame = cam.read()
            frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
            cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
            cv2.imshow("photo_booth", frame)
            cv2.waitKey(1)
            if current_time - start_time > 1:
                timer -= 1
                start_time = current_time

        ret, frame = cam.read()
        photo = cv2.copyMakeBorder(frame, height_margin, height_margin - 72, width_margin - 128 * 2 + 72, width_margin + 128 - 72, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        photo3 = photo
        frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        cv2.putText(frame, "click", (int(width // 2 - 300 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
        cv2.imshow("photo_booth", frame)
        cv2.waitKey(500)

        # prendre photo 4
        timer = second_timer
        start_time = time.time()
        while timer > 0:
            current_time = time.time()
            ret, frame = cam.read()
            frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
            cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
            cv2.imshow("photo_booth", frame)
            cv2.waitKey(1)
            if current_time - start_time > 1:
                timer -= 1
                start_time = current_time

        ret, frame = cam.read()
        photo = cv2.copyMakeBorder(frame, height_margin - 72, height_margin, width_margin - 128 * 2 + 72, width_margin + 128 - 72, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        photo4 = photo
        frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
        cv2.putText(frame, "click", (int(width // 2 - 300 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
        cv2.imshow("photo_booth", frame)
        cv2.waitKey(500)


        # ecrire photo ensemble

        im_v1 = cv2.vconcat([photo1, photo2])
        im_v2 = cv2.vconcat([photo3, photo4])

        photo_finale = cv2.hconcat([im_v1, im_v2])

        cv2.imshow("photo_booth", photo_finale)
        cv2.waitKey(1)
        img_name = "cousinade_leard/cousinade_4_{}.png".format(current_time)
        cv2.imwrite(img_name, photo_finale)
        print("{} written!".format(img_name))
        time.sleep(5)
        img_counter += 1

    elif k%256 == 32:
        # SPACE pressed
        timer = first_timer
        start_time = time.time()
        while timer > 0:
            current_time = time.time()
            ret, frame = cam.read()
            frame = cv2.copyMakeBorder(frame, height_margin, height_margin, width_margin, width_margin, cv2.BORDER_CONSTANT,value=(255, 255, 255))
            cv2.putText(frame, str(timer), (int(width // 2 - 100 + width_margin),int(height // 2 + 100 + height_margin)), font, 7, (0, 0, 200), 10, cv2.LINE_AA)
            cv2.imshow("photo_booth", frame)
            cv2.waitKey(1)
            if current_time - start_time > 1:
                timer -= 1
                start_time = current_time

        ret, frame = cam.read()
        cv2.imshow("photo_booth", frame)
        cv2.waitKey(1)
        img_name = "cousinade_leard/cousinade_{}.png".format(current_time)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        time.sleep(5)
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
