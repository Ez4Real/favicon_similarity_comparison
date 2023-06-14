import numpy as np
from skimage.metrics import structural_similarity as ssim
from utils import original_favicons, phishing_favicons

def compare_favicon_similarity(fav1, fav2, similarity_threshold):
    # Resize the images to a consistent size
    width, height = 32, 32
    img1_resized = fav1.resize((width, height))
    img2_resized = fav2.resize((width, height))

    img1 = np.array(img1_resized.convert('RGB'))
    img2 = np.array(img2_resized.convert('RGB'))
    similarity_index = ssim(img1, img2, win_size=3, multichannel=True, channel_axis=-1)
    return similarity_index >= similarity_threshold, similarity_index


# Set threshold
similarity_threshold = 0.8

# Compare favicons using image similarity
match_found = False
for i, (original_favicon, original_filename) in enumerate(original_favicons):
    for j, (phishing_favicon, phishing_filename) in enumerate(phishing_favicons):
        similar, index = compare_favicon_similarity(original_favicon, phishing_favicon, similarity_threshold)
        if similar:
            match_found = True
            print(f"-!- Icons Similarity Found - {round(index * 100)}%: Original {original_filename} and Phishing {phishing_filename} -!-")
            
if not match_found:
    print("--- No hash matches found. ---")
