import base64
f=open(r'D:\bl\git\dzml\static\logo.png','rb') #�����Ʒ�ʽ��ͼ�ļ�
ls_f=base64.b64encode(f.read()) #��ȡ�ļ����ݣ�ת��Ϊbase64����
print ls_f
f.close()