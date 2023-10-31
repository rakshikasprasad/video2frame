import streamlit as st
import cv2
import os

# Define the function to extract images from video
def get_fun(filename):
    # Read the video from specified path
    cam = cv2.VideoCapture(filename)
    # print(cam.get(cv2.CAP_PROP_FPS))
    info1 = st.empty()
    info1.text("Frame Rate  :  " + str(cam.get(cv2.CAP_PROP_FPS)))
    x = int(cam.get(cv2.CAP_PROP_FPS))
    try:
        # creating a folder named data
        if not os.path.exists('inputs'):
            os.makedirs('inputs')
    # if not created then raise error
    except OSError:
        st.warning('Error: Creating directory of data')
    # frame
    currentframe = 0
    x2=0
    while (True):
        # reading from frame
        ret, frame = cam.read()
        if ret:
            if currentframe % x == 0:
                # if video is still left continue creating images
                x1 = int(currentframe / x)
                name = './inputs/frame' + str(x1) + '.jpg'
                x2 = x2 + 1
                #         print ('Creating...' + name)
                # writing the extracted images
                cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break
    #     ret,frame = cam.read()
    info2 = st.empty()
    info2.text("No. of frame/Images  :  " + str(x2))
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    st.success("Images extracted successfully.\n\nSaved to Video Images folder.")



# Create the Streamlit application
st.title("Video to Frames  for image reconstruction")
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])
if uploaded_file is not None:
    # Save the uploaded file to disk
    with open("temp.mp4", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract images from the video file
    get_fun("temp.mp4")

    # Remove the temporary file from disk
    os.remove("temp.mp4")
