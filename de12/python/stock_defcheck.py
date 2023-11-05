import cv2

# Load images
img1 = cv2.imread('xbp/de12/images/sony_exceptFigure_1.png')
img2 = cv2.imread('xbp/de12/images/sony_real.png')

# Convert images to grayscale
img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Calculate absolute difference between the two images
diff = cv2.absdiff(img1_gray, img2_gray)

# Apply threshold to identify significant differences
thresh = 30
diff[diff < thresh] = 0
diff[diff >= thresh] = 255

# Find contours of significant differences
contours, hierarchy = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw rectangles around the differences
for contour in contours:
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Display the output image with differences highlighted
cv2.imshow('Output', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()