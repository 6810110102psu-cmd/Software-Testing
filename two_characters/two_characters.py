def alternate(s):
    unique_chars = list(set(s))
    max_length = 0

    # ทดลองจับคู่ตัวอักษรทีละ 2 ตัว
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            c1 = unique_chars[i]
            c2 = unique_chars[j]

            # กรอง string ให้เหลือเฉพาะตัวอักษร 2 ตัวนี้
            filtered = [ch for ch in s if ch == c1 or ch == c2]

            # ตรวจสอบว่าเป็น alternating หรือไม่
            is_alternating = True
            for k in range(1, len(filtered)):
                if filtered[k] == filtered[k - 1]:
                    is_alternating = False
                    break

            # ถ้าเป็น alternating ให้อัปเดตความยาว
            if is_alternating:
                max_length = max(max_length, len(filtered))

    return max_length