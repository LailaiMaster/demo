
#http://blog.csdn.net/zhengxiangwen/article/details/55805700

#进入.py脚本所在目录

 #这里是解释器的位置
 cd Steamspider/&&/Users/mac/anaconda3/envs/python36/bin/scrapy crawl c5-s


#执行.py中定义的项目example，并指定日志文件，其中nohup....&表示可以在后台执行，不会因为关闭终端而导致程序执行中断。
#nohup scrapy crawl example >> example.log 2>&1 &