from django.db import models
from django.utils.html import format_html

# Create your models here.


class Assets(models.Model):
    '''
        status
            0: 表示关机
            1：表示运行

        frame
            1-2-3
            表示第一个机房第2排第三个机架

    '''
    STATUS=((0,'关机'), (1,'运行'))
    hostname            =   models.CharField(max_length=50, db_index=True, unique=True, verbose_name="主机名",default='')
    cpu_num             =   models.IntegerField(verbose_name="cpu核",default=0)
    cpu_model           =   models.CharField(max_length=100, verbose_name="cpu型号",default='')
    mem_total           =   models.CharField(max_length=3, default="8G", verbose_name="内存")
    disk                =   models.CharField(max_length=4, verbose_name="磁盘大小",default='')
    public_ip           =   models.CharField(max_length=32, default="", verbose_name="公网ip")
    private_ip          =   models.CharField(max_length=32, verbose_name="私有ip",default='')
    remote_ip           =   models.CharField(max_length=32, default="", verbose_name="远程ip")
    op                  =   models.CharField(max_length=32, default="", verbose_name="运维负责人")
    status              =   models.IntegerField(verbose_name="机器的状态0 | 1",choices=STATUS,default=0)
    os_system           =   models.CharField(max_length=32, verbose_name="操作系统",default='')
    service_line        =   models.CharField(max_length=32, verbose_name="所属业务线",default='')
    frame               =   models.CharField(max_length=32, verbose_name="机架",default='')
    remark              =   models.TextField(default="", null=True, verbose_name="备注")
    create_time         =   models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # create_time         =   models.DateTimeField(default="1970-1-1 09:00:00", verbose_name="创建时间")
    update_time         =   models.DateTimeField(auto_now=True,  verbose_name="修改时间")

    def __str__(self):
        return self.hostname

    class Meta:
        db_table = "assets"

    # def colored_name(self):
    #     return format_html(
    #         '<span style="color: #{};">{}</span>',
    #         'red',
    #         self.hostname,
    #     )
