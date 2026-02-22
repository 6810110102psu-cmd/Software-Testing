## Algorithm 
1. Initialize deletions = 0
กำหนดตัวแปร deletions เพื่อเก็บจำนวนครั้งที่ต้องลบ
2. Loop from index 1 to len(s) - 1
วนลูปตรวจสอบตัวอักษรตั้งแต่ตำแหน่งที่ 1 ถึงตัวสุดท้าย
3. If s[i] == s[i-1], increment deletions
ถ้าตัวอักษรตำแหน่งปัจจุบันเหมือนกับตัวก่อนหน้า เพิ่มจำนวนการลบ
4. Return deletions
ส่งค่าจำนวนครั้งที่ต้องลบกลับ