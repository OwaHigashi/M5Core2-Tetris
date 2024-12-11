def image_to_c_array(image_path, array_name="tetris_img"):
    # 画像ファイルをバイナリ読み込み
    with open(image_path, "rb") as f:
        data = f.read()
    
    # 配列のサイズ取得
    size = len(data)
    
    # Cコードの出力
    # 出力例:
    # const unsigned char tetris_img[34218] = {
    #     0xff, 0xd8, 0xff, 0xe0, ... };
    print(f"const unsigned char {array_name}[{size}] = {{")
    
    # 適度に改行を入れるため、1行あたり16バイト程度に区切る
    bytes_per_line = 16
    for i in range(0, size, bytes_per_line):
        line_data = data[i:i+bytes_per_line]
        # 各バイトを0xXX形式へ
        line_str = ", ".join(f"0x{b:02x}" for b in line_data)
        # 最後の行以外は末尾にカンマを入れておく
        print("    " + line_str + ("," if (i + bytes_per_line < size) else ""))
    
    print("};")

if __name__ == "__main__":
    # 例: "tetris.jpg"が同一ディレクトリにあると仮定
    image_to_c_array("tetris.jpg", "tetris_img")
