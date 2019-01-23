# Network Topology with Mininet

This repository is a lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Overview

1. We will give you a Python code (`example.py`) that includes an example network topology of Mininet
2. We will get you a figure illustrating a new topology you should generate
3. Copy the necessary function code from `example.py` and write your Python code (`topology.py`) to generate this topology

---
## Tasks

> **NOTICE:** Please follow this [slides](Tasks.pdf) for detail.

1. Environment Setup
2. Example of Mininet
3. Topology Generator
4. Measurement

### File Structure

```bash
Network_Topology/               # This is ./ in this repository
|--- src/                       # Folder of source code
     |--- topo/                 # The figure of topology
          |--- topo0.png
          |--- topo1.png
          |--- topo2.png
     |--- expect/               # Expected result using iPerf
          |--- topo0
          |--- topo1
          |--- topo2
     |--- out/                  # Output files
          |--- .gitkeep         # For keeping this folder
     |--- example.py            # Example code of using Mininet
     |--- topology.py           # Your program should be here!
|--- LICENSE
|--- README.md
|--- .gitignore                 # For ignoring useless files
```

---
## References

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributor

* [David Lu](https://github.com/yungshenglu)

---
## License

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)