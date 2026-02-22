def gridChallenge(grid):
    # เรียงตัวอักษรในแต่ละแถว
    sorted_grid = [''.join(sorted(row)) for row in grid]

    # จำนวนแถวและคอลัมน์
    rows = len(sorted_grid)
    cols = len(sorted_grid[0])

    # ตรวจสอบแต่ละคอลัมน์จากบนลงล่าง
    for c in range(cols):
        for r in range(1, rows):
            # ถ้าตัวอักษรด้านบนมากกว่าด้านล่าง แสดงว่าไม่เรียง
            if sorted_grid[r][c] < sorted_grid[r - 1][c]:
                return "NO"

    return "YES"