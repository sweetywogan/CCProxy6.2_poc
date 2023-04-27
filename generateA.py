import os


def main():
    a_count = int(input("请输入'A'的数量: "))  # 获取用户输入的'A'的数量

    file_name = f"{a_count}个A.txt"  # 根据'A'的数量创建文件名
    file_path = os.path.join(os.getcwd(), file_name)  # 将文件路径设置为当前目录下的文件

    with open(file_path, "w") as f:  # 打开文件并写入相应数量的'A'
        f.write("A" * a_count)

    print(f"已成功创建名为 '{file_name}' 的文件，并写入 {a_count} 个 'A'。")


if __name__ == "__main__":
    main()