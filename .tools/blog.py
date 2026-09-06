# -*- coding: utf-8 -*-
"""
博客一键操作脚本（替代 VSCode tasks.json 里的内联命令，逻辑集中在此便于修改）。

子命令:
  build     hexo clean + generate              生成静态页面到 public/
  deploy    hexo deploy                         推送到 master 分支（GitHub Pages 显示）
  commit    git add -A; commit; push hexo       备份源码到 hexo 分支
  publish   commit -> build -> deploy          一键：备份源码 + 发布新页面
  preview   hexo server                          本地预览 http://localhost:4000
  check     .tools/fix_front_matter.py --check   检查 front-matter 缺失字段

用法（在仓库根目录执行）:
  python .tools/blog.py publish
  python .tools/blog.py build
  python .tools/blog.py deploy

注意:
  hexo deploy / git push 需要能访问 github.com。本机走 SOCKS5 代理时，
  改下面的 PROXY 常量即可；若已配好 git 全局 http.proxy，则此处兜底不生效也无妨。
"""
import os
import sys
import subprocess

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .tools 上级 = 仓库根
TOOLS = os.path.join(REPO, ".tools")
PROXY = "socks5://127.0.0.1:7897"  # 改代理端口在这里；留空字符串 "" 表示不设置


def run(cmd):
    print(">> " + cmd)
    env = os.environ.copy()
    # 兜底：若当前环境没有代理变量，则注入 PROXY，保证 deploy/commit 走代理
    if PROXY:
        for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"):
            if k not in env:
                env[k] = PROXY
    rc = subprocess.run(cmd, shell=True, cwd=REPO, env=env).returncode
    if rc != 0:
        print("[ERROR] 命令返回非零退出码: %d" % rc)
    return rc


def build():
    run("npx hexo clean")
    return run("npx hexo generate")


def deploy():
    return run("npx hexo deploy")


def commit():
    run('git add -A')
    run('git commit -m "source update"')
    return run("git push origin hexo")


def publish():
    rc = commit()
    if rc != 0:
        print("[WARN] git push 失败，仍继续生成与部署页面")
    build()
    return deploy()


def preview():
    return run("npx hexo server")


def check():
    return run('python "%s" --check' % os.path.join(TOOLS, "fix_front_matter.py"))


CMDS = {
    "build": build,
    "deploy": deploy,
    "commit": commit,
    "publish": publish,
    "preview": preview,
    "check": check,
}


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print("用法: python .tools/blog.py {%s}" % "|".join(CMDS))
        sys.exit(2)
    sys.exit(CMDS[sys.argv[1]]())
