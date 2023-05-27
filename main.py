import os
import requests
#import 
print('欢迎使用Minecraft 开服工具Linux 分支版\n 作者:JingJian 感谢KeyKeyMaker的技术支持!')
#欢迎
print('是否已安装Java? y/n')
java_c = input('>')
#Java 测试
if java_c == 'n':
	print('java 8/18')
	javaver_c = input('>')
	if javaver_c == '8':
		output = os.popen('sudo apt install openjdk-8-jdk -y').readlines()
		print(output)
		print('完成')
	elif javaver_c == '18':
		output = os.popen('sudo apt install openjdk-18-jdk -y').readlines()
		print(output)
		print('完成')
#安装Java
print('是否安装核心？ y/n')
coreInstall_c = input('>')
if coreInstall_c == 'y':
	print('请输入核心下载链接')
	url = input('>')
	save_name = 'server.jar'
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
	}
	response = requests.head(url, headers=headers)
	file_size = response.headers.get('Content-Length')
	if file_size is not None:
	    file_size = int(file_size)
print('文件大小:', file_size, 'B')
print('是否初次启动核心？y/n')
startupCore_c = input('>')
if startupCore_c == 'y':
	print('请输入最大内存M')
	xmx = input('>')
	print('请输入最小内存M')
	xms = input('>')
	#当前文件路径
	file_create = open("start.sh", "x")
	#创建文件
	f = open("start.sh", "w")
	f.write("java -server -XX:+UseG1GC  -Xmx"+ xmx +"-Xms"+ xms +"-jar server.jar nogui")
	f.close()
	output = os.popen('./start.sh').readlines()
	print(output)
	print('请修改文件EULA')
