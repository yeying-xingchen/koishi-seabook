import subprocess

def check_docker():
    try:
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False
    
if __name__ == "__main__":
    print("正在安装 Koishi")
    print("安装方式：Docker")
    if check_docker():
        print("Docker 已安装")
        subprocess.run("docker run -p 5140:5140 koishijs/koishi")
    else:
        print("Docker 未安装，请您自行安装。")
    print("Koishi 安装完成")
