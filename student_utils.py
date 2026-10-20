def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不对")
    name = parts[0].strip()
    score_str = parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError("成绩不是整数")
    if score < 0 or score > 100:
        raise ValueError("成绩超出 0~100")
    return {"name": name, "score": score}