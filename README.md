- DT
- GBDT
- xgboost

- SVM

## xgboost在Mac下安装过程
- 创建安装目录
- git clone --recursive https://github.com/dmlc/xgboost **循环git操作**
- cd xgboost
- cp make/minimum.mk ./config.mk
- make -j4 **单线程，多线程需要安装最新版gcc**
- 安装python包
- cd python-package
- sudo python setup.py install
- 添加环境变量export PYTHONPATH=~/xgboost/python-package
- http://www.jianshu.com/p/76ff402a8b58
-