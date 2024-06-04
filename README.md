# openwrt的asu 的修改版本

[官方asu](https://github.com/openwrt/asu)

## 官方版本正提供服务的服务器

- [sysupgrade.openwrt.org](https://sysupgrade.openwrt.org)
- [asu.aparcar.org](http://asu.aparcar.org:8000)
- [asu.hauke-m.de](http://asu.hauke-m.de:8000)

## 快速执行服务的服务器

出于安全原因，每个构建都发生在容器内，以便一个构建不会影响另一个构建。为此，Podman 容器运行 API 服务，以便工作人员可以自己在容器内执行构建。

### 安装 Podman

debain/ubuntu:
```bash
sudo apt update
# 必要环境
sudo apt install podman
```

### 启动服务

```bash
# 获取
git clone https://github.com/Wuqiyang312/asu-wqyblog-cn.git
cd asu-wqyblog-cn
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate
# 安装 podman-compose
pip install podman-compose
export PUBLIC_PATH=$(pwd)/public
# 安装到工作容器中的 podman 套接字的绝对路径
export CONTAINER_SOCK=/run/user/1001/podman/podman.sock
podman-compose up -d
```

### 生产

对于生产，建议使用反向代理，例如 "nginx" 或 "caddy"。

#### 系统最低配置

- 2 GB RAM (4 GB recommended)
- 2 CPU cores (4 cores recommended)
- 50 GB disk space (200 GB recommended)
  
### 开发环境

#### 安装 Podman 和 可能需要的环境:

debain/ubuntu:
```bash
sudo apt update
# 必要环境
sudo apt install podman 
# 可能需要的环境 用于二次开发
sudo apt install pythom3 python3-pip python3-venv
```

#### 运行服务器

 > **提示**: 别忘了启动 redis

```bash
# 获取
git clone https://github.com/Wuqiyang312/asu-wqyblog-cn.git
cd asu-wqyblog-cn
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate
# 安装 poetry podman-compose
pip install poetry podman-compose
poetry install
poetry run flask run
```

#### 运行worker

```bash
# 安装到工作容器中的 podman 套接字的绝对路径
export CONTAINER_HOST=unix:///run/user/1001/podman/podman.sock
poetry run rq worker
```

### API

The API is documented via _OpenAPI_ and can be viewed interactively on the
server:

[https://sysupgrade.openwrt.org/ui/](https://sysupgrade.openwrt.org/ui/)
