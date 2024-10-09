import paramiko

# 服务器信息
hostname = '192.168.2.108'
port = 22  # 默认 SSH 端口
username = 'root'
password = '123123'

# 创建 SSH 客户端对象
ssh = paramiko.SSHClient()

# 自动添加未知主机的密钥
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 连接服务器
    ssh.connect(hostname, port, username, password)

    # 执行部署脚本命令，假设部署脚本为 deploy.sh
    command = 'ls /'
    stdin, stdout, stderr = ssh.exec_command(command)

    # 输出执行结果
    print("标准输出：")
    print(stdout.read().decode())
    print("标准错误：")
    print(stderr.read().decode())

finally:
    # 关闭连接
    ssh.close()