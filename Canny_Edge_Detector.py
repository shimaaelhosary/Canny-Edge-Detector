import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

img = plt.imread("image.jpg")
img = rgb2gray(img)


sigma = 1
mask = np.empty((5, 5))

for row in range(-2, mask.shape[0]-2):
    for col in range(-2, mask.shape[0]-2):
        x = 1 / (2.0 * np.pi * sigma**2)
        mask[row+2][col+2] = x * (np.exp(- (row**2 + col**2)/(2 * sigma**2)))


gauss = np.zeros(img.shape)
for i in range(2, img.shape[0]-2):
    for j in range(2, img.shape[1]-2):
        temp = img[i-2:i+3, j-2:j+3]
        gauss[i, j] = np.sum(temp * mask)

rGx = np.zeros(gauss.shape)
rGy = np.zeros(gauss.shape)
magnitude = np.zeros(gauss.shape)

Gx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

Gy = np.array([[1,  2, 1], [0, 0, 0], [-1, -2, -1]])

for r in range(1, gauss.shape[0]-1):
    for c in range(1, gauss.shape[1]-1):
        a = gauss[r-1:r+2, c-1:c+2]
        rGx[r, c] = np.sum(a * Gx)
        rGy[r, c] = np.sum(a * Gy)

for r in range(1, gauss.shape[0]-1):
    for c in range(1, gauss.shape[1]-1):
        magnitude[r, c] = np.sqrt(rGx[r, c]**2 + rGx[r, c]**2)

D = np.arctan(rGy / rGx)
        
M, N = magnitude.shape
Z = np.zeros((M, N), dtype=np.int32)
for i in range(M):
    for j in range(N):
        where = np.round(D[i, j])
        try:
            if where == 0:
                if (magnitude[i, j] >= magnitude[i, j - 1]) and \
                        (magnitude[i, j] >= magnitude[i, j + 1]):
                    Z[i, j] = magnitude[i, j]
            elif where == 90:
                if (magnitude[i, j] >= magnitude[i - 1, j]) and \
                        (magnitude[i, j] >= magnitude[i + 1, j]):
                    Z[i, j] = magnitude[i, j]
            elif where == 135:
                if (magnitude[i, j] >= magnitude[i - 1, j - 1]) and \
                        (magnitude[i, j] >= magnitude[i + 1, j + 1]):
                    Z[i, j] = magnitude[i, j]
            elif where == 45:
                if (magnitude[i, j] >= magnitude[i - 1, j + 1]) and \
                        (magnitude[i, j] >= magnitude[i + 1, j - 1]):
                    Z[i, j] = magnitude[i, j]
        except IndexError as e:
                
            pass
        
        
plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.title("Gray Image")
plt.axis('off')


plt.subplot(222)
plt.imshow(gauss , cmap="gray")
plt.title("After Gaussian Filter")
plt.axis('off')


plt.subplot(223)
plt.imshow(magnitude, cmap="gray")
plt.title("Magnitude of Gaussian Image")
plt.axis('off')


plt.subplot(224)
plt.imshow(Z, cmap="gray")
plt.title("After Non-maximum Suppression")
plt.axis('off')
plt.show()
