def alternatingCharacters(s):
    deletions = 0

    # เริ่มตรวจตั้งแต่ตัวที่ 2
    for i in range(1, len(s)):
        # ถ้าตัวปัจจุบันเหมือนตัวก่อนหน้า ต้องลบ 1 ตัว
        if s[i] == s[i - 1]:
            deletions += 1

    return deletions