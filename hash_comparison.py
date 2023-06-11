import imagehash
from utils import original_favicons, phishing_favicons

def compare_favicon_hashes(fav1, fav2):
    hash1 = imagehash.average_hash(fav1)
    hash2 = imagehash.average_hash(fav2)
    return hash1 == hash2


# Compare favicons using hashes
match_found = False
for i, original_favicon in enumerate(original_favicons):
    for j, phishing_favicon in enumerate(phishing_favicons):
        if compare_favicon_hashes(original_favicon, phishing_favicon):
            match_found = True
            print(f"Hash Match Found: Original Favicon {i+1} and Phishing Favicon {j+1}")

if not match_found:
    print("--- No hash matches found. ---")


# Compare favicons using image similarity
# similarity_threshold = 0.8
# for i, original_favicon in enumerate(original_favicons):
#     for j, phishing_favicon in enumerate(phishing_favicons):
#         if compare_favicon_similarity(original_favicon, phishing_favicon, similarity_threshold):
#             print(f"Similarity Found: Original Favicon {i+1} and Phishing Favicon {j+1}")