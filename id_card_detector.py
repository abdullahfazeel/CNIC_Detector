import cv2
import matplotlib.pyplot as plt

# Function to detect and replace ID card with a black rectangle
def detect_and_replace_id_card(image_path):

    # Read the image
    img = cv2.imread(image_path)

    #show original Image
    plt.imshow(img)
    plt.title('Original Image')
    plt.show()


    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Otsu's thresholding to obtain a binary image
    _, binary_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours to find the largest rectangular contour (presumed ID card)
    max_contour = max(contours, key=cv2.contourArea)

    # Create a mask for the ID card region
    mask = np.zeros_like(binary_img)
    cv2.drawContours(mask, [max_contour], 0, 255, thickness=cv2.FILLED)

    # Replace the ID card region with a black rectangle
    img[mask == 255] = [0, 0, 0]




    plt.subplot(1, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('ID Card Mask')

    plt.show()

# Provide the path to your image
image_path = '/content/drive/MyDrive/CNIC/cnic.jpg'

# Call the function
detect_and_replace_id_card(image_path)
