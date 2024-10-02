def linear_search(arr, target):
    """
    Pencarian linear untuk menemukan semua kemunculan target dalam list.
    
    :param arr: List elemen yang akan dicari.
    :param target: Elemen yang dicari.
    :return: List indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.
    """
    # Penanganan error: Pastikan arr adalah list
    if not isinstance(arr, list):
        raise ValueError("Argumen pertama harus berupa list.")
    
    # List untuk menyimpan semua indeks yang ditemukan
    indices = []
    
    # Melakukan pencarian linear
    for i, elem in enumerate(arr):
        if elem == target:
            indices.append(i)
    
    # Mengembalikan list indeks (kosong jika target tidak ditemukan)
    return indices


def is_sorted(arr):
    """
    Fungsi untuk memeriksa apakah list diurutkan secara ascending (menaik).
    :param arr: List yang akan diperiksa.
    :return: True jika list diurutkan, False jika tidak.
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def binary_search(arr, target):
    """
    Pencarian biner untuk menemukan semua kemunculan target dalam list yang terurut.
    List harus diurutkan secara ascending (menaik).
    
    :param arr: List yang sudah diurutkan untuk pencarian.
    :param target: Elemen yang dicari.
    :return: List indeks di mana target ditemukan, atau list kosong jika tidak ditemukan.
    """
    # Penanganan error: Pastikan arr adalah list dan terurut
    if not isinstance(arr, list):
        raise ValueError("Argumen pertama harus berupa list.")
    
    if not is_sorted(arr):
        raise ValueError("List harus diurutkan secara ascending untuk pencarian biner.")
    
    # List untuk menyimpan semua indeks yang ditemukan
    indices = []
    
    low, high = 0, len(arr) - 1
    
    # Melakukan pencarian biner
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            # Jika target ditemukan, kita cari di kedua arah (kiri dan kanan)
            indices.append(mid)
            
            # Cari kemunculan lain ke kiri dari mid
            left = mid - 1
            while left >= 0 and arr[left] == target:
                indices.append(left)
                left -= 1
            
            # Cari kemunculan lain ke kanan dari mid
            right = mid + 1
            while right < len(arr) and arr[right] == target:
                indices.append(right)
                right += 1
            
            break  # Keluar dari loop setelah menemukan semua kemunculan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    # Mengembalikan list indeks yang sudah ditemukan (kosong jika target tidak ditemukan)
    return indices

# Contoh penggunaan
if __name__ == "__main__":
    lst_random = [3, 1, 5, 7, 7, 9, 11, 3, 13, 15]
    
    # Tes Pencarian Linear (list acak)
    print("Hasil Pencarian Linear (acak):", linear_search(lst_random, 3))  # Output: [0, 7]
    
    # Tes Pencarian Biner (list terurut)
    lst_sorted = sorted(lst_random)  # Mengurutkan list
    print("Hasil Pencarian Biner (terurut):", binary_search(lst_sorted, 7))  # Output: [4, 5]
