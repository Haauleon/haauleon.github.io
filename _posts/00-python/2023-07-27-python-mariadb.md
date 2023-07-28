---
layout:        post
title:         "Python3 | 安装 MariaDB 报错"
subtitle:      "Python MariaDB pip 安装失败，缺少 MariaDB 配置"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 安装mariadb
尝试安装：      
```
pip install mariadb==1.1.6
```

报错信息如下：       
```
Collecting mariadb==1.1.6 (from -r requirements.txt (line 4))
  Downloading mariadb-1.1.6.tar.gz (83 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 83.7/83.7 kB 786.7 kB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [30 lines of output]
      /bin/sh: 1: mariadb_config: not found
      Traceback (most recent call last):
        File "/home/yzy/Spider/huburpa-openapi-sdk-python/venv/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/home/yzy/Spider/huburpa-openapi-sdk-python/venv/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
        File "/home/yzy/Spider/huburpa-openapi-sdk-python/venv/lib/python3.8/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 118, in get_requires_for_build_wheel
          return hook(config_settings)
        File "/tmp/pip-build-env-5t7tb8t1/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 341, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=['wheel'])
        File "/tmp/pip-build-env-5t7tb8t1/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 323, in _get_build_requires
          self.run_setup()
        File "/tmp/pip-build-env-5t7tb8t1/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 487, in run_setup
          super(_BuildMetaLegacyBackend,
        File "/tmp/pip-build-env-5t7tb8t1/overlay/lib/python3.8/site-packages/setuptools/build_meta.py", line 338, in run_setup
          exec(code, locals())
        File "<string>", line 27, in <module>
        File "/tmp/pip-install-bieap9cp/mariadb_6d036fdf79ee4d468d6984064993b589/mariadb_posix.py", line 62, in get_config
          cc_version = mariadb_config(config_prg, "cc_version")
        File "/tmp/pip-install-bieap9cp/mariadb_6d036fdf79ee4d468d6984064993b589/mariadb_posix.py", line 28, in mariadb_config
          raise EnvironmentError(
      OSError: mariadb_config not found.

      This error typically indicates that MariaDB Connector/C, a dependency which
      must be preinstalled, is not found.
      If MariaDB Connector/C is not installed, see installation instructions
      If MariaDB Connector/C is installed, either set the environment variable
      MARIADB_CONFIG or edit the configuration file 'site.cfg' to set the
       'mariadb_config' option to the file location of the mariadb_config utility.

      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
```

解决步骤：     
```
sudo apt install mariadb-server
sudo apt-get install libmariadb3 libmariadb-dev
```

再次安装 pip install mariadb==1.1.6 时如果还会提示 Connector/C 的版本不符的问题，可以尝试安装低版本的 mariadb：          
```
pip install mariadb==1.0.11
```

最后安装成功：      
```
> pip show mariadb
Name: mariadb
Version: 1.0.11
Summary: Python MariaDB extension
Home-page: https://www.github.com/mariadb-corporation/mariadb-connector-python
Author: Georg Richter
Author-email: None
License: LGPL 2.1
Location: /usr/local/lib/python3.8/site-packages
Requires:
Required-by:
```