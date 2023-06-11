from skimage.metrics import structural_similarity as ssim

def compare_favicon_similarity(fav1, fav2, similarity_threshold):
    img1 = fav1.convert('RGB')
    img2 = fav2.convert('RGB')
    similarity_index = ssim(img1, img2, multichannel=True)
    return similarity_index >= similarity_threshold