def caesarCipher(s, k):
    result = []
    k = k % 26  # ลดค่า k ให้อยู่ในช่วง 0-25

    for ch in s:
        # กรณีเป็นตัวอักษรพิมพ์เล็ก
        if 'a' <= ch <= 'z':
            new_char = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)

        # กรณีเป็นตัวอักษรพิมพ์ใหญ่
        elif 'A' <= ch <= 'Z':
            new_char = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
            result.append(new_char)

        # กรณีไม่ใช่ตัวอักษร
        else:
            result.append(ch)

    return ''.join(result)